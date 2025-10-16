
#Importerad metod för Eulers stegmetod 
def euler_method(N0, k, h, t_max):
    """
    Beräknar lösningen till dN/dt = -kN med Eulers metod.

    Parametrar:
        N0: initialt värde (float)
        k: konstant (float)
        h: tidssteg (float)
        t_max: sluttid (float)

    Returnerar:
        t (numpy array): tidssteg
        y (numpy array): uppskattad lösning med Eulers metod
    """
    t = np.arange(0, t_max, h)
    y = np.zeros(len(t))
    y[0] = N0

    for i in range(1, len(t)):
        y[i] = y[i-1] + dx_dt(y[i-1], k) * h

    return t, y



