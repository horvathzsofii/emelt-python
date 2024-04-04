f = open("ajto.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))

print("2. feladat")

sz = 0

for i in l:
    sz += 1
    if sz == 1:
        elso = i[2]
    
sz = 0

for i in l:
    if i[3] == "ki":
        sz += 1

s = 0

for i in l:
    if i[3] == "ki":
        s += 1
        if s == sz:
            utolso = i[2]

#ezt most valoszinu bonyolultabban nem is lehetett volna

print(f"Az első belépő: {elso}")
print(f"Az utolsó kilépő: {utolso}")

print("3. feladat")

#en ezt most itt csinalom

szemelyek = []

for i in l:
    szemelyek.append(i[2])

szemelyek = list(set(szemelyek))

szemelyek = [int(i) for i in szemelyek]

szemelyek = sorted(szemelyek)

belepesek = []


for i in szemelyek:
    sz = 0
    for j in l:
        if int(j[2]) == i:
            sz += 1

    belepesek.append(sz)

print(szemelyek)
print(belepesek)

print("4. feladat")

beki = []
tartkozk = []

for i in szemelyek:
    for j in l:
        if int(j[2]) == i:
            beki.append(j[3])
    if beki[-1] == "be":
        tartkozk.append(i)

print(f"A végén a társalgóban voltak: {tartkozk}")

print("5. feladat")

sz = 0
bentlevok = []

for i in l:
    if i[3] == "be":
        sz += 1
    elif i[3] == "ki":
        sz = sz - 1
    bentlevok.append(sz)

m = max(bentlevok)

sz = 0

for i in bentlevok:
    sz += 1
    if i == m:
        break

s = 0

for i in l:
    s += 1
    if s == sz:
        ido1 = i[0]
        ido2 = i[1]


print(f"Például {ido1}:{ido2}-kor voltak a legtöbben a társalgóban.")

print("6. feladat")

azon = input("Adja meg a személy azonosítóját! ")

print("7. feladat")

helyek = []
be = 0
ki = 0

for i in l:
    if len(helyek) == 4:
        print(f"{helyek[0]}:{helyek[1]}-{helyek[2]}:{helyek[3]}")
        helyek = []

    elif i[2] == azon:
        helyek.append(i[0])
        helyek.append(i[1])
        if i[3] == "be":
            be += 1
        elif i[3] == "ki":
            ki += 1

sz = 0
    
if ki != be:
    for i in l:
        if i[2] == azon:
            sz += 1

s = 0

if ki != be:
    for i in l:
        if i[2] == azon:
            s += 1
            if s == sz:
                utolsoo = int(i[0])*60+int(i[1])
                print(f"{i[0]}:{i[1]}-")

#na ez most megint nagy kabare, de mukodik

print("8. feladat")

sz = 0
ora3 = 0
helyek = []

if ki == be:
    for i in l:
        if len(helyek) == 4:
            ora1 = int(helyek[0])*60+int(helyek[1])
            ora2 = int(helyek[2])*60+int(helyek[3])
            ora0 = ora2-ora1
            ora3 += ora0
            helyek = []

        elif i[2] == azon:
            helyek.append(i[0])
            helyek.append(i[1])

    print(f"A(z) {azon} személy összesen {ora3} percet volt bent, a megfigyelés végén nem volt a társalgóvan.")


if ki != be:
    for i in l:
        if len(helyek) == 4:
            ora1 = int(helyek[0])*60+int(helyek[1])
            ora2 = int(helyek[2])*60+int(helyek[3])
            ora0 = ora2-ora1
            ora3 += ora0
            helyek = []

        elif i[2] == azon:
            helyek.append(i[0])
            helyek.append(i[1])
    ora3 += 15*60-utolsoo

    print(f"A(z) {azon} személy összesen {ora3} percet volt bent, a megfigyelés végén a társalgóban volt.")

#juhu csak a harmast kene rendesre de ahhoz most nincs kedvem