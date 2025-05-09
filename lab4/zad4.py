from z3 import *

opt = Optimize()

x = Int('x')
y = Int('y')
z = Int('z')


opt.add(x > y, y > z, z > 0)
# Zakres dla szybszej pracy
opt.add(x < 200, y < 200, z < 200)

expressions = [x - y, x + z, x - z, y + z, y - z]

for i, expr in enumerate(expressions):
    s = Int(f'sq_{i}')
    opt.add(expr == s * s)

opt.minimize(x + y + z)

if opt.check() == sat:
    m = opt.model()
    xv, yv, zv = m[x].as_long(), m[y].as_long(), m[z].as_long()
    print(f"Najmniejsza suma: {xv + yv + zv}")
    print(f"x = {xv}, y = {yv}, z = {zv}")
else:
    print("Brak rozwiązania w danym zakresie.")
