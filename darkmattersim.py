#Starta programmet

import numpy as np
import matplotlib.pyplot as plt

#plt.style.use('seaborn-poster')

#Sätt gravitationskonstanten G och tidssteget h samt andra konstanter som behövs för Eulers stegmetod
# Define parameters (importerade med Eulers stegmetod)
f = lambda t, s: np.exp(-t) # ODE
h = 0.1 # Step size
t = np.arange(0, 1 + h, h) # Numerical grid
s0 = -1 # Initial Condition

G = 1e-3 #6.674e-11 
t_max = 5  # total simuleringstid
steg = int(t_max / h)


#_______________________
#________METODER________
#_______________________

#Importerad metod för Eulers stegmetod 

# Explicit Euler Method
def euler(s0, f, h):
    t = np.arange(0, t_max + h, h)  # tidsgrid
    s = np.zeros(len(t))
    s[0] = s0

    for i in range(0, len(t) - 1):
        s[i + 1] = s[i] + h*f(t[i], s[i])

    return t,s

def total_gravitationskraft(i, Positioner, Massor):
    kraft = np.zeros(2)
    for j in range(len(Massor)):
        if i != j:
            diff = Positioner[j] - Positioner[i]
            dist = np.linalg.norm(diff)
            if dist > 1e-5:  # undvik division med 0
                kraft += G * Massor[i] * Massor[j] * diff / dist**3
    return kraft

#_______________________
#______Programmet_______
#_______________________

#Initiera antal partiklar, massor, positioner och hastigheter
N = 10 #Antal partiklar
Massor = np.random.uniform(1, 10, size=N) #Skapar array med partiklarnas massor (slumpad mellan 1 och 10)
Positioner = np.random.uniform(-1, 1, size=(N,2)) #Skapar array med partiklarnas slumpade positioner (x, y) för N partiklar
Hastigheter = np.zeros((N, 2)) #Skapar array med partiklarnas hastigheter (alla är 0)

#Spara positioner för analys
Positions_historik = np.zeros((steg+1, N, 2))
Positions_historik[0] = Positioner

#För varje tidssteg tills simuleringstiden är slut:
    #För varje partikel:
for tid in range(steg):
    for i in range(N):
        #Beräkna den totala gravitationskraften från alla andra partiklar
        a = total_gravitationskraft(i, Positioner, Massor) / Massor[i]

        # Uppdatera hastighet med Eulers metod
        Hastigheter[i] = Hastigheter[i] + a * h

        # Uppdatera position med Eulers metod
        Positioner[i] = Positioner[i] + Hastigheter[i] * h

    # Spara positioner
    Positions_historik[tid + 1] = Positioner
    
#Rita partiklarna och deras banor
plt.figure(figsize=(12, 8))
for i in range(N):
    start_x = f"{Positions_historik[0, i, 0]:.2f}"
    start_y = f"{Positions_historik[0, i, 1]:.2f}"
    
    plt.plot(
        Positions_historik[:, i, 0],
        Positions_historik[:, i, 1],
        label=f'Partikel {i+1}: Massa = {Massor[i]:.2f}, Start = ({start_x}, {start_y})'
    )
plt.title('Partiklarnas banor i 2D')
plt.xlabel('x-position')
plt.ylabel('y-position')
plt.grid(True)
plt.legend()
plt.show()
#Avsluta programmet

