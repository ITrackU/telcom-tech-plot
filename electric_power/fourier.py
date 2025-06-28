import numpy as np
import matplotlib.pyplot as plt

# Paramètres
f = 50                # Fréquence fondamentale en Hz
T = 1 / f             # Période en secondes
A = 1                 # Amplitude de l'onde carrée
N = 20                # Nombre de termes de la série (harmoniques impairs)
t = np.linspace(0, 2 * T, 1000)  # Deux périodes

# Série de Fourier d'une onde carrée (somme de sinusoïdes impaires)
def fourier_square_wave(t, f, N):
    result = np.zeros_like(t)
    for n in range(1, N + 1, 2):  # Seulement les harmoniques impairs
        result += (1 / n) * np.sin(2 * np.pi * n * f * t)
    return (4 / np.pi) * result

# Calcul des signaux
fourier_signal = fourier_square_wave(t, f, N)
original_square = np.sign(np.sin(2 * np.pi * f * t))

# Tracé
plt.figure(figsize=(12, 6))

# Signal reconstruit vs original
plt.subplot(2, 1, 1)
plt.plot(t * 1000, original_square, label="Onde carrée réelle", color='black', linestyle='--')
plt.plot(t * 1000, fourier_signal, label=f"Série de Fourier (N={N})", color='red')
plt.title("Reconstruction d'une onde carrée par série de Fourier")
plt.xlabel("Temps (ms)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Spectre des harmoniques
# Spectre des harmoniques (corrigé sans use_line_collection)
plt.subplot(2, 1, 2)
harmoniques = np.arange(1, N + 1, 2)
amplitudes = (4 / np.pi) * (1 / harmoniques)
plt.stem(harmoniques * f, amplitudes, basefmt=" ") 
plt.title("Spectre en amplitude des harmoniques (onde carrée)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.savefig("serie_fourier_square.png", dpi=300)
