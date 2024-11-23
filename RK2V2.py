import numpy as np
import matplotlib.pyplot as plt
import math

def fx_y(x, y):
    return math.exp(-x)-y

def rk2(h, x, y):
    return y + h * fx_y(x + h / 2, y + h * fx_y(x, y) / 2)

# Paramètres
h = 0.01
y0 = float(input('y0 initial : '))  # Valeur initiale

nb_points = 1000
t = np.linspace(0, nb_points, nb_points)
x = np.linspace(0, h * nb_points, nb_points)

y = np.zeros(nb_points)
solution = np.zeros(nb_points)

# Initialisation
y[0] = y0
solution[0] = y0

# Calcul des valeurs pour chaque point
for i in range(1, nb_points):
    y[i] = rk2(h, x[i - 1], y[i - 1])
    solution[i] = math.exp(-x[i])*(x[i])

# Tracé des courbes
plt.plot(t, y, label="Solution approximée (RK2)", color="blue")
plt.plot(t, solution, label="Solution exacte", color="red")

# Ajout de la légende en haut à droite
plt.legend(loc="upper right")

# Affichage du graphe
plt.xlabel("Temps (t)")
plt.ylabel("y(t)")
plt.title("Comparaison entre solution exacte et approximée")
plt.grid(True)
plt.show()
