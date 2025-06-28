import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.signal import square

# Constants
R = 2       # Ohms (realistic moderate damping)
L = 2e-3     # Henries (typical power line inductance)
C = 2e-6     # Farads (typical line-to-ground capacitance)

f = 50                       # Hz
omega = 2 * np.pi * f
#V_rms = 12                  # RMS voltage
V_peak = 12 # Peak voltage V

# Square wave voltage source
def v_source(t):
    return V_peak * square(omega * t)

# Derivative of source voltage (not used here but left for generality)
def dv_dt(t):
    return 0  # Not defined for square wave (discontinuous)

# ODE system: y = [i, di/dt]
# Equation: L*d²i/dt² + R*di/dt + i/C = dv/dt ≈ 0
# So: d²i/dt² = (v(t) - R*di/dt - i/C) / L
def rlc_system(t, y):
    i = y[0]
    di_dt = y[1]
    d2i_dt2 = (v_source(t) - R * di_dt - i / C) / L
    return [di_dt, d2i_dt2]

# Initial conditions: i(0) = 0 A, di/dt(0) = 0 A/s
y0 = [0, 0]

# Time range: 5 cycles of 50 Hz = 100 ms
t_span = (0, 0.02)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the system
sol = solve_ivp(rlc_system, t_span, y0, t_eval=t_eval, method='RK45')

# Extract results
t_ms = sol.t * 1000         # Time in ms
i = sol.y[0]                # Current
v = v_source(sol.t)         # Input voltage

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t_ms, v, label='Input Voltage (Square)', color='black')
plt.ylabel("Voltage (V)")
plt.title("RLC Response to Square Wave Input")
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t_ms, i, label='Current i(t)', color='blue')
plt.xlabel("Time (ms)")
plt.ylabel("Current (A)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("rlc_square_wave_response.png", dpi=300)
