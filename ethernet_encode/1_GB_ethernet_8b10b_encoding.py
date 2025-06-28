import matplotlib.pyplot as plt

# Demo 8b/10b data table (subset for example purposes)
EIGHTB_TENB_TABLE = {
    0xCB: '1001110100',  # D.21.5 example
    0x55: '0101010100',  # D.17.2 example
    0xAB: '1010101100',  # D.21.2 example
    0xF0: '1111000100',  # D.30.0 example
    0xAA: '1010101001',  # D.21.1 example
    0x33: '0011001100',  # D.12.3 example
}

def chunk_bits(bits, size=8):
    """Chunk bitstream into 8-bit bytes, pad last with 0s if needed."""
    chunks = []
    for i in range(0, len(bits), size):
        chunk = bits[i:i+size]
        if len(chunk) < size:
            chunk += [0] * (size - len(chunk))
        chunks.append(chunk)
    return chunks

def bits_to_byte(chunk):
    return int(''.join(str(b) for b in chunk), 2)

def encode_8b10b(data_bits):
    byte_chunks = chunk_bits(data_bits, size=8)
    encoded_bits = []
    symbols = []

    for chunk in byte_chunks:
        byte_val = bits_to_byte(chunk)
        if byte_val not in EIGHTB_TENB_TABLE:
            raise ValueError(f"No encoding for byte 0x{byte_val:02X}")
        tenb = [int(b) for b in EIGHTB_TENB_TABLE[byte_val]]
        encoded_bits.extend(tenb)
        symbols.append(f'{byte_val:02X}')
    
    return symbols, encoded_bits

def waveform(bits):
    """Create time vs value lists"""
    time = []
    signal = []
    for i, bit in enumerate(bits):
        time += [i, i+1]
        signal += [bit, bit]
    return time, signal

def generate_clock(length):
    clock = [i % 2 for i in range(length)]
    return waveform(clock)

def plot_all(data_bits, encoded_bits, symbols):
    data_time, data_signal = waveform(data_bits)
    encoded_time, encoded_signal = waveform(encoded_bits)
    clock_time, clock_signal = generate_clock(len(encoded_bits))

    plt.figure(figsize=(14, 5))

    # Clock
    plt.subplot(3, 1, 1)
    plt.step(clock_time, clock_signal, where='post', color='black')
    plt.title("Clock Signal")
    plt.ylim(-0.5, 1.5)
    plt.grid(True, alpha=0.3)

    # Raw Data
    plt.subplot(3, 1, 2)
    plt.step(data_time, data_signal, where='post', color='blue')
    plt.title("Data Input (8-bit bytes)")
    plt.ylim(-0.5, 1.5)
    plt.grid(True, alpha=0.3)

    # Encoded
    plt.subplot(3, 1, 3)
    plt.step(encoded_time, encoded_signal, where='post', color='green')
    plt.title("8b/10b Encoded Output")
    plt.ylim(-0.5, 1.5)
    plt.grid(True, alpha=0.3)

    for i, sym in enumerate(symbols):
        plt.text(i * 10 + 5, 1.2, sym, ha='center', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.savefig("8b10b_encoded.png", dpi=150)
    print("Diagram saved as '8b10b_encoded.png'")

# === MAIN ===

if __name__ == "__main__":
    # You can modify the input bits below (must be in 8-bit groups matching known bytes in the table)
    data = [
        1, 0, 1, 0, 1, 0, 1, 1,  # 0xAB
        0, 1, 0, 1, 0, 1, 0, 1,  # 0x55
        1, 1, 1, 1, 0, 0, 0, 0   # 0xF0
    ]
    
    print("Input bits:", data)

    symbols, encoded = encode_8b10b(data)

    print("Symbols (8-bit bytes):", symbols)
    print("Encoded bits:", encoded)

    plot_all(data, encoded, symbols)
