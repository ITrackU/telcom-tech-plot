import matplotlib.pyplot as plt

# 4B/5B encoding table
FOURB_FIVEB_TABLE = {
    '0': '11110', '1': '01001', '2': '10100', '3': '10101',
    '4': '01010', '5': '01011', '6': '01110', '7': '01111',
    '8': '10010', '9': '10011', 'A': '10110', 'B': '10111',
    'C': '11010', 'D': '11011', 'E': '11100', 'F': '11101',
}

def chunk_bits(bits, size=4):
    """Split bits into groups of size, pad with 0s if needed."""
    chunks = []
    for i in range(0, len(bits), size):
        chunk = bits[i:i+size]
        if len(chunk) < size:
            chunk += [0] * (size - len(chunk))
        chunks.append(chunk)
    return chunks

def bits_to_hex_symbol(bits):
    return hex(int(''.join(str(b) for b in bits), 2))[2:].upper()

def encode_4b5b_from_bits(bitstream):
    hex_symbols = [bits_to_hex_symbol(chunk) for chunk in chunk_bits(bitstream)]
    encoded_bits = []
    for symbol in hex_symbols:
        encoded_bits.extend([int(b) for b in FOURB_FIVEB_TABLE[symbol]])
    return hex_symbols, encoded_bits

def waveform(bits):
    """Generate time and signal lists for waveform plotting"""
    time = []
    signal = []
    for i, bit in enumerate(bits):
        time += [i, i + 1]
        signal += [bit, bit]
    return time, signal

def generate_clock(length):
    """Generate alternating clock signal"""
    clock = [i % 2 for i in range(length)]
    return waveform(clock)

def plot_all(data_bits, encoded_bits, symbols):
    # Raw data line (before 4B/5B)
    data_time, data_signal = waveform(data_bits)
    
    # Encoded signal (after 4B/5B)
    encoded_time, encoded_signal = waveform(encoded_bits)
    
    # Clock (same length as encoded bits)
    clock_time, clock_signal = generate_clock(len(encoded_bits))

    plt.figure(figsize=(14, 5))
    
    # Clock
    plt.subplot(3, 1, 1)
    plt.step(clock_time, clock_signal, where='post', label='Clock', color='black')
    plt.title("Clock Signal")
    plt.ylim(-0.5, 1.5)
    plt.yticks([0, 1])
    plt.grid(True, alpha=0.3)

    # Raw Data Input
    plt.subplot(3, 1, 2)
    plt.step(data_time, data_signal, where='post', label='Data Input', color='blue')
    plt.title("Data Input (Unencoded)")
    plt.ylim(-0.5, 1.5)
    plt.yticks([0, 1])
    plt.grid(True, alpha=0.3)

    # Encoded Output
    plt.subplot(3, 1, 3)
    plt.step(encoded_time, encoded_signal, where='post', label='4B/5B Encoded Output', color='green')
    plt.title("4B/5B Encoded Output")
    plt.ylim(-0.5, 1.5)
    plt.yticks([0, 1])
    plt.grid(True, alpha=0.3)

    # Add symbol labels
    for i, symbol in enumerate(symbols):
        plt.text(i * 5 + 2.5, 1.2, symbol, ha='center', va='center', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.savefig("4b5b_full_diagram.png", dpi=150)
    print("Diagram saved as '4b5b_full_diagram.png'")

# === MAIN ===

if __name__ == "__main__":
    data = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1]
    print("Input bits:", data)

    symbols, encoded = encode_4b5b_from_bits(data)

    print("Symbols (4-bit):", symbols)
    print("Encoded bits:", encoded)

    plot_all(data, encoded, symbols)
