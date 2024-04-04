f = open("melyseg.txt")
l = []
count = 0
count1 = 0
szaml = []
count2 = 0
szaraz = 0
vizes = 0
count3 = 0
darabl = []

for i in f:
    l.append(i.strip().split(" "))

print(l)

print("1. feladat")

for i in l:
    count += 1

print(f"A fájl adatainak száma: {count}")

print("2. fealdat")

sor = int(input("Adjon meg egy távolságértéket! "))


for i in l:
    count2 += 1
    if count2 == sor:
        m = i[0]

print(f"Ezen a helyen a felszin {m} méter mélyen van")

for i in l:
    if i[0] == '0':
        szaraz += 1
    elif i[0] != '0':
        vizes += 1


erintetlen = szaraz/vizes*100

print("3. feladat")

print(f"Az érintetlen felület aránya {erintetlen}")

print("5. feladat")


for i in l:
    count3 += 1
    darab = i*count3
    darabl.append(darab)


print(darabl)

#ezt az egesz feladatot turelmem se volt ertelmezni