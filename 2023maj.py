f = open("taborok.txt")
l = []

for i in f:
    l.append(i.strip().split('\t'))

print("2. feladat")
print(f"Az adatsorok száma: {len(l)}")
print(f"Az először rögzített tábor témája: {l[0][5]}")
print(f"Az utoljára rögzített tábor témája: {l[-1][5]}")

print("3. feladat")

c = 0
for i in l:
    if i[5] == "zenei":
        c = 1
        print(f"Zenei tábor kezdődik {i[0]}. hó {i[1]}. napján.")

if c == 0:
    print("Nem volt zenei tábor.")


print("4. feladat")
print("Legnépszerűbbek: ")

nagyobb = 0

for i in l:
    if len(i[4]) > nagyobb:
        nagyobb = len(i[4])

for i in l:
    if len(i[4]) == nagyobb:
        print(i[0],i[1],i[5])

print("5. feladat")

def sorszam(honap,nap):
    c = 0
    if honap == 6:
        c = nap - 15
    elif honap == 7:
        c = nap + 15
    elif honap == 8:
        c = 15 + 31 + nap

    return c

print("6. feladat")
ho = int(input("hó: "))
napja = int(input("nap: "))

tabor = sorszam(ho,napja)
c = 0

for i in l:
    if sorszam(int(i[0]),int(i[1])) <= tabor and sorszam(int(i[2]),int(i[3])) >= tabor:
        c += 1

print(f"Ekkor éppen {c} tábor tartott.")

print("7. feladat")
tanulo = input("Adja meg egy tanuló betüjelét: ")
egy = []
taboros = []
c = ""
for i in l:
        if tanulo in i[4]:
            if int(i[1]) > 10:
                c = i[0] + i[1]
            elif int(i[1]) < 10:
                c = i[0] + "0" + i[1]
            egy.append([c,i[2],i[3],i[5]])
            taboros.append([i[0],i[1],i[2],i[3]])

egy = sorted(egy)

ketto = []
for i in egy:
    if i[0][1] != '0':
        ketto.append([f"{i[0][0]}.{i[0][1:]}-{i[1]}.{i[2]}. {i[3]}"])
    if i[0][1] == '0':
        ketto.append([f"{i[0][0]}.{i[0][2:]}-{i[1]}.{i[2]}. {i[3]}"])

with open("egynapos.txt","w") as egynapos:
    for i in ketto:
        for j in i:
            egynapos.write(j)
            egynapos.write("\n")


amikor = []
c1 = 0
c2 = 0

for i in taboros:
    c1 = sorszam(int(i[0]),int(i[1]))
    c2 = sorszam(int(i[2]),int(i[3]))
    amikor.append([c1,c2])

c = 0
for i in range(len(amikor)):
        for j in range(len(amikor)):
            if amikor[i][0] <= amikor[j][0] and amikor[i][1] >= amikor[j][1]:
                c = 1

if c == 1:
    print("Nem mehet el mindegyik táborba.")
elif c == 0:
    print("Mindegyiken részt tud venni.")