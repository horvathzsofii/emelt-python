f = open("ip.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))


print("2. feladat")

print(f"Az állományban {len(l)} adatsor van")

legk = min(l)

print("3. feladat")

print(f"A legalacsonabb tarolt IP-cím:\n{legk[0]}")

print("4. feladat")

dok = 0
glo = 0
hely = 0

for i in l:
    if i[0][0:9] == "2001:0db8":
        dok += 1

    elif i[0][0:7] == "2001:0e":
        glo += 1
    elif i[0][0:2] == "fd" or i[0][0:2] == "fc":
        hely += 1
    
print(f"Dokumentációs cím: {dok} darab")
print(f"Globális egyedi cím: {glo} darab")
print(f"Helyi egyedi cím: {hely} darab")

print("5. feladat")

nulla = 0

with open("sok.txt","w") as sok:
    for i,j in enumerate(l):
        for k in j[0]:
            if k == "0":
                nulla += 1


        if nulla >= 18:
            sok.write(f"{i+1} {j[0]}")
            sok.write("\n")


print("6. feladat")

bek = int(input(f"Kérek egy sorszámot: "))

sor = []

for i,j in enumerate(l):
    if i+1 == bek:
        print(j[0])
        for p in j:
            sor.append(p.split(":"))


negynullak = ""
nullak = 0

sor = sor[0]

for i,j in enumerate(sor):
    if j != "0000":
        if j.startswith('0'):
            sor[i] = j.strip("0")

    
    elif j == "0000":
        sor[i] = "0"


egeszsor = ""
sz = 0

for i in sor:
        sz += 1
        if sz < 8:
            egeszsor = egeszsor + i + ":"

        elif sz == 8:
            egeszsor = egeszsor + i

print(egeszsor)

print("7. feladat")

for i in range(len(sor) - 1):
    if sor[1] and sor[i + 1] == "0":
        sor[i] = ":"
        sor[i + 1] = ":"
        nemjo = 1

if nemjo == 0:
    print("Nem rövidíthető tovább.")

print(sor)

egeszsor = ""
sz = 0
s = 0

for i in sor:
        sz += 1
        if sz < 8 and i != ":":
            egeszsor = egeszsor + i + ":"

        elif sz == 8 and i != ":":
            egeszsor = egeszsor + i

        elif i == ":" and s == 0:
            s += 1
            egeszsor = egeszsor + ":"



print(egeszsor)