import numpy as np
import matplotlib.pyplot as plt

# 16-QAM: I and Q ∈ {-3, -1, +1, +3}
levels = [-3, -1, 1, 3]
symbols = np.array([(i, q) for i in levels for q in levels], dtype=float)

# Normalize power to 1 (optional for clarity)
symbols /= np.sqrt(np.mean(np.square(symbols)))

I = symbols[:, 0]
Q = symbols[:, 1]

# Plot
plt.figure(figsize=(6, 6))
plt.scatter(I, Q, color='red', s=80)

# Annotate each point with small, shifted text to prevent overlap
for i, (x, y) in enumerate(zip(I, Q)):
    x_offset = 0.15 if i % 2 == 0 else -0.25
    y_offset = 0.15 if i % 3 == 0 else -0.20
    plt.text(x + x_offset, y + y_offset, f"({x:.1f},{y:.1f})", ha='center', fontsize=7)

# Axes and formatting
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.title("16-QAM Constellation Diagram")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Save the figure
plt.savefig("16qam_constellation.png", dpi=300, bbox_inches='tight')
