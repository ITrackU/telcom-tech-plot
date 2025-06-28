import numpy as np
import matplotlib.pyplot as plt

# Paramètres du circuit
V0 = 12            # Tension d'alimentation (Volts)
R = 1e3            # Résistance en ohms (1 kΩ)
C = 100e-6         # Capacité en farads (100 µF)
tau = R * C        # Constante de temps en secondes

# Temps de simulation (jusqu’à 5 constantes de temps)
t = np.linspace(0, 5 * tau, 1000)
vc = V0 * (1 - np.exp(-t / tau))  # Tension aux bornes du condensateur

# Affichage
plt.figure(figsize=(8, 4))
plt.plot(t * 1000, vc, label='Tension sur le condensateur', color='blue')
plt.axhline(V0, color='gray', linestyle='--', label='Tension finale')
plt.title("Charge d’un condensateur dans un circuit RC")
plt.xlabel("Temps (ms)")
plt.ylabel("Tension (V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("charge_RC.png", dpi=300)
