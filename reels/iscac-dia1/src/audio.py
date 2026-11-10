"""Banda sonora do reel ISCAC · DIA 1 (45 s) -> WAV estéreo 44.1 kHz.
Uso: python3 audio.py saida.wav
"""
import sys, wave
import numpy as np

SR = 44100
DUR = 45.0
N = int(SR * DUR)
t = np.arange(N) / SR
rng = np.random.default_rng(3)
mix = np.zeros(N)


def band(x, lo, hi):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    X[(f < lo) | (f > hi)] = 0
    return np.fft.irfft(X, len(x))


def put(sig, at, gain=1.0):
    i = int(at * SR); j = min(N, i + len(sig))
    if i < N: mix[i:j] += sig[: j - i] * gain


def tt(d): return np.arange(int(d * SR)) / SR


def tone(f, d, k=6, wave_='sine'):
    x = tt(d); ph = 2 * np.pi * f * x
    s = np.sin(ph) if wave_ == 'sine' else np.sign(np.sin(ph)) * .6
    return s * np.exp(-x * k)


def kick():
    x = tt(.35); f = 50 + 90 * np.exp(-x * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x * 9)


def hat():
    x = tt(.06); return band(rng.standard_normal(len(x)), 6000, 14000) * np.exp(-x * 70)


def snare():
    x = tt(.2); return band(rng.standard_normal(len(x)), 1200, 7000) * np.exp(-x * 22) * .7 + np.sin(2 * np.pi * 190 * x) * np.exp(-x * 25) * .5



def buzzer(at, g=.3):
    d = tt(.6); put(np.sign(np.sin(2 * np.pi * 110 * d)) * .5 * (d < .55), at, g); put(kick(), at, .5)
def whoosh(at, g=.3, d_=.6):
    d = tt(d_); w = band(rng.standard_normal(len(d)), 300, 6000) * np.sin(np.pi * d / d_) ** 2; put(w / np.abs(w).max(), at, g)
def click(at, g=.25):
    d = tt(.05); put(band(rng.standard_normal(len(d)), 2000, 9000) * np.exp(-d * 90), at, g)
def thud(at, g=.6):
    d = tt(.5); s = np.sin(2 * np.pi * 60 * d) * np.exp(-d * 9) + band(rng.standard_normal(len(d)), 100, 2500) * np.exp(-d * 25) * .6
    put(s / np.abs(s).max(), at, g)

