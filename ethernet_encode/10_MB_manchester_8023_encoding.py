import matplotlib.pyplot as plt

# Example data bits
data = [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1]

def data_line(bits):
    """Generate data line"""
    time = []
    signal = []
    for i, bit in enumerate(bits):
        time += [i, i+1]
        signal += [bit, bit]
    return time, signal

def generate_clock(bit_count):
    """Clock signal for IEEE 802.3 Manchester (low-to-high)"""
    time = []
    clock = []
    for i in range(bit_count):
        t0 = i
        t1 = t0 + 0.5
        t2 = t0 + 1
        time += [t0, t1, t1, t2]
        clock += [0, 0, 1, 1]  # Low first half, High second half
    return time, clock

def manchester_encode_xor(bits):
    """IEEE 802.3 Manchester Encoding using XOR (Data XOR Clock)"""
    time = []
    signal = []

    for i, bit in enumerate(bits):
        t0 = i
        t1 = i + 0.5
        t2 = i + 1

        # IEEE 802.3 clock pattern: [0, 1]
        clock_first = 0
        clock_second = 1

        first_half = bit ^ clock_first
        second_half = bit ^ clock_second

        time += [t0, t1, t1, t2]
        signal += [first_half, first_half, second_half, second_half]

    return time, signal

def plot_manchester():
    """Plot Data, Clock, and IEEE 802.3 Manchester Encoded signals"""
    data_time, data_signal = data_line(data)
    clock_time, clock_signal = generate_clock(len(data))
    manch_xor_time, manch_xor_signal = manchester_encode_xor(data)
    
    plt.figure(figsize=(14, 8))

    # Original Data
    plt.subplot(3, 1, 1)
    plt.step(data_time, data_signal, where='post', linewidth=2, color='red')
    plt.title('Original Data')
    plt.ylabel('Level')
    plt.ylim(-0.5, 1.5)
    plt.grid(True, alpha=0.3)
    for i, bit in enumerate(data):
        plt.text(i + 0.5, bit + 0.1, str(bit), ha='center', va='bottom', fontweight='bold')

    # Clock
    plt.subplot(3, 1, 2)
    plt.step(clock_time, clock_signal, where='post', linewidth=2, color='orange')
    plt.title('Clock Signal (IEEE 802.3 Convention)')
    plt.ylabel('Level')
    plt.ylim(-0.5, 1.5)
    plt.grid(True, alpha=0.3)

    # Manchester XOR (IEEE 802.3)
    plt.subplot(3, 1, 3)
    plt.step(manch_xor_time, manch_xor_signal, where='post', linewidth=2, color='purple')
    plt.title('Manchester Encoded (IEEE 802.3: XOR Method)')
    plt.ylabel('Level')
    plt.xlabel('Time (bit periods)')
    plt.ylim(-0.5, 1.5)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('manchester_8023_encoding.png', dpi=150, bbox_inches='tight')
    print("Plot saved as 'manchester_8023_encoding.png'")

def verify_encoding(bits):
    """Print bit-level encoding verification for IEEE 802.3"""
    signal_time, signal = manchester_encode_xor(bits)

    print("\nIEEE 802.3 Manchester Encoding Verification:")
    print("Bit | Encoded Signal [first_half, second_half]")
    print("----|-------------------------------------------")
    for i, bit in enumerate(bits):
        idx = i * 4
        fh = signal[idx]
        sh = signal[idx + 2]
        print(f" {bit}  | [{fh}, {sh}]   → {'low-to-high' if bit == 0 else 'high-to-low'}")

# Run
if __name__ == "__main__":
    print("Data bits:", data)
    verify_encoding(data[:8])  # check first 8 bits for clarity
    plot_manchester()
