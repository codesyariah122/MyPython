print('Ha'*5)
print([1, 2] * 5)
print(1, 2 * 5)

a = range(12)

print(a[::2])
print(a[::-1])

a = [6, 3, 2, 5, 4, 1]
a.sort()
print(a)

print({'kuadrat_'+str(x): x**2 for x in range(5)})

a = 5
b = 7

print('Sebelum: a = '+str(a)+', b = '+str(b))
a, b = b, a
print('Sesudah: a = '+str(a)+', b = '+str(b)) 