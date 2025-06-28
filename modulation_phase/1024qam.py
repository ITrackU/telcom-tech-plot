import numpy as np
import matplotlib.pyplot as plt

# 1024-QAM: I and Q ∈ {-31, -29, ..., +31}
levels = np.arange(-31, 32, 2)
symbols = np.array([(i, q) for i in levels for q in levels], dtype=float)

# Normalize to unit average power
symbols /= np.sqrt(np.mean(np.square(symbols)))

# Separate I and Q components
I = symbols[:, 0]
Q = symbols[:, 1]

# Plot
plt.figure(figsize=(9, 9))
plt.scatter(I, Q, color='navy', s=10)

# Axes and layout
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.title("1024-QAM Constellation Diagram")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True, linestyle='--', linewidth=0.3)
plt.gca().set_aspect('equal', adjustable='box')

# Save to file
plt.savefig("1024qam_constellation.png", dpi=300, bbox_inches='tight')
