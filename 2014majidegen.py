f = open("verseny.txt")
l = []

for i in f:
    l.append(i.strip())


elso = l.pop(0)[0]

print("2. feladat")

c = 0
jo = 0
egymasutan = []

for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == "+":
            c += 1
            if c == 2:
                jo = 1
        elif l[i][j] == "-":
            c = 0

    if jo == 1:
        egymasutan.append(str(i+1))

    jo = 0
    c = 0


egymasutan = " ".join(egymasutan)

print(f"Az egymást követően többször találó versenyzők: {egymasutan}")

print("3. feladat")

c = 0
jo = 0
szamolosdi = 0

for i in l:
    szamolosdi += 1
    if len(i) > c:
        c = len(i)
        jo = szamolosdi

print(f"A legtöbb lövést leadó versenyző rajtszáma: {jo}")

def loertek(sor):
    aktpont = 20
    ertek = 0
    for i in range(len(sor)):
        if aktpont > 0 and sor[i] == "-":
            aktpont -= 1

        else:
            ertek += aktpont


    return ertek

print("5. feladat")

rajtszam = int(input("Adjon meg egy rajtszámot! "))

rajt = l[rajtszam-1]

c = 0
szamolo = 0
jok = []
nagyonjok = []

for i in rajt:
    szamolo += 1
    if i == "+":
        jok.append(str(szamolo))

for i in rajt:
    if i == "+":
        c += 1

    elif i == "-":
        nagyonjok.append(c)
        c = 0

pont = loertek(rajt)

k = len(jok)
jok = " ".join(jok)

print(f"5.a feladat: Célt érő lövések: {jok}")
print(f"5b. feladat: Az eltalált korongok száma: {k}")
print(f"5c. feladat: A leghosszab hibátlan sorozat hossza: {max(nagyonjok)}")
print(f"5d. feladat: A versenyző pontszáma: {pont}")

pontok = []
szamolo = 0

for i in l:
    szamolo += 1
    pontok.append([loertek(i),szamolo])

pontok = list(reversed(sorted(pontok)))

szamolo = 0
sorrend = []

for i in range(len(pontok)):
    if pontok[i][0] != pontok[i-1][0]:
        sorrend.append(szamolo+1)
        szamolo += 1

    elif pontok[i][0] == pontok[i-1][0]:
        sorrend.append(szamolo)

with open("sorrend.txt","w") as sorenddd:
    for i in range(len(sorrend)):
        sorenddd.write(f"{sorrend[i]}\t{pontok[i][1]}\t{pontok[i][0]}\n")