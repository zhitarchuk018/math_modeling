a = int(input('Введите год:'))

if a % 4 == 0  and a % 400 == 0  or a % 100 != 0:
  print(f"{a} - високосный год")

else:
  print(f"{a} - невисокосный год")
