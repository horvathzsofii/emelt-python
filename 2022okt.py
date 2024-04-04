f = open("jel.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))

print("2. feladat")

sorsz = int(input("Adja meg a jel sorszámát! "))

z = 0

for i in l:
    z += 1
    if z == sorsz:
        print(f"x={i[3]} y={i[4]}")

#3.feladat

def eltelt(h1,m1,s1,h2,m2,s2):
    s = (h2*3600+m2*60+s2)-(h1*3600+m1*60+s1)
    return s

print("4. feladat")

elsoutolso = []
sz = 0

for i in l:
    sz += 1
    if sz == 1:
        h1 = int(i[0])
        m1 = int(i[1])
        s1 = int(i[2])
    elif sz == len(l):
        h2 = int(i[0])
        m2 = int(i[1])
        s2 = int(i[2])


mas = (eltelt(h1,m1,s1,h2,m2,s2))

ora = int(mas/3600)

maradek = mas-(ora*3600)

perc = int(maradek/60)

maradek = 0

maradek = mas-(ora*3600)-(perc*60)

masodp = maradek

print(f"Időtartam: {ora}:{perc}:{masodp}")

print("5. feladat")

#ennek mar nem allok neki