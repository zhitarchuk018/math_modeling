import numpy as np 

def mean_func(a):
  x = np.mean(a)
  return x

a = np.array([1,3,5,7,9,11,13,15, 19])

print(mean_func(a))


a = [1,3,5,7,9,11,13,15, 19]


def mean_func(a):
  s = 0
  for i in range(len(a)):
    s = s + a[i]
  return s/len(a)    
 
tmp = mean_func(a)

print(tmp)
