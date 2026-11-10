"""Gera a banda sonora do Episódio 1 (92 s) -> WAV estéreo 44.1 kHz.
Uso: python3 audio.py saida.wav
"""
import sys, wave
import numpy as np

SR = 44100
DUR = 92.0
N = int(SR * DUR)
t = np.arange(N) / SR
rng = np.random.default_rng(7)
mix = np.zeros(N)


def band(x, lo, hi):
    """Filtro passa-banda no domínio da frequência."""
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    X[(f < lo) | (f > hi)] = 0
    return np.fft.irfft(X, len(x))


def env(a, b, fade=1.0):
    """Envelope 0..1 ativo entre a e b segundos, com fades."""
    e = np.clip((t - a) / fade, 0, 1) * np.clip((b - t) / fade, 0, 1)
    return e


def put(sig, at, gain=1.0):
    i = int(at * SR)
    j = min(N, i + len(sig))
    mix[i:j] += sig[: j - i] * gain


def decay(d, k):
    tt = np.arange(int(d * SR)) / SR
    return tt, np.exp(-tt * k)


# --- drone grave contínuo ---
lfo = 0.6 + 0.4 * np.sin(2 * np.pi * 0.07 * t)
drone = (np.sin(2 * np.pi * 55 * t) + 0.6 * np.sin(2 * np.pi * 82.4 * t + 1) + 0.3 * np.sin(2 * np.pi * 110.3 * t)) * lfo
drone_env = np.clip(t / 2, 0, 1) * (1 - 0.85 * env(73, 78, 0.2)) * np.clip((DUR - t) / 1.5, 0, 1)
mix += drone * drone_env * 0.10

# --- vento (ruído filtrado) ---
wind = band(rng.standard_normal(N), 80, 700)
wind /= np.abs(wind).max()
wmod = 0.5 + 0.5 * np.sin(2 * np.pi * 0.11 * t) * np.sin(2 * np.pi * 0.043 * t + 2)
mix += wind * wmod * (env(0, 31, 1.5) + env(56, 65, 1.5)) * 0.22

# --- passos ---
def step():
    tt, e = decay(0.18, 30)
    s = band(rng.standard_normal(len(tt)), 60, 900) * e
    return s / (np.abs(s).max() + 1e-9)
for a, b, per in [(7.3, 15, 0.62), (23.6, 30.5, 0.6), (31.2, 39.5, 0.75)]:
    x = a
    while x < b:
        put(step(), x, 0.25)
        x += per

# --- estática do rádio (cena 3) ---
st = band(rng.standard_normal(N), 1500, 7000)
st /= np.abs(st).max()
chop = (np.sin(2 * np.pi * 9 * t) > -0.3).astype(float)
mix += st * chop * env(16.8, 19.4, 0.1) * 0.22
# bip do canal
for at in (15.6, 16.0):
    tt, e = decay(0.12, 5)
    put(np.sin(2 * np.pi * 1400 * tt) * e, at, 0.12)

# --- zumbido do néon (cena 4) ---
buzz = np.sign(np.sin(2 * np.pi * 100 * t)) * 0.5 + np.sin(2 * np.pi * 200 * t) * 0.5
flick = (np.sin(2 * np.pi * 3.3 * t) + np.sin(2 * np.pi * 7.1 * t) > -0.6).astype(float)
mix += band(buzz, 80, 1200) * flick * env(23.2, 31, 0.6) * 0.035

# --- batimento cardíaco ---
def beat():
    tt, e = decay(0.35, 14)
    return np.sin(2 * np.pi * 52 * tt) * e + 0.5 * np.sin(2 * np.pi * 38 * tt) * e
def heart(a, b, bpm0, bpm1, g):
    x = a
    while x < b:
        k = (x - a) / (b - a)
        bpm = bpm0 + (bpm1 - bpm0) * k
        put(beat(), x, g)
        put(beat(), x + 0.22 * 60 / bpm, g * 0.7)
        x += 60 / bpm
heart(31.4, 39.8, 62, 104, 0.55)
heart(60.0, 65.0, 90, 110, 0.4)
heart(65.0, 73.0, 115, 150, 0.55)
heart(73.0, 78.0, 60, 60, 0.7)

