f = open("hivas.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))

def mpbe(h, m, s):
    h = h*3600
    m = m*60
    k = h + m + s
    return k

orak = []

for i in l:
    orak.append(i[0])

orak = list(set(orak))


orak1 = [int(i) for i in orak]

orak1.sort()

print(orak1)

orak2 = [str(i) for i in orak1]

szama = []

print("3. feladat")

for i in orak2:
    z = 0
    for j in l:
        if j[0] == i:
            z += 1
    
    print(f"{i} ora {z} hivas")

print("4. feladat")

v = 0

for i in l:
    ido = (int(i[3])*3600+int(i[4])*60+int(i[5]))-(int(i[0])*3600+int(i[1])*60+int(i[2]))
    if ido > v:
        v = ido


sz = 0


for i in l:
    ido = (int(i[3])*3600+int(i[4])*60+int(i[5]))-(int(i[0])*3600+int(i[1])*60+int(i[2]))
    sz += 1
    if ido == v:
        break

print(f"A leghosszabb ideig vonalban lévő hívó {sz}. sorban szerepel, a hívás hossza {v} másodperc.")

print("5. feladat")

bek = input("Adjon meg egy idopontot! (ora perc masodperc)")


h,m,s = bek.split()

bekido = int(h)*3600+int(m)*60+int(s)

k = 0
hivott = []

"""for i in l:
    ido = (int(i[3])*3600+int(i[4])*60+int(i[5]))-(int(i[0])*3600+int(i[1])*60+int(i[2]))
    hivas = (int(i[0])*3600+int(i[1])*60+int(i[2]))
    if hivas > sz:
        sz = hivas
        k += 1
        hivott.append(i)
        sz = 0


