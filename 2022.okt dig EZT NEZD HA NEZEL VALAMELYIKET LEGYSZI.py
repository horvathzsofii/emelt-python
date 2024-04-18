f = open("felajanlas.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))

db = l.pop(0)

for i in db:
    db = i

db = int(db)

print("2. feladat")
print(f"A felajánlások száma: {len(l)}")

print("3. feladat")

sz = 0
egymasmellet = []
for i in l:
    sz += 1
    if int(i[0]) > int(i[1]):
        egymasmellet.append(sz)

egymas = ""
for i in egymasmellet:
    egymas = egymas + str(i) + " "

print(f"A bejárat mindkét oldalán ültetők: {egymas}")

print("4. feladat")

agyas = int(input("Adja meg az ágyás sorszámát! "))

sz = 0
szin = ""
for i in l:
    if agyas >= int(i[0]) and agyas <= int(i[1]):
        sz += 1

    elif int(i[0]) > int(i[1]):
        if agyas >= int(i[0]) and agyas <= (int(i[1]) + db):
            sz += 1

print(f"A felajánlások száma: {sz}")

for i in l:
    if agyas >= int(i[0]) and agyas <= int(i[1]):
        szin = i[2]
        break

    elif int(i[0]) > int(i[1]):
        if agyas >= int(i[0]) and agyas <= (int(i[1]) + db):
            szin = i[2]
            break

if sz != 0:
    print(f"A virágágyások színe, ha csak az első ültet: {szin}")

elif sz == 0:
    print("Ezt az ágyást nem ültetik be.")

szinek = ""
for i in l:
    if agyas >= int(i[0]) and agyas <= int(i[1]):
        if i[2] not in szinek:
            szinek = szinek + i[2] + " "


    elif int(i[0]) > int(i[1]):
        if agyas >= int(i[0]) and agyas <= (int(i[1]) + db):
            if i[2] not in szinek:
                szinek = szinek + i[2] + " "


if sz != 0:
    print(f"A virágágyás színei: {szinek}")


print("5. feladat")

ultetesszam = 0
ultetes = []



for i in l:
    if int(i[0]) < int(i[1]):
        for j in range(int(i[0]),int(i[1]) + 1):
                ultetes.append(j)


    elif int(i[0]) > int(i[1]):
        for j in range(int(i[0]),int(i[1]) + db):
                if j < int(i[1]) + db:
                    ultetes.append(j)

                elif j >= int(i[1]) + db:
                    ultetes.append(j-db)


ultetes1 = list(set(ultetes))
sz = 0
for i in range(db):
    if i not in ultetes1:
        sz += 1

if sz == 0:
    print("Minden ágyás beültetésére van jelentkező.")

c = 0

for i in ultetes:
    c += 1

if c >= db:
    print("Átszervezéssel megoldható a beültetés.")

if c < db:
    print("A beültetés nem oldható meg.")


sz = 0
ultetes2 = []

for i in l:
    sz += 1
    if int(i[0]) < int(i[1]):
        for j in range(int(i[0]),int(i[1]) + 1):
                ultetes2.append([str(j), str(sz), str(i[2])])


    elif int(i[0]) > int(i[1]):
        for j in range(int(i[0]),int(i[1]) + db):
                if j < int(i[1]) + db:
                    ultetes2.append([str(j), str(sz), str(i[2])])

                elif j >= int(i[1]) + db:
                    ultetes2.append([str(j-db), str(sz), str(i[2])])



kiiras = []
"""

for i in range(db):
    for k in ultetes2:
        for j in k:
            if int(j[0]) == i:
                kiiras.append([(j[1]),j[2]])

            elif int(j[0]) != i:
                kiiras.append(["#",0])
"""

with open("szinek.txt","w") as szinek:
    for i in ultetes2:
        if i[0] not in kiiras:
            kiiras.append([i[1],i[2]])


        
    for i in kiiras:
        szinek.write(i)
