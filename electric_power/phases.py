import numpy as np
import matplotlib.pyplot as plt

# Time array (0 to 40 ms, enough for 2 full cycles at 50Hz)
t = np.linspace(0, 0.04, 1000)

# Frequency and angular frequency
f = 50  # Hz
omega = 2 * np.pi * f

# Peak voltage from RMS value (RMS = V_peak / √2)
V_rms = 230  # Phase voltage
V_peak = V_rms * np.sqrt(2)

# Generate three phase signals, offset by 120 degrees (2π/3 radians)
Va = V_peak * np.sin(omega * t)              # Phase A
Vb = V_peak * np.sin(omega * t - 2*np.pi/3)  # Phase B
Vc = V_peak * np.sin(omega * t + 2*np.pi/3)  # Phase C

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t * 1000, Va, label='Phase A', color='red')
plt.plot(t * 1000, Vb, label='Phase B', color='green')
plt.plot(t * 1000, Vc, label='Phase C', color='blue')

plt.title('Three-Phase AC Voltage (50Hz, 230V RMS per phase)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.tight_layout()

# Save the figure instead of showing it
plt.savefig("three_phase.png", dpi=300)
