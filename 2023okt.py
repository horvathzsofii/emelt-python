f1 = open("dobasok.txt")
dobasok = []
osvenyek = []

f2 = open("osvenyek.txt")

for i in f2:
    osvenyek.append(i.strip().split(" "))

for i in f1:
    dobasok.append(i.strip().split(" "))

dobasok = dobasok[0]

print("2. feladat")

print(f"A dobások száma: {len(dobasok)}")
print(f"Az ösvények száma: {len(osvenyek)}")

print("3. feladat")

c1 = 0
c2 = 0
c3 = 0

for i in osvenyek:
    for j in i:
        for k in j:
            c2 += 1
    if c2 > c3:
        c3 = c2

    c2 = 0

for i in osvenyek:
    c1 += 1
    for j in i:
        for k in j:
            c2 += 1
    if c2 == c3:
        break

    c2 = 0

print(f"Az egyik leghosszabb a(z) {c1} ösvény, hossza: {c3}")

print("4. feladat")

osv = int(input("Adja meg egy ösvény sorszámát: "))
jatekosok = int(input("Adja meg a játékosok számát: "))

print("5. feladat")
c = 0

for i in osvenyek:
    c += 1
    if c == 9:
        kilences = i[0]

m = 0
v = 0
e = 0

for i in kilences:
    if i == "M":
        m += 1
    elif i == "V":
        v += 1
    elif i == 'E':
        e += 1

if m != 0:
    print(f"M: {m} darab")

if v != 0:
    print(f"V: {v} darab")

if e != 0:
    print(f"E: {e} darab")

darab = len(kilences)
c = 0

with open("kulonleges.txt", "w") as kulonleges:
    for i in kilences:
        c += 1
        if i == 'V' or i == "E":
            kulonleges.write(f"{c}\t{i}\n")

print("7. feladat")

c = 0
jodobasok = []
for i in dobasok:
    c += 1
    if c > 5:
        c = 1
    jodobasok.append([c,int(i)])

c = 0
szemelyek = []

for i in range(1, jatekosok + 1):
    szemelyek.append(0)

nyertes = 0
darab = int(darab)
m = 0
c = 0
sz = 0

for i in jodobasok:
    if i[0] == 5:
        c += 1

    for j in range(1, jatekosok+1):
        if i[0] == j:
            szemelyek[j-1] += i[1]

            if szemelyek[j-1] >= darab:
                sz = 1

    
    if sz == 1 and i[0] == 5:
        break

m = max(szemelyek)
k = 0

for i in szemelyek:
    k += 1
    if i == m:
        break

print(f"A játék a(z) {c}. körben fejeződött be. A legtábolabb jutó(k) sorszáma: {k}")

print("8. feladat")

szemelyek = []
nyertes = []

for i in range(1,jatekosok + 1):
    szemelyek.append(0)

for i in range(1,jatekosok + 1):
    nyertes.append(0)

sz = 0

for i in jodobasok:
    if i[0] == 5:
        c += 1

    if szemelyek[i[0] - 1] + i[1] >= darab:
        szemelyek[i[0]-1] += i[1]
        if i[0] == 5:
            break

    else:
        if kilences[szemelyek[i[0] - 1] + i[1] - 1] == "M":
            szemelyek[i[0]-1] += i[1]
            print(szemelyek)

        elif kilences[szemelyek[i[0] - 1] + i[1] - 1] == "E":
            szemelyek[i[0]-1] += 2*i[1]

m = max(szemelyek)
nyertesek = ""
c = 0

for i in szemelyek:
    c += 1
    if i == m:
        nyertesek += str(c) + ' '

print(f"Nyertes(ek): {nyertesek}")

print("A többiek pozíciója: ")

sz = 0

for i in szemelyek:
    sz += 1
    if str(sz) not in nyertesek:
        print(f"{sz}. játékos, {i} mező.")