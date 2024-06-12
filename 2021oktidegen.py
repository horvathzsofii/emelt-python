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

print("4. feladat")

azon = input("Adja meg egy vonat azonosítóját! ")
oraja = input("Adjon meg egy időpontot (óra perc)! ")

print("5. feladat")

elso = 0
masodik = 0

for i in l:
    if i[0] == azon and i[1] == "0":
        elso = (int(i[2])*60) + int(i[3])

    if i[0] == azon:
        masodik = (int(i[2])*60) + int(i[3])

jo = 0
jo = (masodik - elso)

eleg = 2*60 + 22

if jo == eleg:
    print(f"")