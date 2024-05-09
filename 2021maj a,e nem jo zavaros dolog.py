f = open("melyseg.txt")

l = []

for i in f:
    l.append(i.strip().split(" "))

print("1. feladat")
print(f"A fájl adatainak száma: {len(l)}")

print("2. feladadt")

tavolsagertek = input("Adjon meg egy távolságértéket! ")

c = 0
for i in l:
    c += 1
    if c == int(tavolsagertek):
        print(f"Ezen a helyen a felszín {i[0]} méter mélyen van.")

print("3. feladat")

c = 0
for i in l:
    if i[0] == "0":
        c += 1

arany = round(c/len(l),4)*100

print(f"Az érintetlen terület aránya {arany}%")

kisgodrok = []
nagygodrok = []

with open("godrok.txt","w") as godrok:
    for i in l:
        if i[0] != "0":
            kisgodrok.append(i[0])

        elif i[0] == "0":
            if kisgodrok != []:
                nagygodrok.append(kisgodrok)
            kisgodrok = []



    for i in nagygodrok:
        for j in i:
            godrok.write(f"{j} ")
        godrok.write('\n')


print("5. feladat")

f2 = open("godrok.txt")
godroktxt = []

for i in f2:
    godroktxt.append(i.strip().split(" "))

print(f"A gödrök száma: {len(godroktxt)}")

print("6. feladat")
print("a)")

c = 0
meter = 0
for k in l:
    c += 1
    if c == int(tavolsagertek) and k[0] == "0":
        print("Az adott helyen nincs gödör.")

    elif c == int(tavolsagertek) and k[0] != '0':
        kisgodrok = []
        nagygodrok = []

        for i in l:
            if i[0] != "0":
                kisgodrok.append(i[0])

            elif i[0] == "0":
                if kisgodrok == []:
                    kisgodrok = ["0"]
                    nagygodrok.append(kisgodrok)
                else:
                    nagygodrok.append(kisgodrok)
                kisgodrok = []

        meter = 0
        c = 0
        for i in nagygodrok:
            for j in i:
                meter += 1
                if j == "0":
                    c = 0
                elif j != "0":
                    c += 1

                if meter == int(tavolsagertek):
                    kezdo = meter-c + 1
                    vegso =  kezdo + len(i) - 1

print(f"A gödör kezdete: {kezdo} méter, a gödör vége {vegso} méter.")


                        

print("b)")

meter = 0
c = 0
nagyon = 0
for i in nagygodrok:
    for j in i:
        meter += 1
        if meter == int(tavolsagertek):
            nagyobb = 0
            valtozo = 0
            m = max(i)
            for j in i:
                valtozo += 1
                if j == m:
                    break

            for k in range(len(i)):
                c += 1
                if c < valtozo:
                    if i[k-1] < i[k]:
                        nagyobb += 1

                elif c > valtozo:
                    if i[k-1] > i[k]:
                        nagyobb += 1
                
            if nagyobb + 1 == len(i):
                print("Folyamatosan mélyül")

            else:
                print("Nem folyamatosan mélyül.")
print("c)")
meter = 0
for i in nagygodrok:
    for j in i:
        meter += 1
        if meter == int(tavolsagertek):
            print(f"A legnagyobb mélysége {max(i)} méter.")

print("d)")
meter = 0
terulet = 0
for i in nagygodrok:
    for j in i:
        meter += 1
        if meter == int(tavolsagertek):
            for j in i:
                terulet += int(j)

terulet = terulet*10
print(f"A terfogata {terulet} m^3.")

print("e)")

