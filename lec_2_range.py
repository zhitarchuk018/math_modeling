a = range(0,10,2)
print(a)
print(type(a))

print(a[3])

a = 'good'
for i in range(0,10,1):       #range-generator
  if i < len(a):              #len-длина   
    print(a[i] + ' - bad')
  else:
    print(f'{i}' + ' - good')
      