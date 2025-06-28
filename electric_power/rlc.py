import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
R1 = 1      # Ohm
R2 = 1      # Ohm
L1 = 1e-3   # H
L2 = 1e-3   # H
C1 = 1e-6   # F
C2 = 1e-6   # F

f = 50                   # Hz
omega = 2 * np.pi * f
V_rms = 230              # RMS
V_peak = V_rms * np.sqrt(2)  # Peak voltage

# Voltage source
def v_source(t):
    return V_peak * np.sin(omega * t)

# Differential equations
# y = [i1, di1/dt, i2, di2/dt, v_c1, v_c2]
def rlc_3rd_order(t, y):
    i1, di1, i2, di2, v_c1, v_c2 = y

    # First loop: R1-L1-C1
    d2i1 = (v_source(t) - R1 * di1 - v_c1) / L1
    dv_c1 = di1 / C1

    # Second loop: R2-L2-C2, driven by v_c1
    d2i2 = (v_c1 - R2 * di2 - v_c2) / L2
    dv_c2 = di2 / C2

    return [di1, d2i1, di2, d2i2, dv_c1, dv_c2]

# Initial conditions
y0 = [0, 0, 0, 0, 0, 0]

# Time domain (2 cycles)
t_span = (0, 0.02)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the system
sol = solve_ivp(rlc_3rd_order, t_span, y0, t_eval=t_eval, method='RK45')

# Extract values
t_ms = sol.t * 1000
i1 = sol.y[0]
i2 = sol.y[2]
v_c1 = sol.y[4]
v_c2 = sol.y[5]
v_in = v_source(sol.t)

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t_ms, v_in, label="Input Voltage (V)", color='orange')
plt.title("Input Voltage (Phase A - 50Hz)")
plt.ylabel("Voltage (V)")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t_ms, v_c1, label="Voltage at C1 (Node 1)", color='blue')
plt.plot(t_ms, v_c2, label="Voltage at C2 (Node 2)", color='green')
plt.title("Voltage across Capacitors (Nodes in Ladder)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t_ms, i1, label="Current i1", color='red')
plt.plot(t_ms, i2, label="Current i2", color='purple')
plt.title("Currents Through Inductors")
plt.xlabel("Time (ms)")
plt.ylabel("Current (A)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("rlc_3rd_order_system.png", dpi=300)
