f = open("kerites.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))

print("2. feladat")

print(f"Az eladott telkek száma: {len(l)}")

print("3. feladat")

c = 0

if l[-1][0] == "0":
    print("A páros oldalon adták el az utolsó telket.")
    for i in l:
        if i[0] == "0":
            c += 1

    c = c*2
    print(f"Az utolsó telek házszáma: {c}")

elif l[-1][0] == "1":
    c = 0
    print("A páratlan oldalon adták el az utolsó telket.")
    for i in l:
        if i[0] == "1":
            c += 1

    print(f"Az utolsó telek házszáma: {c}")


print("4. feladat")

paratlan = []

for i in l:
    if i[0] == "1":
        paratlan.append(i)

c = 1

for i in range(len(paratlan)):
    if paratlan[i][-1] == paratlan[i+1][-1] and paratlan[i][-1] != ":" and paratlan[i][-1] != "#":
        break

    c += 2

print(f"A szomszédossal egyezik a kerités színe: {c}")

print("5. feladat")

hazszam = int(input("Adjon meg egy házszámot! "))

d = 0

paros = []
c = 0

for i in l:
    if i[0] == "0":
        paros.append(i)

if hazszam % 2 == 0:
    for i in paros:
        c += 2
        if c == hazszam:
            print(f"A kerités színe / állapota: {i[-1]}")

if hazszam % 2 != 0:
    c = 0
    for i in paratlan:
        d += 1
        if c == 0:
            c += 1

        elif c != 0:
            c += 2

        if c == hazszam:
            print(f"A kerités színe / állapota: {i[-1]}")
            break


abc = ["A","B","C","D","E","F","G"]

for i in abc:
    if paratlan[d-2][-1] != i and paratlan[d-1][-1] != i and paratlan[d][-1] != i:
        print(f"Egy lehetséges festési szin: {i}")
        break

osszes = ""
szamos = ""
c = 0



for i in paratlan:
    if c == 0:
        c += 1

    elif c != 0:
        c += 2

    szamos += str(c)

    for j in range(int(i[1])):
        osszes += i[-1]
    
    if c < 10:
        for k in range(int(i[1])-1):
            szamos += " "
    elif c > 10:
        for k in range(int(i[1])-2):
            szamos += " "

with open("utcakep.txt","w") as utcakep:
    utcakep.write(osszes)
    utcakep.write("\n")
    utcakep.write(szamos)

