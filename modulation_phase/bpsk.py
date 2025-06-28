import numpy as np
import matplotlib.pyplot as plt

# BPSK symbols: -1 and +1 along the I-axis
bpsk_symbols = np.array([-1, 1])  # Only real part, Q = 0

# Create the plot
plt.figure(figsize=(6, 6))
plt.scatter(bpsk_symbols, np.zeros_like(bpsk_symbols), color='blue', s=100)

# Annotate each symbol
for symbol in bpsk_symbols:
    plt.text(symbol, 0.1, f"{symbol}", ha='center', fontsize=12)

# Axis and formatting
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.xlim(-2, 2)
plt.ylim(-1, 1)
plt.title("BPSK Constellation Diagram")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Save the plot to a file
plt.savefig("bpsk_constellation.png", dpi=300, bbox_inches='tight')
