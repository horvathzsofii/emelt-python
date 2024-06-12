f = open("tancrend.txt")
l2 = []
l = []

for i in f:
    l2.append(i.strip().split(" "))
    if len(l2) == 3:
        l.append([l2[0][0],l2[1][0],l2[2][0]])
        l2 = []


print("2. feladat")

print(f"Első: {l[0][0]}, utolsó: {l[-1][0]}")

print("3. feladat")

c = 0

for i in l:
    if i[0] == "samba":
        c += 1

print(f"Ennyi páros mutatta be a sambát: {c}")

print("4. feladat")

c = 0
vilma = []

for i in l:
    if i[1] == "Vilma":
        vilma.append(i[0])

vilma = list(set(vilma))

vlmak = ""

for i in vilma:
    vlmak += i + ", "

print("Az alábbi táncokban szerepelt Vilma: ",vlmak[0:len(vlmak)-2])

print("5. feladat")

tanc = input("Adjon meg egy táncot! ")

c = 0

for i in l:
    if i[0] == tanc and i[1] == "Vilma":
        print(f"A {tanc} bemutatóján Vilma párja {i[-1]} volt.")
        c = 1


if c == 0:
    print(f"Vilma nem táncolt {tanc}-t.")


print("6. feladat")

with open("szereplok.txt","w") as szereplok:
    lanyok = ""
    fiuk = ""

    for i in l:
        if i[1] not in lanyok:
            lanyok += i[1] + ", "

        if i[2] not in fiuk:
            fiuk += i[-1] + ", "


    szereplok.write(f"Lányok: {lanyok[0:len(lanyok)-2]}\n")
    szereplok.write(f"Fiuk: {fiuk[0:len(fiuk)-2]}")


lany = []
fiu = []

for i in l:
    lany.append(i[1])
    fiu.append(i[2])


legtlany = max(lany)

legtobbl = []

legtfiu = max(fiu)

legtobbf = []

c = 0

for i in lany:
    if i == legtlany:
        c += 1

k = 0

for i in range(len(lany)):
    for j in lany:
        if j == lany[i]:
            k += 1


    if k == c:
        legtobbl.append(lany[i])

    k = 0

legtobbl = list(set(legtobbl))

c = 0

for i in fiu:
    if i == legtfiu:
        c += 1

k = 0

for i in range(len(fiu)):
    for j in fiu:
        if j == fiu[i]:
            k += 1


    if k == c:
        legtobbf.append(fiu[i])

    k = 0

legtobbf = list(set(legtobbf))

legtobbl = ", ".join(legtobbl)

legtobbf = ", ".join(legtobbf)

print(f"Legtöbbször szerepelt fiú(k): {legtobbf}")

print(f"Legtöbbször szerepelt lány(ok): {legtobbl}")
