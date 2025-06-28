import numpy as np
import matplotlib.pyplot as plt

# QPSK symbols: 4 points, 90 degrees apart
# Typically: (±1, ±1), normalized
qpsk_symbols = np.array([
    (1, 1),
    (-1, 1),
    (-1, -1),
    (1, -1)
]) / np.sqrt(2)  # Normalize power to 1

# Separate I and Q components
I = qpsk_symbols[:, 0]
Q = qpsk_symbols[:, 1]

# Create the plot
plt.figure(figsize=(6, 6))
plt.scatter(I, Q, color='green', s=100)

# Annotate each symbol
for i, (x, y) in enumerate(zip(I, Q)):
    plt.text(x, y + 0.1, f"({x:.2f}, {y:.2f})", ha='center', fontsize=10)

# Axis and formatting
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.title("QPSK Constellation Diagram")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Save the plot to a file
plt.savefig("qpsk_constellation.png", dpi=300, bbox_inches='tight')
