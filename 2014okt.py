f1 = open("foglaltsag.txt")
helyek = []
arak = []

for i in f1:
    helyek.append(i.strip().split(" "))

f2 = open("kategoria.txt")

for i in f2:
    arak.append(i.strip().split(" "))


print("2. feladat")

sor = int(input("Adja meg a sor szamat! "))
szek = int(input("Adja meg az oszlop szamat! "))

sz = 0
s = 0
megvett = 0

for i in helyek:
    sz += 1
    if sz == sor:
        for j in i:
            for k in j:
                s += 1
                if s == szek:
                    if k == "x":
                        print(" Ez a hely foglalt.")

                    elif k == "o":
                        print("Ez a hely nem foglalt.")

print("3. feladat")

megvett = 0

for i in range(len(helyek[0][0])):
    for j in helyek:
        if j[0][i] == "x":
            megvett += 1

szazalek = round((megvett/300)*100)

print(f"Az előadásra eddig {megvett} jegyet adtak el, ez a nézőtér {szazalek}%-a. ")

print("4. feladat")

egy = 0
ketto = 0
harom = 0
negy = 0
ot = 0

for i,j in zip(helyek,arak):
    for k,p in zip(i[0],j[0]):
        if k == "x":
            if p == "1":
                egy += 1

            elif p == '2':
                ketto += 1

            elif p == '3':
                harom += 1

            elif p == '4':
                negy += 1

            elif p == "5":
                ot += 1

jegyek = []
jegyek.append([egy,1])
jegyek.append([ketto,2])
jegyek.append([harom,3])
jegyek.append([negy,4])
jegyek.append([ot,5])

m = max(jegyek)
szamu = 0

for i in jegyek:
    if i[0] == m[0]:
        szamu = i[1]

print(f"A legtöbb jegyet a(z) {szamu}. kategóriában értékesítették.")

print("5. feladat")

ossz = egy*500 + ketto*4000 + harom*3000 + negy*2000 + ot*1500

print(f"A színház bevétele {ossz} forint lenne.")

print("6. feladat")

sz = 0
s = 0

for i in helyek:
    for j in i:
        for k in j:
            if k == "o":
                sz += 1

            elif k == "x" and sz == 1:
                s += 1

            elif k == "x" and sz != 1:
                sz = 0


print(f"{s} ilyen hely van.")

print("7. feladat")


with open("szabad.txt","w") as szabad:
    for i,j in zip(helyek,arak):
        for k,p in zip(i[0],j[0]):
            if k == "x":
                szabad.write(k)
            elif k == "o":
                szabad.write(p)


        szabad.write("\n")