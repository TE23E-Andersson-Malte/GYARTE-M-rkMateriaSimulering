#Starta programmet

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

#Initiera antal partiklar, massor, positioner och hastigheter
#Sätt gravitationskonstanten G och tidssteget h
#För varje tidssteg tills simuleringstiden är slut:
    #För varje partikel:
        #Beräkna den totala gravitationskraften från alla andra partiklar
        #Beräkna acceleration = kraft / massa
        #Uppdatera hastighet med Eulers metod
        #Uppdatera position med Eulers metod
    #Spara positioner och energivärden för analys
#Rita partiklarna och deras banor
#Analysera hur resultatet påverkas av antal partiklar, massa och hastighet
#Avsluta programmet

#_______________________
#________METODER________
#_______________________

#Importerad metod för Eulers stegmetod 

# Define parameters
f = lambda t, s: np.exp(-t) # ODE
h = 0.1 # Step size
t = np.arange(0, 1 + h, h) # Numerical grid
s0 = -1 # Initial Condition

# Explicit Euler Method
s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h*f(t[i], s[i])

plt.figure(figsize = (12, 8))
plt.plot(t, s, 'bo--', label='Approximate')
plt.plot(t, -np.exp(-t), 'g', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()