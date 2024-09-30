x = 1
y = 2
print(x+y)

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(x[0:10])
print(x[0:10:2])

def myfunc():
  global z
  z = 1000
myfunc()
print(z)