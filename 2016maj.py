f = open("penztar.txt")
l0 = []
l1 = []
l = []

for i in f:
    l0.append(i.strip().split(" "))

for i in l0:
    for j in i:
        if j != "F" and j != "ceruza":
            if j == "HB":
                l1.append("HB ceruza")
            elif j != "HB":
                l1.append(j)

        elif j == "F":
            l.append(l1)

            l1 = []



print("2. feladat")
print(f"A fizetések száma: {len(l)}")

print("3. feladat")
print(f"Az első vásárló {len(l[0])} darab árucikket vásárolt.")

print("4. feladat")
sorszam = input("Adja meg egy vásárlás sorszámát! ")
arucikk = input("Adj meg egy árucikk nevét! ")
darabszam = input("Adja meg a vásárolt darabszámot! ")

print("5. feladat")

sz = 0
s = 0

for i in l:
    sz += 1
    for j in i:
        if j == arucikk:
            s = 1

    if s == 1:
        break

print(f"Az első vásárlás sorszáma: {sz}")

sz = 0
s = 0
megjelenes = []
for i in l:
    s += 1
    for j in i:
        if j == arucikk:
            megjelenes.append(s)

print(f"Az utolsó vásárlás sorszáma: {megjelenes[-1]}")

sz = 0
s = 0

for i in l:
    for j in i:
        if j == arucikk:
            sz += 1


    if sz >= 1:
        s += 1
        sz = 0

print(f"{s} vásárlás során vettek belőle.")

print("6. feladat")

def ertek(darabszamm):
    if darabszamm == 1:
        ara = 500

    elif darabszamm == 2:
        ara = 500 + 450

    elif darabszamm == 3:
        ara = 500 + 450 + 400

    elif darabszamm > 3:
        ara = 500 + 450 + (darabszamm-2)*400

    return ara

print(f"{darabszam} darab vételekor fizetendő: {ertek(int(darabszam))}")

print("7. feladat")

targyak = []

for i in l:
    sz += 1
    if sz == int(sorszam):
        for j in i:
            targyak.append(j)

sz = 0
aruk = []
for i in targyak:
    for j in targyak:
        if i == j:
            sz += 1
    aruk.append(str(sz) + " " + i)

    sz = 0

arukveglegesmostmar = []
for i in aruk:
    if i not in arukveglegesmostmar:
        arukveglegesmostmar.append(i)


for i in arukveglegesmostmar:
    print(i)

sz = 0
s = 0
ossz = 0
szamos = []
vegleges = []

with open("osszeg.txt","w") as osszeg:
    targyak = []
    for i in l:
        s += 1
        for j in i:
            for k in i:
                if k == j:
                    sz += 1

            if [sz,j] not in szamos:
                szamos.append([sz,j])
                sz = 0
            else:
                sz = 0

        for z in szamos:
            ossz += ertek(z[0])

        osszeg.write(f"{s}: {ossz}\n")
        ossz = 0
        szamos = []
