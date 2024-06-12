f = open("furdoadat.txt") 
l = []
l2 = []
rendes = []

for i in f:
    l.append(i.strip().split(" "))


print("2. feladat")

elso = l[0][3::]

utolso = []

print(f"Az első vendég {elso[0]}:{elso[1]}:{elso[2]}-kor lépett ki az öltözőből.")


for i in l:
    if i[1] == "0" and i[2] == "1":
        utolso.append(i[3::])
 

utolso = utolso[-1]

print(f"Az utolsó vendég {utolso[0]}:{utolso[1]}:{utolso[2]}-kor lépett ki az öltözőből.")

print("3. feladat")

azon = []

for i in l:
    azon.append(i[0])


azon = list(set(azon))

for i in azon:
    for j in l:
        if j[0] == i:
            l2.append(j)



    rendes.append(l2)
    l2 = []

c = 0

for i in rendes:
    if len(i) <= 4:
        c += 1

print(f"A fürdőben {c} vendég járt csak egy részlegen.")

print("4. feladat")

ido = 0
n = 0
h = 0
m = 0
s = 0

for i in rendes:
    ido = (int(i[-1][3])*60*60 + int(i[-1][4])*60 + int(i[-1][5])) -  (int(i[0][3])*60*60 + int(i[0][4])*60 + int(i[0][5]))
    if ido > n:
        n = ido

for i in rendes:
    ido = (int(i[-1][3])*60*60 + int(i[-1][4])*60 + int(i[-1][5])) -  (int(i[0][3])*60*60 + int(i[0][4])*60 + int(i[0][5]))
    if ido == n:
        h = int(n/60/60)
        m = int((n - h*60*60)/60)
        s = n - h*60*60 - m*60
        print(f"A legtöbb időt eltöltő vendég:")
        print(f"{i[0][0]}. vendég {h}:{m}:{s}")

print("5. feladat")


hatos = 0
kilences = 0
negyes = 0

for i in rendes:
    if int(i[0][-3]) >= 6 and int(i[0][-3]) < 9:
        hatos += 1

    elif int(i[0][-3]) >= 9 and int(i[0][-3]) < 16:
        kilences += 1

    elif int(i[0][-3]) >= 16 and int(i[0][-3]) < 20:
        negyes += 1


print(f"6-9 óra között {hatos} vendég")
print(f"9-16 óra között {kilences} vendég")
print(f"16-20 óra között {negyes} vendég")

print("7. feladat")

u = 0
uszod = 0
gy = 0
gogy = 0
sz = 0
szaun = 0 
s = 0
strand = 0

for i in rendes:
    for j in i:
        if j[1] == "1":
            u = 1

        elif j[1] == "3":
            gy = 1

        elif j[1] == "2":
            sz = 1

        elif j[1] == "4":
            s = 1

    if u == 1:
        uszod += 1
        u = 0

    if gy == 1:
        gogy += 1
        gy = 0

    if sz == 1:
        szaun += 1
        sz = 0

    if s == 1:
        strand += 1
        s = 0


print(f"Uszoda: {uszod}")
print(f"Szaunák: {szaun}")
print(f"Gyógyvizes medencék: {gogy}")
print(f"Strand: {strand}")