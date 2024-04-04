f = open("utasadat.txt")
l = []
datum = []
count = 0
z = 0

for i in f:
    l.append(i.strip().split(" "))

print("2. feladat")

print(f"A buszra {len(l)} utas akart fellszálni.")

print("3. feladat")

for i in l:
    if int(i[4]) == 0:
        count += 1


for i in l:
    if int(i[1][:8]) > int(i[4]) and i[3] != "JGY":
        count += 1


print(f"A buszra {count} utas nem szállhatott fel.")

print("4. feladat")

megallok = []
 
for i in l:
    megallok.append(i[0])

megallok = list(set(megallok))

megallok0 = [int(i) for i in megallok]

megallok1 = sorted(megallok0)

szam = []

for i in megallok1:
    c = 0
    for j in l:
        if int(j[0]) == i:
            c += 1
    
    szam.append(c)

m = max(szam)

print(szam)

sz = -1

for i in szam:
    sz += 1
    if i == m:
        break


print(f"A legtöbb utas ({m} fő) a {sz}. megállóban próbált felszállni.")

print("5. feladat")

kedv = 0
ingy = 0

for i in l:
    if (int(i[1][:8]) <= int(i[4]) and i[3] != "JGY") and int(i[4]) != 0 and (i[3] == "TAB" or i[3] == "NYB"):
        kedv += 1
    elif (int(i[1][:8]) <= int(i[4]) and i[3] != "JGY") and int(i[4]) != 0 and (i[3] == "NYP" or i[3] == "RVS" or i[3] == "GYK"):
        ingy += 1


print(f"Ingyenesen utazók száma: {ingy} fő")
print(f"Kedvezményesen utazók száma: {kedv} fő")

print("6. feladat")

"""def napokszama(e1:egész, h1:egész, n1: egész, e2:egész, h2: egész, n2: egész): egész
	h1 = (h1 + 9) MOD 12
	e1 = e1 - h1 DIV 10
	d1= 365*e1 + e1 DIV 4 - e1 DIV 100 + e1 DIV 400 + (h1*306 + 5) DIV 10 + n1 - 1
	h2 = (h2 + 9) MOD 12
	e2 = e2 - h2 DIV 10
	d2= 365*e2 + e2 DIV 4 - e2 DIV 100 + e2 DIV 400 + (h2*306 + 5) DIV 10 + n2 - 1
	napokszama:= d2-d1
Függvény vége"""



