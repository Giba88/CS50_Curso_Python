def Array(x):
    s = set()
    s.add(1)
    s.add(2)
    s.add(3)
    return s    

name = input()
print(f"hello, {name}!")

x = 3

if x > 0:
    print("x é positivo")
elif x < 0:
    print("x é negativo")
else:
    print("x é zero")

for x in range(5):
    print(x)

names = ["Alice", "Bob", "Giba", name]

for name in names:
    print(name)

print(Array(x))

class Clase:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Clase(3, 5)
print(p.x)
print(p.y)
