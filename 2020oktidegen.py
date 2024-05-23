f = open("vonat.txt")
l = []

for i in f:
    l.append(i.strip().split("\t"))

print("2. feladat")

allomasok = []
vonatok = []

for i in l:
    if i[0] not in vonatok:
        vonatok.append(i[0])
    if i[1] not in allomasok:
        allomasok.append(i[1])

print(f"Az állomások száma: {len(allomasok)}")
print(f"A vonatok száma: {len(vonatok)}")

print("3. feladat")

nagy = 0
c = 0
szunet = []
c2 = 0

for i in vonatok:
    for j in l:
        if j[0] == i:
            if j[-1] == "E":
                c = (int(j[2])*60) + int(j[3])

            elif j[-1] == "I":
                c2 = (int(j[2])*60) + int(j[3]) - c

            if c2 > nagy:
                nagy = c2

    szunet.append(nagy)
    nagy = 0

szunet.pop(0)
m = max(szunet)
v = ""
meg = ""

for i in vonatok:
    for j in l:
        if j[0] == i:
            if j[-1] == "E":
                c = (int(j[2])*60) + int(j[3])

            elif j[-1] == "I":
                c2 = (int(j[2])*60) + int(j[3]) - c

            if c2 > nagy:
                nagy = c2

            if nagy == int(m):
                v = j[0]
                meg = j[1]

print(f"A(z) {v} vonat a(z) {meg}. állomáson {m} percet állt.")


  