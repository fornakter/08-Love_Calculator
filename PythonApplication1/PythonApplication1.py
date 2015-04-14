#Kalkulator mi³oœci - do skonczenia

a = input("Podaj pierwsze imie:")
b = input("Podaj drugie imie:")

c = 0
for i in range(len(a)):
    c = c + ord(a[i]) 
c = c/10
print("Pierwsze:", c)
d = 0
for i in range(len(b)):
    d = d + ord(b[i])
d = d/10
print("Drugie:", d)
print("1 + 2:", c+d)
e = c+d/(len(a)*len(b))
print(e, "%")

