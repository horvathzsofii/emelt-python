f = open("fogado.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))

print("2. feladat")

print(f"Foglalások száma: {len(l)}")

print("3. feladat")

tanar = input("Adjon meg egy nevet: ")

tanar = tanar.split(" ")

c = 0

for i in l:
    if i[0] == tanar[0] and i[1] == tanar[1]:
        c += 1

if c > 0:
    print(f"{tanar[0]} {tanar[1]} néven {c} időpontfoglalás van.")

elif c == 0:
    print("A megadott néven nincs időpontfoglalás.")

print("4. feladat")

ora = input("Adjon meg egy érvényes időpontot (pl 17:10): ")

tanarok = []
t = ""

for i in l:
    if i[2] == ora:
        t = i[0] + ' ' + i[1]
        tanarok.append(t)


tanarok = list(set(tanarok))

tanarok = sorted(tanarok)

for i in tanarok:
    print(i)

jo = ora[0:2] + ora[3:5]


with open(f"{jo}.txt","w") as idosss:
    for i in tanarok:
        idosss.write(f"{i}\n")

print("5. feladat")




"""
napok = []
n = ""
ido = 0

for i in l:
    n = i[3][0:10]
    n = n.split('.')
    ido = int(i[3][11:13])*60 + int(i[3][14:])
    n.append(ido)
    napok.append(n)

napok = sorted(napok)

elso = napok[0]

hour = elso[-1]/60
hour = int(hour)
minute = elso[-1] - (hour*60)

hourminute = ""

hourminute = str(hour) + ":" + str(minute)

elso.pop(-1)

elso.append(hourminute)

elso = elso[0] + "." + elso[1] + "." + elso[2] + "-" + elso[3]

t = ""

for i in l:
    if i[-1] == elso:
        t = i[0] + " " + i[1]
        print(f"Tanár neve: {t}")
        print(f"Foglalt időpont: {i[-2]}")
        print(f"Foglalás ideje: {i[-1]}")

        
"""

print("6. feladat")



foglalasok = []

for i in l:
    if i[0] + " " + i[1] == "Barna Eszter":
        foglalasok.append(i[-2])


ora = [16, 0]

for i in range(12):
    r = str(ora[0]) + ":" + str(ora[1]) + "0"
    if r not in foglalasok:
        print(r)
    if ora[1] < 5:
        ora[1] += 1
    else:
        ora[0] += 1
        ora[1] = 0



"""
foglalasok = []

for i in l:
    if i[0] == "Barna" and i[1] == "Eszter":
        foglalasok.append((int(i[-2][0:2])*60)+int(i[-2][3:]))


helyek = []

for i in range(16*60,17*60+50+1):
    if i % 10 == 0:
        if i not in foglalasok:
            helyek.append(i)


johelyek = []
hm = ""
h = 0
m = 0

for i in helyek:
    h = int(i/60)
    m = i - (h*60)
    if m == 0:
        hm = str(h) + ":" + "00"
    elif m != 0:
        hm = str(h) + ":" + str(m)
    johelyek.append(hm)

for i in johelyek:
    print(i)


foglalasok = sorted(foglalasok)

utcsoh = int(foglalasok[-1]/60)

utcsom = (foglalasok[-1] - utcsoh*60) + 10

utcso = ""

utcso += str(utcsoh) + ":" + str(utcsom)

print(f"Barna Eszter legkorábban távozhat: {utcso}")


"""