f = open("szallit.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))

elso = l.pop(0)

hossza = elso[0]

ido = elso[1]

print("2. feladat")

adatsor = int(input("Adja meg, melyik adatsorra kiváncsi! "))

c = 0

ind = l[adatsor-1][1]
veg = l[adatsor-1][2]

print(f"Honnan: {ind} Hova: {veg}")

def tav(szalaghossz, indulashelye, erkezeshelye):
    c = 0
    if indulashelye < erkezeshelye:
        c = erkezeshelye - indulashelye

    elif indulashelye > erkezeshelye:
        c = (szalaghossz - indulashelye) + erkezeshelye


    return c

print("4. feladat")

szallitasok = []

for i in l:
    szallitasok.append(tav(int(hossza),int(i[1]),int(i[2])))

m = max(szallitasok)

print(f"A legnagyobb távolság: {m}")

c = 0
osszes = ""
for i in l:
    c += 1
    if tav(int(hossza),int(i[1]),int(i[2])) == m:
        osszes += str(c) + " "

uts = len(osszes) - 1

print(f"A maximális távolságú szállítások sorszáma: {osszes[:uts]}")

print("5. feladat")

tomeg = 0

for i in l:
    if (int(i[1]) > int(i[2])) and i[1] != "0" and i[2] != "0":
        tomeg += int(i[-1])


print(f"A kezdőpont előtt elhaladó rekeszek össztömege: {tomeg}")

print("6. feladat")

idopont = int(input("Adja meg a kívánt időpontot! "))

rekeszek = ""
c = 0

for i in l:
    c += 1
    if (int(i[0]) + (tav(int(hossza),int(i[1]),int(i[2]))*int(ido))) > idopont and idopont > int(i[0]):
        rekeszek += str(c) + " "

utso = len(rekeszek) -1

if rekeszek != "":
    print(f"A szállított rekeszek halmaza: {rekeszek[:utso]}")

else:
    print("A szállított rekeszek halmaza: üres")


with open("tomeg.txt","w") as tomeggg:
    c = 0
    t = 0
    for i in range(int(hossza)+1):
        for j in l:
            if int(j[1]) == i:
                t += int(j[-1])


        if t != 0:
            tomeggg.write(f"{i} {t}\n")
            t = 0