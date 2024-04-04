fajl = input("Adja meg a bemeneti fájl nevét! ")
s = int(input("Adja meg egy sor számát! "))
o = int(input("Adja meg egy oszlop számát! "))
kis = []
count = 0
z = 0


f = open(fajl)
l = []
sor = []

for i in f:
    l.append(i.strip().split(" "))


for i in l:
    z += 1
    if z > 9:
        kis.append(i)


del l[-4:]

print(l)

print("3. feladat")

print("a,")

z = 0

for i in range(len(l)):
    if i == s:
        for j in l:
            z += 1
            if z == i:
                for p in j:
                    sor.append(p)

z = 0

for i in range(len(sor)):
    if i == o:
        for j in sor:
            z += 1
            if z == i:
                if j != '0':
                    print(f"Az adott helyen szereplő szám: {j}")
                elif j == '0':
                    print("Az adott helyet még nem töltötték ki.")



for i in l:
    for j in i:
        if j == '0':
            count += 1

print("b,")

atlag = count/81*100

atlag = round(atlag, 1)


print("4. feladat")

print(f"Az üres helyek aránya: {atlag} %")

#ezeket a résztáblákat nagyon kiakartam találni hogy tudnám de a for lupaim nem sehogy se mukodtek:/
