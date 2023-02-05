Alphabets = ['a', 'b', 'c','d','e']
print(Alphabets[1:3])

print(Alphabets[:4])

print(Alphabets[1:])

print(Alphabets[:])

Alphabets.append('f')
print(Alphabets)

Alphabets.insert(4,'d1')
print(Alphabets)

Alphabets1 = ['f','g','h']
Alphabets.extend(Alphabets1)
print(Alphabets)

Alphabets.append(Alphabets1)
print(Alphabets)
print(Alphabets.pop())
print(Alphabets.pop(2))
