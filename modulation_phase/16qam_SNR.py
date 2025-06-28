import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# === Paramètres de la modulation (ici 16-QAM) ===
levels = [-3, -1, 1, 3]
symbols = np.array([(i, q) for i in levels for q in levels], dtype=float)

# Normalisation de la puissance moyenne
symbols /= np.sqrt(np.mean(np.square(symbols)))

# I/Q idéaux
I_symbols = symbols[:, 0]
Q_symbols = symbols[:, 1]

# === Paramètres de l’animation ===
snr_db_list = np.linspace(2, 30, 60)  # SNR de 2 dB à 30 dB
n_noise_points = 500  # Nombre de symboles bruités par frame

# === Création de la figure ===
fig, ax = plt.subplots(figsize=(6, 6))
scat = ax.scatter([], [], s=10, color='blue', alpha=0.5)
title = ax.text(0.5, 1.05, "", transform=ax.transAxes, ha="center", fontsize=14)

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_xlabel("In-phase (I)")
ax.set_ylabel("Quadrature (Q)")
ax.set_title("16-QAM with AWGN Noise")
ax.grid(True)
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(0, color='gray', linewidth=0.8)
ax.set_aspect('equal')

# === Fonction d’animation ===
def update(frame):
    snr_db = snr_db_list[frame]
    snr_linear = 10 ** (snr_db / 10)
    noise_power = 1 / (2 * snr_linear)

    # Génération des symboles bruités
    idx = np.random.randint(0, len(symbols), size=n_noise_points)
    chosen_symbols = symbols[idx]
    noise = np.random.normal(scale=np.sqrt(noise_power), size=(n_noise_points, 2))
    noisy_symbols = chosen_symbols + noise

    # Mise à jour du graphique
    scat.set_offsets(noisy_symbols)
    title.set_text(f"SNR = {snr_db:.1f} dB")
    return scat, title

# === Animation ===
anim = FuncAnimation(fig, update, frames=len(snr_db_list), interval=500, blit=True)

# === Export en GIF (nécessite ImageMagick ou Pillow) ===
anim.save("16qam_snr_animation.gif", writer=PillowWriter(fps=15))

# Pour afficher l'animation dans Jupyter Notebook (facultatif)
# from IPython.display import Image
# Image(filename="16qam_snr_animation.gif")

