def changer(a,b):
  a = 2
  b[0] = 'good'
x = 10
l = [1,2]

changer(x,l)

print(x)
print(l)

l = [1,2]
changer(x, l[:])

print(l)

x = 3
y = 4

z = complex(x,y)
print(z)

w = complex(y,x)
print(z + w)

s = 'hello'
print(s[0])

#s[0] = 'H'

t = (1, 4, 9)
print(t)
print(t[0])
#t[0] = 3

l = [1, 4, 9]
l[0] = 3
print(l)

d = {'al':4, 4:'al', 'str':'hello'}
print(d['al'])
print(d[4])
print(d['str'])

d['str'] = 'good'
print(d)
