f = open("tavirathu13.txt")

l = []
telepl = []
z = 0
telepz = []
k = ""

maxido = 0
minido = 0
p = 0
s = 0

varosok = []
homerseklet = []

for i in f:
    l.append(i.strip().split(" "))

print("2. feladat")
telep = input("Adja meg egy település kódját! Település: ")

for i in l:
    if i[0] == telep:
        telepl.append(i[1])

m = max(telepl)

sz = "2345"

s = sz[0:1] + ":" + sz[2:3]
 


for i in m:
    z += 1
    telepz.append(i)
    if z == 2:
        telepz.append(":")

for i in telepz:
    k = k + i

print(f"Az utolsó mérési adat a megadott településről {k}-kor érkezett.")

print("3.feladat")

for i in l:
    if minido == 0:
        minido = i[3]
    elif i[3] < minido:
        minido = i[3]

for i in l:
    if minido == i[3]:
        print(f"A legalacsonyabb hőmérséklet: {i[0]} {i[1]} {minido} fok.")


for i in l:
    if maxido == 0:
        maxido = i[3]
    elif i[3] > maxido:
        maxido = i[3]


for i in l:
    if maxido == i[3]:
        print(f"A legmagasabb hőmérséklet: {i[0]} {i[1]} {maxido} fok.")
        break
        

print("4. feladat")

for i in l:
    if i[2] == "00000":
        print(i[0],i[1])
        p += 1


if p == 0:
    print("Nem volt szélcsend a mérések idején")


print("5. feladat")

for i in l:
    if i[0] not in varosok:
        varosok.append(i[0])


for i in varosok:
    homerseklet = []
    homerseklet0 = []
    homerseklet1 = []
    homerseklet2 = []  
    homerseklet3 = []
    maxho = 0
    minho = 0
    for j in l:
        if i == j[0]:
            if j[1] >= '0100' and j[1] < '0200':
                homerseklet0.append(int(j[3]))
            elif j[1] >= '0700' and j[1] < '0800':
                homerseklet1.append(int(j[3]))
            elif j[1] >= '1300' and j[1] < '1400':
                homerseklet2.append(int(j[3]))
            elif j[1] >= '1900' and j[1] < '2000':
                homerseklet3.append(int(j[3]))
    
            if minho == 0:
                minho = j[3]
            elif minho != 0:
                if j[3] < minho:
                    minho = j[3]
            if maxho == 0:
                maxho = j[3]
            elif maxho != 0:
                if j[3] > maxho:
                    maxho = j[3]

    ingad = int(maxho) - int(minho)
    if len(homerseklet0)*len(homerseklet1)*len(homerseklet3) == 0:
        print(f"{i} NA; Hőmérséklet-ingadozás: {ingad}")
    elif len(homerseklet0)*len(homerseklet1)*len(homerseklet3) != 0:
        homerseklet = (sum(homerseklet0)/len(homerseklet0) + sum(homerseklet1)/len(homerseklet1) + sum(homerseklet2)/len(homerseklet2) + sum(homerseklet3)/len(homerseklet3))/4
        print(f"{i} Középhőmérséklet: {round(homerseklet)}; Hőmérséklet-ingadozás: {ingad}")
