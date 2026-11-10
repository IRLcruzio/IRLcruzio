"""Banda sonora do reel ISCAC · DIA 1 (30 s) -> WAV estéreo 44.1 kHz.
Uso: python3 audio.py saida.wav
"""
import sys, wave
import numpy as np

SR = 44100
DUR = 30.0
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


# --- 0-17.7: lo-fi "estudo" com tensão (relógio a fazer tic-tac) ---
bpm = 92; b = 60 / bpm; x = 0.25
bass = [55, 55, 65.4, 49]
i = 0
while x < 17.65:
    put(kick(), x, .55 if i % 4 in (0, 2) else 0)
    put(snare(), x, .35 if i % 4 in (1, 3) else 0)
    put(hat(), x, .18); put(hat(), x + b / 2, .1)
    put(tone(1900 if i % 2 else 1500, .03, 80), x, .12)  # tic-tac
    if i % 4 == 0:
        put(tone(bass[(i // 4) % 4], b * 4, 1.2), x, .35)
    x += b; i += 1

# --- whoosh do zoom-out (3.0) ---
d = tt(.7); w = band(rng.standard_normal(len(d)), 300, 6000) * np.sin(np.pi * d / .7) ** 2
put(w / np.abs(w).max(), 2.95, .3)
# confusão (1.6-3): "boing" de dúvida
for at in (1.6, 2.3):
    d = tt(.4); put(np.sin(2 * np.pi * np.cumsum(300 + 200 * np.sin(d * 30)) / SR) * np.exp(-d * 7), at, .15)

# --- caneta sem tinta (10-12.3) ---
d = tt(2.2); scr = band(rng.standard_normal(len(d)), 2500, 9000) * (np.sin(2 * np.pi * 7 * d) > 0) * .5
put(scr, 10.05, .25)
put(tone(220, .3, 4, 'sq'), 11.1, .2); put(tone(196, .4, 4, 'sq'), 11.35, .2)

# --- T de razão: troca dos rótulos + buzzer ERRADO ---
for at in (12.55, 13.1):
    d = tt(.35); put(np.sin(2 * np.pi * np.cumsum(400 + 800 * d / .35) / SR) * np.exp(-d * 4), at, .15)
d = tt(.6); put(np.sign(np.sin(2 * np.pi * 110 * d)) * .5 * (d < .55), 14.05, .3)
put(kick(), 14.05, .6)

# --- café: glup glup + "zing" cafeína ---
for k in range(4):
    d = tt(.16); put(np.sin(2 * np.pi * np.cumsum(260 - 900 * d) / SR) * np.exp(-d * 18), 15.3 + k * .17, .4)
d = tt(.9); put(np.sin(2 * np.pi * np.cumsum(300 + 2500 * d) / SR) * np.exp(-d * 2), 15.9, .18)
d = tt(1.0); put(np.sin(2 * np.pi * 60 * d) * (0.5 + .5 * np.sign(np.sin(2 * np.pi * 25 * d))), 15.9, .15)
# cabeceio: assobio a descer
d = tt(.7); put(np.sin(2 * np.pi * np.cumsum(1400 - 1100 * d / .7) / SR) * np.exp(-d * 1.5), 16.95, .12)

# --- PUM! no vidro + squeak ---
d = tt(1.2); thud = np.sin(2 * np.pi * 70 * d) * np.exp(-d * 6) + band(rng.standard_normal(len(d)), 200, 4000) * np.exp(-d * 20) * .5
thud += sum(np.sin(2 * np.pi * f * d) for f in (1650, 2320, 3110)) * np.exp(-d * 5) * .08
put(thud / np.abs(thud).max(), 17.7, .9)
d = tt(1.5); f = 1700 + 500 * np.sin(2 * np.pi * 3 * d) + 300 * np.sin(2 * np.pi * 11 * d)
put(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.clip(d / .1, 0, 1) * np.clip((1.5 - d) / .2, 0, 1), 18.7, .1)
# plop ao descolar
d = tt(.2); put(np.sin(2 * np.pi * np.cumsum(200 + 900 * d / .2) / SR) * np.exp(-d * 15), 20.35, .45)

# --- trombone triste (womp womp) 21.3-24.6 ---
def womp(f0, f1, dur):
    d = tt(dur); f = np.linspace(f0, f1, len(d)) * (1 + .012 * np.sin(2 * np.pi * 6 * d))
    ph = 2 * np.pi * np.cumsum(f) / SR
    s = sum(np.sin(k * ph) / k for k in range(1, 9))
    return band(s, 80, 2500) * np.clip(d / .05, 0, 1) * np.clip((dur - d) / .12, 0, 1)
for at, f0, f1, du in ((21.3, 233, 226, .6), (22.0, 220, 213, .6), (22.7, 207, 200, .6), (23.4, 196, 170, 1.4)):
    put(womp(f0, f1, du), at, .13)

# --- CENA 4: alarme + LEVEL UP + batida rápida ---
for k in range(3):
    put(np.sign(np.sin(2 * np.pi * (880 if k % 2 == 0 else 660) * tt(.22))) * .4, 25.0 + k * .24, .15)
for k, f in enumerate((523.3, 659.3, 784, 1046.5, 1318.5)):
    put(tone(f, .35, 5, 'sq'), 25.78 + k * .07, .16)
bpm = 128; b = 60 / bpm; x = 26.0; i = 0
while x < 30:
    put(kick(), x, .6); put(hat(), x + b / 2, .2)
    if i % 2: put(snare(), x, .4)
    put(tone([65.4, 65.4, 77.8, 87.3][(i // 4) % 4], b, 3, 'sq'), x, .12)
    x += b; i += 1
for k in range(3):  # pings das regras
    put(tone(1567, .3, 7), 26.2 + k * .22, .14)

mix = np.tanh(mix * 1.2)
mix *= np.clip((DUR - t) / .3, 0, 1)
mix /= np.abs(mix).max() / .9
d = int(.01 * SR)
right = np.concatenate([np.zeros(d), mix[:-d]]) * .8 + mix * .2
pcm = (np.stack([mix, right], 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('ok')
