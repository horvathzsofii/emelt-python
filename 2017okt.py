f = open("naplo.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))

l2 = []
sz = ""
l3 = []

for i in l:
    for j in i:
        if j == "#":
            l2.append(l3)
            l3 = []
        l3.append(j)



print("2. feladat")

sz = 0

for i in l:
    if i[0] != "#":
        sz += 1

print(f"A naplóban {sz} bejegyzés van.")

print("3. feladat")

igazolt = 0
igazolatlan = 0

for i in l:
    if i[0] != "#":
        for j in i[2]:
            if j == "X":
                igazolt += 1
            elif j == "I":
                igazolatlan += 1


print(f"Az igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra.")

print("5. feladat")

def hetnapja(honap,nap):
    napnev = ["vasarnap","hetfo","kedd", "szerda", "csutortok",
 "pentek", "szombat"]
    napok = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napok[honap-1]+nap) % 7
    hetnapja = napnev[napsorszam]
    return hetnapja


honap = int(input("A hónap sorszáma="))
nap = int(input("A nap sorszáma="))

print(f"Azon a napon {hetnapja(honap,nap)} volt.")


print("6. feladat")

napppp = input("A nap neve=")
ora = int(input("Az óra sorszáma="))

sz = 0
s =  0
z = 0
p = 0

l2.pop(0)


print(l)

for i in l2:
    if hetnapja(int(i[1]),int(i[2])) == napppp:
        for j in i:
            sz += 1
            if sz == 6 or (sz > 6 and sz % 3 == 0):
                for k in j:
                    s += 1
                    if s == ora:
                        if k == "X" or k == "I":
                            z += 1
                s = 0
sz = 0


print(f"Ekkor összesen {z} óra hiányzás történt.")


print("7. feladat")

sz = 0
l4 = []
l5 = []

for i in l:
    if i[0] != "#":
        l4.append(i[0])
        l4.append(i[1])

    l5.append(l4)
    l4 = []

l6 = []

for i in l5:
    if i != []:
        l6.append(i)


l7 = []
for i in l6:
    if i not in l7:
        l7.append(i)


tanulok = []
maxtanulok = []
sz = 0

for i in l7:
    for j in l:
        if j[0] == i[0]:
            if j[0] != "#":
                for k in j[2]:
                    if k == "X" or k == "I":
                        sz += 1

    tanulok.append(sz)
    sz = 0

m = max(tanulok)

for i in l7:
    for j in l:
        if j[0] == i[0]:
            if j[0] != "#":
                for k in j[2]:
                    if k == "X" or k == "I":
                        sz += 1

    if sz == m:
        maxtanulok.append(i)

    sz = 0

sz = ""

for i in maxtanulok:
    sz += i[0] + " " + i[1] + " "


print(f"A legtöbbet hiányzó tanulók: {sz}")