# --- 0-29.3: batida lo-fi de estudo com tic-tac (para no PUM!) ---
bpm = 92; b = 60 / bpm; x = 0.25; bass = [55, 55, 65.4, 49]; i = 0
while x < 29.25:
    fast = 23.4 <= x < 26.4  # time-lapse: hi-hats a dobrar
    put(kick(), x, .55 if i % 4 in (0, 2) else 0)
    put(snare(), x, .35 if i % 4 in (1, 3) else 0)
    put(hat(), x, .18); put(hat(), x + b / 2, .1)
    if fast:
        put(hat(), x + b / 4, .12); put(hat(), x + 3 * b / 4, .12)
    put(tone(1900 if i % 2 else 1500, .03, 80), x, .12)
    if i % 4 == 0: put(tone(bass[(i // 4) % 4], b * 4, 1.2), x, .35)
    x += b; i += 1

# CENA 1: dúvida + zoom out + slot machine
for at in (1.6, 2.3):
    d = tt(.4); put(np.sin(2 * np.pi * np.cumsum(300 + 200 * np.sin(d * 30)) / SR) * np.exp(-d * 7), at, .15)
whoosh(2.95, .3, .7)
y = 4.7
while y < 7.2:  # roleta a abrandar
    click(y, .2); k = (y - 4.7) / 2.5; y += .05 + .25 * k ** 2
for k_, f in enumerate((523, 659, 784)): put(tone(f, .2, 8, 'sq'), 7.25 + k_ * .06, .12)
buzzer(7.45, .25)

# pen (9-11.3)
d = tt(2.2); put(band(rng.standard_normal(len(d)), 2500, 9000) * (np.sin(2 * np.pi * 7 * d) > 0) * .5, 9.05, .25)
put(tone(220, .3, 4, 'sq'), 10.1, .2); put(tone(196, .4, 4, 'sq'), 10.35, .2)
# T (11.3-13.8)
for at in (11.55, 12.1):
    d = tt(.35); put(np.sin(2 * np.pi * np.cumsum(400 + 800 * d / .35) / SR) * np.exp(-d * 4), at, .15)
buzzer(13.05)
# IVA (13.8-17)
for off in (.1, .25, .4, .55, .8, 1.0, 1.15, 1.4): click(13.8 + off, .35); put(tone(1200, .04, 60), 13.8 + off, .08)
d = tt(.5); put(np.sin(2 * np.pi * np.cumsum(500 + 900 * d) / SR) * np.exp(-d * 5), 15.25, .15)
d = tt(1.2); put(band(rng.standard_normal(len(d)), 80, 5000) * np.exp(-d * 4), 15.8, .55); put(kick(), 15.8, .7)
d = tt(.8); put(band(rng.standard_normal(len(d)), 3000, 9000) * np.exp(-d * 3), 16.0, .12)
# Balança (17-20.2)
d = tt(1.2); put(np.sin(2 * np.pi * (180 + 40 * np.sin(2 * np.pi * 3 * d)) * d) * .3 * np.exp(-d * 1.5), 17.0, .2)
thud(18.25, .6); buzzer(18.5)
# FIFO (20.2-23.4)
whoosh(20.6, .2, .5); buzzer(21.4)
for k_ in range(4): thud(22.3 + k_ * .09 + rng.random() * .05, .5)
# time-lapse (23.4-26.4): fita a acelerar + "−20%"
d = tt(3.0); f = 200 + 900 * d / 3
put(band(np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)), 100, 3000) * .15 * np.clip(d / .2, 0, 1) * np.clip((3 - d) / .2, 0, 1), 23.4, .5)
for k_ in range(1, 5): put(tone(330, .15, 10, 'sq'), 23.4 + k_ * .6, .12)
# café (26.4-29.3)
for k_ in range(4):
    d = tt(.16); put(np.sin(2 * np.pi * np.cumsum(260 - 900 * d) / SR) * np.exp(-d * 18), 26.9 + k_ * .17, .4)
d = tt(.9); put(np.sin(2 * np.pi * np.cumsum(300 + 2500 * d) / SR) * np.exp(-d * 2), 27.5, .18)
d = tt(1.0); put(np.sin(2 * np.pi * 60 * d) * (0.5 + .5 * np.sign(np.sin(2 * np.pi * 25 * d))), 27.5, .15)
d = tt(.7); put(np.sin(2 * np.pi * np.cumsum(1400 - 1100 * d / .7) / SR) * np.exp(-d * 1.5), 28.55, .12)
# PUM! (29.3) + squeak + plop
d = tt(1.2); th = np.sin(2 * np.pi * 70 * d) * np.exp(-d * 6) + band(rng.standard_normal(len(d)), 200, 4000) * np.exp(-d * 20) * .5
th += sum(np.sin(2 * np.pi * f_ * d) for f_ in (1650, 2320, 3110)) * np.exp(-d * 5) * .08
put(th / np.abs(th).max(), 29.3, .9)
d = tt(1.5); f = 1700 + 500 * np.sin(2 * np.pi * 3 * d) + 300 * np.sin(2 * np.pi * 11 * d)
put(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.clip(d / .1, 0, 1) * np.clip((1.5 - d) / .2, 0, 1), 30.3, .1)
d = tt(.2); put(np.sin(2 * np.pi * np.cumsum(200 + 900 * d / .2) / SR) * np.exp(-d * 15), 31.95, .45)
# trombone triste (32.8-36.6)
def womp(f0, f1, dur):
    d = tt(dur); f = np.linspace(f0, f1, len(d)) * (1 + .012 * np.sin(2 * np.pi * 6 * d)); ph = 2 * np.pi * np.cumsum(f) / SR
    s = sum(np.sin(k * ph) / k for k in range(1, 9)); return band(s, 80, 2500) * np.clip(d / .05, 0, 1) * np.clip((dur - d) / .12, 0, 1)
for at, f0, f1, du in ((32.9, 233, 226, .6), (33.6, 220, 213, .6), (34.3, 207, 200, .6), (35.0, 196, 170, 1.6)):
    put(womp(f0, f1, du), at, .13)
# CENA 4 (37-45): alarme + LEVEL UP + batida rápida
for k_ in range(3): put(np.sign(np.sin(2 * np.pi * (880 if k_ % 2 == 0 else 660) * tt(.22))) * .4, 37.0 + k_ * .24, .15)
for k_, f in enumerate((523.3, 659.3, 784, 1046.5, 1318.5)): put(tone(f, .35, 5, 'sq'), 37.78 + k_ * .07, .16)
bpm = 128; b = 60 / bpm; x = 38.0; i = 0
while x < 45:
    put(kick(), x, .6); put(hat(), x + b / 2, .2)
    if i % 2: put(snare(), x, .4)
    put(tone([65.4, 65.4, 77.8, 87.3][(i // 4) % 4], b, 3, 'sq'), x, .12)
    x += b; i += 1
for k_ in range(3): put(tone(1567, .3, 7), 38.2 + k_ * .22, .14)
put(tone(1318.5, .5, 4), 42.6, .15); put(tone(1760, .6, 4), 42.75, .15)  # "segue"
mix = np.tanh(mix * 1.2)
mix *= np.clip((DUR - t) / .3, 0, 1)
mix /= np.abs(mix).max() / .9
d = int(.01 * SR)
right = np.concatenate([np.zeros(d), mix[:-d]]) * .8 + mix * .2
pcm = (np.stack([mix, right], 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('ok')
