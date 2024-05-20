f = open("kep.txt")
l = []
l2 = []
l3 = []
l4 = []
l5 = []

for i in f:
    l.append(i.strip().split(" "))

for i in range(len(l)):
    for j in l[i]:
        l2.append(int(j))
        if len(l2) == 3:
            l3.append(l2)
            l2 = []

print("2. feladat")
print("Kérem egy képpont adatait!")

sor = int(input("Sor:"))
oszlop = int(input("Oszlop:"))

c = 0
c2 = 0

for i in l3:
    l4.append(i)
    if len(l4) == 640:
        l5.append(l4)
        l4 = []

for i in l5:
    c += 1
    if c == sor:
        for j in i:
            c2 += 1
            if c2 == (oszlop):
                print(f"A képpont színe RGB({j[0]},{j[1]},{j[2]})")


print("3. feladat")

c = 0

for i in l5:
    for j in i:
        if int(j[0]) + int(j[1]) + int(j[2]) > 600:
            c += 1

print(f"A világos képpontok száma: {c}")

print("4. feladat")

kisebb = 0

for i in l5:
    for j in i:
        if kisebb == 0:
            kisebb = int(j[0]) + int(j[1]) + int(j[2])

        elif kisebb != 0:
            if int(j[0]) + int(j[1]) + int(j[2]) < kisebb:
                kisebb = int(j[0]) + int(j[1]) + int(j[2])


print(f"A legsötétebb pont RGB összege: {kisebb}")

sotet = []

for i in l5:
    for j in i:
        if int(j[0]) + int(j[1]) + int(j[2]) == kisebb:
            sotet.append(f"RGB({j[0]},{j[1]},{j[2]})")


print("A legsötéttebb pixelek színe:")
for i in sotet:
    print(i)



def hatar(sor,elteres):
    sz = 0

    for k in range(1,len(l5[sor-1])):
        c2 = (int(l5[sor-1][k][2])) - (int(l5[sor-1][k-1][2]))
        if c2 < 0:
            if (c2*-1) > elteres:
                sz = 1

        elif c2 > 0:
            if c2 > elteres:
                sz = 1


    if sz == 1:
        return True



print('6. feladat')

sorok = []

for i in range(1,361):
    if hatar(i,10):
        sorok.append(i)


mi = min(sorok)
ma = max(sorok)

print(mi,ma)

