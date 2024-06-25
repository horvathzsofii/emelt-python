f = open("lista.txt")
l = []
l2 = []

for i in f:
    l2.append(i.strip())
    if len(l2) == 5:
        l.append(l2)
        l2 = []


print("2. feladat")

c = 0

for i in l:
    if i[0] != "NI":
        c += 1

print(f"A listában {c} db vetitési dátummal rendelkező epizód van.")

print("3. feladat")

c = 0

for i in l:
    if i[-1] == "1":
        c += 1

atlag = c/len(l)*100

atlag = round(atlag,2)

print(f"A listában lévő epizódok {atlag}%-át látta.")

print("4. feladat")

c = 0

for i in l:
    if i[-1] == '1':
        c += int(i[3])

import math

nap = math.floor(c/60/24)

ora = (c - nap*24*60)

ora = math.floor(ora)

perc = c - nap*24*60 - ora*60


print(f"A sorozatnézéssel {nap} nap {ora} óra {perc} perc töltött.")

print("5. feladat")

datum = input("Adjon meg egy dátumot! Dátum= ")

for i in l:
    if i[0] != "NI":
        if i[0] <= datum:
            print(f"{i[2]}\t{i[1]}")



def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p","szo"]
    honapok = [0,3,2,5,0,3,5,1,4,6,2,4]
    if ho < 3:
        ev - 1
    hetnapja = napok[int((ev + ev / 4 - ev / 100 + ev / 400 + honapok[ho-1] + nap) % 7)]

    return hetnapja

print("7. feladat")

hetnap = input("Adja meg a hét napját (például cs)! Nap= ")

sor = []


for i in l:
    if i[0] != "NI":
        if hetnapja(int(i[0][0:4]),int(i[0][5:7]),int(i[0][-2:])) == hetnap:
            sor.append(i[1])

sor = list(set(sor))

for i in sor:
    print(i)

if sor == []:
    print("Az adott napon nem kerül adásba sorozat.")


sorozatok = []

for i in l:
    if i[1] not in sorozatok:
        sorozatok.append(i[1])

c = 0
c2 = 0

vegleges = []

for i in sorozatok:
    for j in l:
        if j[1] == i:
            c += int(j[3])
            c2 += 1

    
    vegleges.append(f"{i} {c} {c2}")
    c = 0
    c2 = 0


with open("summa.txt","w") as summa:
    for i in vegleges:
        summa.write(f"{i}\n")





