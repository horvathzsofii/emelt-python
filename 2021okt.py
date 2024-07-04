print("1. feladat")

fajl = input("Adja meg a bemeneti fájl nevét! ")
sor = int(input("Adja meg egy sor számát! "))
oszlop = int(input("Adja meg egy oszlop számát! "))

f = open(fajl)
l = []

for i in f:
    l.append(i.strip().split(" "))

print("3. feladat")

szam = l[sor-1][oszlop-1]

print(f"Az adott helyen szereplő szám: {szam}")

c = 0

i = sor-1
j = oszlop-1

if i <= 2 and j <= 2:
    c = 1
elif i <= 2 and (j > 2 and j <=5):
    c = 2
elif i <= 2 and (j > 5):
    c = 3

elif (i > 2 and i <= 5) and j <= 2:
    c = 4
elif (i > 2 and i <= 5)  and (j > 2 and j <=5):
    c = 5
elif (i > 2 and i <= 5)  and (j > 5):
    c = 6

elif i > 5 and j <= 2:
    c = 7
elif i > 5  and (j > 2 and j <=5):
    c = 8
elif i > 5  and (j > 5):
    c = 9

print(f"A hely a(z) {c} résztáblához tartozik.")

print("4. feladat")

k = 0

for i in l:
    for j in i:
        if j == "0":
            k += 1

k = round((k/81*100),1)

print(f"Az üres helyek aránya: {k}%")

print("5. feladat")

for p in l:
    if len(p) != 9:
        szam = int(p[0])
        sor = int(p[1])
        oszlop = int(p[2])
        a = 0
        b = 0
        c = 0
        d = 0
        jo = True
        print(f"A kiválasztott sor: {sor} oszlop: {oszlop} a szám: {szam}")

        if l[sor-1][oszlop-1] != "0":
            a = 1
            jo = False


        if szam in l[sor-1]:
            b = 1
            jo = False


        for d in l:
            if len(d) == 9:
                if d[oszlop-1] == str(szam):
                    c = 1
                    jo = False


        i = sor - 1
        j = oszlop - 1

        if i <= 2 and j <= 2:
            for b in range(0,2):
                for n in range(0,3):
                    if l[b][n] == str(szam):
                        d = 1
                        jo = False
        elif i <= 2 and (j > 2 and j <= 5):
            for b in range(0,2):
                for n in range(3,6):
                    if l[b][n] == str(szam):
                        d = 1
                        jo = False
        elif i <= 2 and (j > 5):
            for b in range(0,2):
                for n in range(6,9):
                    if l[b][n] == str(szam):
                        d = 1
                        jo = False
        elif (i > 2 and i <= 5) and j <= 2:
            for b in range(3,6):
                for n in range(0,3):
                    if l[b][n] == str(szam):
                        d = 1
                        jo = False
        elif (i > 2 and i <= 5) and (j > 2 and j <= 5):
            for b in range(3,6):
                for n in range(3,6):
                    if l[b][n] == str(szam):
                        d = 1
                        jo = False
        elif (i > 2 and i <= 5) and (j > 5):
            for b in range(3,6):
                for n in range(6,9):
                    if l[b][n] == str(szam):
                        d = 1
                        jo = False

        elif i > 5 and j <= 2:
            for b in range(6,9):
                for n in range(0,2):
                    if l[b][n] == str(szam):
                        d = 1
                        jo = False
        elif i > 5 and (j > 2 and j <= 5):
            for b in range(6,9):
                for n in range(3,6):
                    if l[b][n] == str(szam):
                        d = 1
                        jo = False
        elif i > 5 and (j > 5):
            for b in range(6,9):
                for n in range(6,9):
                    if l[b][n] == str(szam):
                        d = 1
                        jo = False

        if jo == True:
            print("A lépés megtehető.")

        elif a == 1:
            print("A helyet már kitöltötték.")
        elif b == 1:
            print("Az adott sorban már szerepel a szám.")
        elif c == 1:
            print("Az adott oszlopban szerepel a szám.")
        elif d == 1:
            print("Az adott résztáblában már szerepel a szám.")