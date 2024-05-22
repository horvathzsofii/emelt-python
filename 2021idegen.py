f = open("meresek.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))

for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] = int(l[i][j])

sor = l[0][0]
oszlop = l[1][0]

l.pop(0)
l.pop(0)

print("2. feladat")

sorsz = int(input("A mérés sorának azonosítója="))
oszlopsz = int(input("A mérés oszlopának azonosítója="))

c = 0
c2 = 0

j = l[sorsz-1][oszlopsz-1]

print(f"A mért mélység az adott helyen {j} dm")

print("3. feladat")

nagyl = []

for i in l:
    for j in i:
        nagyl.append(j)

sz = nagyl.count(0)
sz2 = len(nagyl) - sz
atlag = round(sum(nagyl)/sz2/10,2)

print(f"A tó felszíne: {sz2} m2, átlagos mélysége: {atlag} m")

print("4. feladat")

m = max(nagyl)
koord = []

for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == m:
            koord.append(f"({i+1}; {j+1})")

k = " ".join(koord)

print(f"A tó legnagyobb mélysée: {m} m")
print(f"A legmélyebb helyek sor-oszlop koordinátái:")
print(k)

c = 0

for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] != 0:
            if l[i-1][j] == 0:
                c += 1
            if l[i+1][j] == 0:
                c += 1
              
            if l[i][j-1] == 0 and l[i][j+1] == 0:
                c += 2
            elif l[i][j-1] == 0 or l[i][j+1] == 0:
                c += 1     
print(c)

oszlopppp = int(input("A vizsgált szelvény oszlopának azonosítója="))

with open("diagram.txt","w") as diagram:
    csillag = ""
    for i in range(len(l)):
        db = (l[i][oszlopppp-1])/10
        for k in range(round(db)):
            csillag += "*"

        if i < 10:
            diagram.write(f"0{i+1} {csillag}\n")
        else:
            diagram.write(f"{i+1} {csillag}\n")
        csillag = ""