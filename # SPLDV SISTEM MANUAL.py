# SPLDV SISTEM MANUAL

print('persamaan 1 : ax+by = c')
print('input')
print('masukkan nilai a, b, dan c')
a = float(input('a : '))
b = float(input('b : '))
c = float(input('c : '))

print('persamaan 2 : px+qy = r')
print('input')
print('masukkan nilai p, q, dan r')
p = float(input('p : '))
q = float(input('q : '))
r = float(input('r : '))

x = (c*q-r*b)/(a*q-p*b)
y = (1/b)*(c-a*x)

print("hasil nilai dari x dan y adalah : ")
print("x : ", x)
print("y : ", y)