y0 = 82
vx0 = 92
vy0 = 36

N = 100

coords = np.zeros((N, 3))
t = np.linspace(0, 5, N)
x = x0 + vx0 * t
y = y0 + vy0 * t - 9.8 * t**2 / 2

for j in range(3)
  for i in range(N)
    coords[i, j] = t[i]

print(coords)

