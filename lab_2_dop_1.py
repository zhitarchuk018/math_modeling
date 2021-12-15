b = float(input('введите коэффицент a: '))
c = float(input('введите коэффицент b: '))
d = float(input('введите коэффицент с: '))

a = f'{b}*x**2 + {c}*x + {d}'

q = c**2 - 4*b*d
e = (- c + q**0.5)/2*b
r = (- c - q**0.5)/(2*b)
t = - c / (2 * b)
if q > 0:
  print(f'x1 = {e} x2 = {r}')
elif q == 0:
  print(f'x = {t}')
else:
  print('нет решений')

