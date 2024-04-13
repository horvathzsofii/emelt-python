f = open("valaszok.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))


helyes = l[0]

l.pop(0)

print("1. feladat: Az adatok beolvasása")

print(f"2. feladat: A vetélkedőn {len(l)} versenyző indult.")

azon = input(f"3. feladat: A versenyző azonosítója = ")

for i in l:
    if i[0] == azon:
        valasz = i[1]
        print(f"{i[1]} (a versenyző válasza)")

print("4. feladat: ")

for i in helyes:
    print(f"{i} (a helyes megoldás)")
    helyess = i


ell = ""

for i in range(len(helyess)):
    if valasz[i] == helyess[i]:
        ell += "+"
    elif valasz[i] != helyess[i]:
        ell += " "


print(f"{ell} (a versenyző helyes válaszai")

sorszam = int(input("5. feladat: A feladat sorszáma = "))

sz = 0

for i in l:
    if i[1][sorszam - 1] == helyess[sorszam - 1]:
        sz += 1

arany = (sz/len(l)*100)
arany = round(arany,2)

print(f"A feladatra {sz} fő, a versenyzők {arany}%-a adott helyes választ.")

print("6. feladat: A versenyzők pontszámának meghatározása.")

sz = 0
s = 0
pontszam = []

for i in l:
    for j in i[1]:
        sz += 1
        if sz <= 5:
            if j == helyess[sz - 1]:
                s = s + 3

        elif sz > 5 and sz <= 10:
            if j == helyess[sz - 1]:
                s = s + 4

        elif sz > 10 and sz <= 13:
            if j == helyess[sz - 1]:
                s = s + 5
                
        elif sz == 14:
            if j == helyess[sz - 1]:
                s = s + 6



    pontszam.append(s)
    s = 0 
    sz = 0

with open("pontok.txt","w") as pontok:
    
    for i in range(len(l)):
        pontok.write(f"{l[i][0]} {pontszam[i]}\n")


print("7. feladat")
pontlista = []

for i in range(len(l)):
    pontlista.append([pontszam[i],l[i][0]])



pontlista = sorted(pontlista)[::-1]

legjobb = []

for i in pontlista:
    legjobb.append(i[0])
    legjobb = list(set(legjobb))
    if len(legjobb) == 3:
        break

legjobb = sorted(legjobb)[::-1]

for i in pontlista:
    if i[0] == legjobb[0]:
        print(f"1. díj ({legjobb[0]} pont): {i[1]}")

for i in pontlista:
    if i[0] == legjobb[1]:
        print(f"2. díj ({legjobb[1]} pont): {i[1]}")


for i in pontlista:
    if i[0] == legjobb[2]:
        print(f"3. díj ({legjobb[2]} pont): {i[1]}")
