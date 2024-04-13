f = open("kiserlet.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))

import random

print("1. feladat")

dobas = random.randint(1,2)

if dobas == 1:
    dobas = "F"

elif dobas == 2:
    dobas = "I"

print(f"A pénzfeldobás eredménye: {dobas}")

print("2. feladat")

tipp = input("Tippeljen! (F/I)= ")

feldob = random.randint(1,2)

if feldob == 1:
    feldob = "F"

elif feldob == 2:
    feldob = "I"

if feldob == tipp:
    print(f"A tipp {tipp}, a dobás eredménye {feldob} volt.")
    print("Ön eltalálta!")

elif feldob != tipp:
    print(f"A tipp {tipp}, a dobás eredménye {feldob} volt.")
    print("Ön nem találta el.")

print("3. feladat")

print(f"A kisérlet {len(l)} dobásból állt.")

print("4. feladat")

sz = 0

for i in l:
    if i == ["F"]:
        sz += 1

gyak = round(sz/len(l)*100,2)



print(f"A kisérlet során a fej relativ gyakorisága {gyak}% volt.")

print("5. feladat")

sz = 0
s = 0


for i in l:
    if sz == 2 and i == ["I"]:
        s += 1
        sz = 0
    elif i == ["F"]:
        sz += 1
    elif i == ["I"]:
        sz = 0
    elif sz > 2:
        sz = 0


print(f"A kisérlet során {s} alkalommal dobtak pontosan két fejet egymás után.")


print("6. feladat.")

sz = 0
s = 0
z = 0

for i in l:
    if i == ["F"]:
        sz += 1
    
    elif i == ["I"]:
        sz = 0

    if sz > s:
        s = sz


for i in l:
    z += 1
    if i == ["F"]:
        sz += 1
    
    elif i == ["I"]:
        sz = 0

    if sz == s:
        break


z = z - s + 1

print(f"A leghosszabb tisztafej sorozat {s} tagból áll, kezdete a {z} dobás.")

