import numpy as np

def f(x):
  return x**2 - 4

akar = np.roots

print ("Akar-Akar dari f(x) = x^2-4 adalah", akar)

import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return x**2 - 4

akar = np.roots([1, 0, -4])

x = np.linspace(-3, 3, 400)
y = f(x)

plt.figure(figsize=(8,5))
plt.plot(x,y, label = '$f(x) = x^2-4$', color='blue')
plt.title("Grafik Fungsi Kuadrat")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
