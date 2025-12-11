# Starta programmet

import numpy as np
import matplotlib.pyplot as plt

#------------------------------
# Konstanter och simuleringens parametrar
#------------------------------

G = 6.67e-11              # Gravitationskonstant
h = 0.01               # Tidssteg
t_max = 1             # Total simuleringstid
steg = int(t_max / h) # Antal steg

#------------------------------
# Funktion: total gravitationskraft på partikel i
#------------------------------

def total_gravitationskraft(i, Positioner, Massor):
    kraft = np.zeros(2)
    for j in range(len(Massor)):
        if i != j:
            diff = Positioner[j] - Positioner[i]
            dist = np.linalg.norm(diff)
            if dist > 1e-10:
                kraft += G * Massor[i] * Massor[j] * diff / dist**3 #Newtons gravitationslag
    return kraft

#------------------------------
# Initiera partiklar
#------------------------------

N = 10
Massor = np.random.uniform(1, 10, size=N)  * 10e7     # Massor
Positioner = np.random.uniform(-1, 1, size=(N, 2))    # Startpositioner
Hastigheter = np.zeros((N, 2))                        # Börjar stillastående

# Spara startpositioner
Positions_historik = np.zeros((steg + 1, N, 2))
Positions_historik[0] = Positioner

#------------------------------
# LEAPFROG-INTEGRATION
#------------------------------

# 1. Beräkna initial acceleration
acc = np.zeros((N, 2))
for i in range(N):
    acc[i] = total_gravitationskraft(i, Positioner, Massor) / Massor[i]

# 2. Ta första halvsteget i hastighet
Hastigheter += 0.5 * h * acc

#--- Huvudloopen ---
for tid in range(steg):

    # 3. Uppdatera positioner (helt steg)
    Positioner += h * Hastigheter

    # 4. Beräkna acceleration vid ny position
    acc_new = np.zeros((N, 2))
    for i in range(N):
        acc_new[i] = total_gravitationskraft(i, Positioner, Massor) / Massor[i]

    # 5. Avsluta hastighetssteget (halv steg)
    Hastigheter += 0.5 * h * acc_new

    # Spara positioner
    Positions_historik[tid + 1] = Positioner

    # Byt acceleration
    acc = acc_new

#------------------------------
# Plotta partiklarnas banor
#------------------------------

plt.figure(figsize=(12, 8))

for i in range(N):
    start_x = f"{Positions_historik[0, i, 0]:.2f}"
    start_y = f"{Positions_historik[0, i, 1]:.2f}"

    plt.plot(
        Positions_historik[:, i, 0],
        Positions_historik[:, i, 1],
        label=f"P{i+1}: m={Massor[i]:.2f}, start=({start_x},{start_y})"
    )

plt.title("Partiklarnas banor i 2D (Leapfrog)")
plt.xlabel("x-position")
plt.ylabel("y-position")
plt.grid(True)
plt.legend()
plt.show()
