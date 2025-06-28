import numpy as np
import matplotlib.pyplot as plt

# 256-QAM: I and Q ∈ {-15, -13, ..., +15}
levels = np.arange(-15, 16, 2)
symbols = np.array([(i, q) for i in levels for q in levels], dtype=float)

# Normalize average symbol power to 1
symbols /= np.sqrt(np.mean(np.square(symbols)))

# Split into I and Q components
I = symbols[:, 0]
Q = symbols[:, 1]

# Plot
plt.figure(figsize=(8, 8))
plt.scatter(I, Q, color='darkorange', s=30)

# Axes and layout
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.title("256-QAM Constellation Diagram")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True, linestyle='--', linewidth=0.4)
plt.gca().set_aspect('equal', adjustable='box')

# Save to file
plt.savefig("256qam_constellation.png", dpi=300, bbox_inches='tight')
