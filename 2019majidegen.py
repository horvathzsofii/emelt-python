f = open("beosztas.txt")
l = []
l2 = []

for i in f:
    l2.append(i.strip().split(" "))
    if len(l2) == 4:
        l.append(l2)
        l2 = []

print("2. feladat")

print(f"A fájlban {len(l)} bejegyzés van.")

print("3. feladat")

c = 0

for i in l:
    c += int(i[-1][0])

print(f"Az iskolában a heti összóraszám: {c}")

print("4. feladat")

tanar = input("A tanár neve= ")

c = 0
t = ""

for i in l:
    t = i[0][0] + " " + i[0][1]
    if t == tanar:
        c += int(i[-1][0])

print(f"A tanár heti óraszáma: {c}")


tanarok = []
t = ""

with open("of.txt","w") as of:
    for i in l:
        if i[1][0] == "osztalyfonoki":
            t = i[0][0] + " " + i[0][1]
            tanarok.append([t,i[2][0]])


    for i in tanarok:
        of.write(f"{i[1]} - {i[0]}\n")


print("6. feladat")

osztaly = input("Osztály= ")
tantargy = input("Tantárgy= ")
c = 0

for i in l:
    if i[1][0] == tantargy and osztaly == i[2][0]:
        c += 1

if c == 1:
    print("Osztályszinten tanulják.")

if c > 1:
    print("Csoportbontásban tanulják.")
        

print("7. feladat")

tanarok = []

for i in l:
    if i[0] not in tanarok:
        tanarok.append(i[0])

print(f"Az iskolában {len(tanarok)} tanár tanít.")