# --- pancada / susto (40 s) ---
tt, e = decay(2.5, 2.2)
metal = sum(np.sin(2 * np.pi * f * tt) / (i + 1) for i, f in enumerate([187, 431, 693, 1021, 1543]))
thump = np.sin(2 * np.pi * 45 * tt) * np.exp(-tt * 6)
crash = band(rng.standard_normal(len(tt)), 200, 9000) * np.exp(-tt * 9)
hit = metal * e * 0.35 + thump * 1.0 + crash * 0.6
put(hit / np.abs(hit).max(), 40.0, 0.9)

# --- "sting" no grito (43.2 s) ---
tt, _ = decay(3.6, 0)
sting = sum(np.sin(2 * np.pi * f * tt) for f in [1180, 1251, 1327, 1405])
sting *= (0.6 + 0.4 * np.sin(2 * np.pi * 11 * tt)) * np.clip(tt / 0.05, 0, 1) * np.exp(-tt * 1.1)
put(sting / np.abs(sting).max(), 43.2, 0.18)

# --- pancadas na porta (cena 7) ---
for k in [1.5, 1.8, 2.1, 5.2, 5.45, 7.4, 7.6, 7.8]:
    tt, e = decay(0.5, 11)
    knock = np.sin(2 * np.pi * 70 * tt) * e + band(rng.standard_normal(len(tt)), 100, 1500) * np.exp(-tt * 30) * 0.6
    put(knock / np.abs(knock).max(), 47 + k, 0.6)

# --- horda: gemidos (cena 8-9) ---
moans = np.zeros(N)
for v in range(7):
    f0 = 85 + v * 13
    vib = np.sin(2 * np.pi * (0.3 + 0.1 * v) * t + v) * 9
    ph = 2 * np.cumsum(np.pi * (f0 + vib) / SR)
    saw = sum(np.sin(k * ph) / k for k in range(1, 12))
    am = np.clip(np.sin(2 * np.pi * (0.13 + 0.05 * v) * t + v * 1.7), 0, 1) ** 2
    moans += saw * am
moans = band(moans, 150, 1100)
moans /= np.abs(moans).max()
growth = np.clip((t - 56.5) / 8, 0, 1)
mix += moans * env(56.5, 73, 1.0) * (0.25 + 0.6 * growth) * 0.3

# --- tom de tensão a subir (56-73) ---
k = np.clip((t - 56) / 17, 0, 1)
freq = 180 + 420 * k ** 1.5
rise = np.sin(2 * np.pi * np.cumsum(freq) / SR) + 0.5 * np.sin(2 * np.pi * np.cumsum(freq * 1.5) / SR)
mix += rise * env(56, 73, 2.0) * (0.02 + 0.08 * k)

# --- tic-tac da contagem ---
for i in range(5):
    tt, e = decay(0.08, 60)
    put(band(rng.standard_normal(len(tt)), 2000, 8000) * e, 73.05 + i, 0.5)
    put(np.sin(2 * np.pi * 900 * tt) * e, 73.05 + i, 0.15)

# --- escolha: pulso grave + ding final ---
x = 78.6
while x < 90.5:
    tt, e = decay(1.0, 4)
    put(np.sin(2 * np.pi * 41 * tt) * e, x, 0.35)
    x += 1.6
for at in (79.4, 82.2):  # "whoosh" das caixas
    tt, _ = decay(0.7, 0)
    w = band(rng.standard_normal(len(tt)), 400, 5000) * np.sin(np.pi * tt / 0.7) ** 2
    put(w / np.abs(w).max(), at, 0.12)
tt, e = decay(3.0, 1.6)
ding = np.sin(2 * np.pi * 1318.5 * tt) + 0.5 * np.sin(2 * np.pi * 2637 * tt) + 0.3 * np.sin(2 * np.pi * 1975.5 * tt)
put(ding * e, 85.6, 0.16)

# --- master ---
mix = np.tanh(mix * 1.1)
mix /= np.abs(mix).max() / 0.9
# ligeira largura estéreo
d = int(0.012 * SR)
left = mix
right = np.concatenate([np.zeros(d), mix[:-d]]) * 0.85 + mix * 0.15
stereo = np.stack([left, right], axis=1)
pcm = (stereo * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print('ok', sys.argv[1])
