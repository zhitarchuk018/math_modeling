a = [1,3,5,7,9,11,13,15, 19]


def mean_func(a):
  s = 1
  for i in range(len(a)):
    s = s * a[i]
  return s    
 
tmp = mean_func(a)

print(tmp)
