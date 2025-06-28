import matplotlib.pyplot as plt

def chunk_bits(bits, size=64):
    """Chunk bitstream into size-bit blocks, pad last block with zeros."""
    chunks = []
    for i in range(0, len(bits), size):
        chunk = bits[i:i+size]
        if len(chunk) < size:
            chunk += [0] * (size - len(chunk))
        chunks.append(chunk)
    return chunks

def encode_64b66b(data_bits, control=False):
    """
    Encode 64 bits into 66-bit block:
    - 2-bit sync header:
      '01' for data
      '10' for control
    - Followed by 64 bits of payload
    """
    blocks = chunk_bits(data_bits, 64)
    encoded_blocks = []

    for block in blocks:
        header = [0,1] if not control else [1,0]  # Data or Control
        encoded_blocks.extend(header + block)
    return encoded_blocks

def waveform(bits):
    """Create time and signal for plotting."""
    time = []
    signal = []
    for i, b in enumerate(bits):
        time.extend([i, i+1])
        signal.extend([b, b])
    return time, signal

def generate_clock(length):
    """Generate alternating clock bits."""
    clock = [i % 2 for i in range(length)]
    return waveform(clock)

def plot_all(data_bits, encoded_bits):
    data_time, data_signal = waveform(data_bits)
    encoded_time, encoded_signal = waveform(encoded_bits)
    clock_time, clock_signal = generate_clock(len(encoded_bits))

    plt.figure(figsize=(14, 6))

    # Clock
    plt.subplot(3, 1, 1)
    plt.step(clock_time, clock_signal, where='post', color='black')
    plt.title("Clock Signal")
    plt.ylim(-0.5, 1.5)
    plt.grid(True, alpha=0.3)

    # Raw Data
    plt.subplot(3, 1, 2)
    plt.step(data_time, data_signal, where='post', color='blue')
    plt.title("Input Data (Raw bits)")
    plt.ylim(-0.5, 1.5)
    plt.grid(True, alpha=0.3)

    # Encoded Data
    plt.subplot(3, 1, 3)
    plt.step(encoded_time, encoded_signal, where='post', color='green')
    plt.title("64b/66b Encoded Output")
    plt.ylim(-0.5, 1.5)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("64b66b_encoded.png", dpi=150)
    print("Plot saved as '64b66b_encoded.png'")

# === MAIN ===

if __name__ == "__main__":
    # Example: 130 bits of random data (2 full 64-bit blocks + 2 bits padding)
    import random
    random.seed(42)
    data = [random.randint(0,1) for _ in range(130)]

    print(f"Input bits length: {len(data)}")

    encoded = encode_64b66b(data, control=False)

    print(f"Encoded bits length: {len(encoded)} (should be multiple of 66)")

    plot_all(data, encoded)
