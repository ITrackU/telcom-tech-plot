import numpy as np
import matplotlib.pyplot as plt

# 64-QAM: I and Q ∈ {-7, -5, -3, -1, +1, +3, +5, +7}
levels = np.arange(-7, 8, 2)
symbols = np.array([(i, q) for i in levels for q in levels], dtype=float)

# Normalize to unit average power
symbols /= np.sqrt(np.mean(np.square(symbols)))

# I and Q components
I = symbols[:, 0]
Q = symbols[:, 1]

# Plot setup
plt.figure(figsize=(7, 7))
plt.scatter(I, Q, color='purple', s=60)

# Optional: enumerate points (uncomment if needed)
# for i, (x, y) in enumerate(zip(I, Q)):
#     plt.text(x + 0.1, y + 0.1, f"{i}", ha='center', fontsize=6)

# Axes and layout
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.title("64-QAM Constellation Diagram")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True, linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')

# Save the figure
plt.savefig("64qam_constellation.png", dpi=300, bbox_inches='tight')
