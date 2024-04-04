f = open("utca.txt")

l = []
d = 0

for i in f:
    l.append(i.strip().split(" "))

elso_sor = l[0]
l = l[1:]


print(f"A mintában {len(l)} ")
"""
s = input("Adj meg egy adószámot")

z = True

for i in l:
    if i[0] == s:
        print(f"{i[1]} utca {i[2]}")
        z = False


if z:
    print("Nem szerepel az adatállományban")

    
"""

def ado(sor):
    if sor[3] == "A":
        return 800*int(sor[4])
    if sor[3] == "B":
        return 600*int(sor[4])
    if sor[3] == "C":
        return 100*int(sor[4])

    
    return 0

print(ado(l[0]))
a = 0
b = 0
c = 0
a_adoszam = 0
b_adoszam = 0
c_adoszam = 0
for i in l:
    if i[3] == "A":
        a += 1
        a_adoszam += ado(i)
    elif i[3] == "B":
        b += 1
        b_adoszam += ado(i)
    elif i[3] == "C":
        c += 1
        c_adoszam += ado(i)


print(f"A sávba {a} telek esik, az adó {a_adoszam} FT.")
print(f"B sávba {b} telek esik, az adó {b_adoszam} FT.")
print(f"C sávba {c} tlek esik, az adó {c_adoszam} FT.")

utcan = []
k = []
for i in l:
    utcan.append(i[1])

utcan = list(set(utcan))

for i in utcan: 
    for j in l:
        if j[1] == i: # sorban vizsgált utcanév az egyenlő  az utcanévevel ami az i
            k.append(j[3]) 
    k = set(k)
    if len(k) > 1:
        print(i)
    k = []