f = open("meresek.txt")
l = []

for i in f:
    l.append(i.strip().split(" "))

print("2. feladat")

print(f"A mérés során {len(l)} jármű adatait rögzítették.")

print("3. feladat")

c = 0

for i in l:
    if i[5] < "9":
        c += 1


print(f"9 óra előtt {c} jármű haladt el a végponti mérőnél.")

print("4. feladat")

oraperc = input("Adjon meg egy óra és perc értékét! ")

orap = []

orap.append(oraperc.split(" "))

ora = str(orap[0][0])
perc = str(orap[0][1])

c = 0

for i in l:
    if i[1] == ora and i[2] == perc:
        c += 1

print(f"\ta. A kezdeti mérépontnál elhaladt járművek száma: {c}")

c = 0

for i in l:
    if int(i[1]) <= int(ora) and int(i[2]) <= int(perc) and int(i[5]) >= int(ora) and int(i[6]) >= int(perc):
        c += 1

print(f"\tb. A forgalomsűrűség: {c/10}")

print("5. feladat")
print("A legnagyobb sebeséggel haladó jármű")

rendszam = ""
atlagok = []
atlag = 0
kezdo = 0
vegso = 0

for i in l:
    atlag  = 10/((int(i[5]) + (int(i[6])/60) + (int(i[7]) + round((int(i[8])*0.001),3))/60/60) - (int(i[1]) + (int(i[2])/60) + (int(i[3]) + round((int(i[4])*0.001),3))/60/60))
    atlagok.append(atlag)

m = max(atlagok)

for i in l:
    atlag = 10/((int(i[5]) + (int(i[6])/60) + (int(i[7]) + round((int(i[8])*0.001),3))/60/60) - (int(i[1]) + (int(i[2])/60) + (int(i[3]) + round((int(i[4])*0.001),3))/60/60))
    if atlag == m:
        rendszam = i[0]
        kezdo = (int(i[5]) + (int(i[6])/60) + (int(i[7]) + round((int(i[8])*0.001),3))/60/60)
        vegso = (int(i[1]) + (int(i[2])/60) + (int(i[3]) + round((int(i[4])*0.001),3))/60/60)

c = 0

for i in l:
    k = (int(i[5]) + (int(i[6])/60) + (int(i[7]) + round((int(i[8])*0.001),3))/60/60)
    v = (int(i[1]) + (int(i[2])/60) + (int(i[3]) + round((int(i[4])*0.001),3))/60/60)
    if vegso >= v and kezdo <= k:
        c += 1

c = c-1
m = round(m)

print(f"\trendszáma: {rendszam}\n\tátlagsebessége: {m}\n\táltal lehagyott járművek száma: {c}")

print("6. feladat")

c = 0

for i in l:
    atlag = 10/((int(i[5]) + (int(i[6])/60) + (int(i[7]) + round((int(i[8])*0.001),3))/60/60) - (int(i[1]) + (int(i[2])/60) + (int(i[3]) + round((int(i[4])*0.001),3))/60/60))
    if atlag > 90:
        c += 1

osszes = round(c/len(l)*100,2)

print(f"A járművek {osszes}%-a volt gyorshajtó.")

with open("buntetes","w") as buntetes:
    for i in l:
        atlag = 10/((int(i[5]) + (int(i[6])/60) + (int(i[7]) + round((int(i[8])*0.001),3))/60/60) - (int(i[1]) + (int(i[2])/60) + (int(i[3]) + round((int(i[4])*0.001),3))/60/60))
        if atlag > 104:
            if atlag <= 121:
                atlag = round(atlag)
                buntetes.write(f"{i[0]}\t{atlag} km/h\t30000 Ft\n")

            elif atlag > 121 and atlag <= 136:
                atlag = round(atlag)
                buntetes.write(f"{i[0]}\t{atlag} km/h\t45000 Ft\n")

            elif atlag > 136 and atlag <= 151:
                atlag = round(atlag)
                buntetes.write(f"{i[0]}\t{atlag} km/h\t60000 Ft\n")

            elif atlag > 151:
                atlag = round(atlag)
                buntetes.write(f"{i[0]}\t{atlag} km/h\t200000 Ft\n")

print("A fájl elkészült.")