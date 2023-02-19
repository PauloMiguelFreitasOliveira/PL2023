def armazena():

    lista = []

    f = open("myheart.csv", "rt")
    content = f.read()
    f.close()

    linhas = content.split("\n")[:-1]

    keys = linhas[0].split(",")

    for linha in linhas[1:]:
        parametro = linha.split(",")
        d1 = {}
        for i, key in enumerate(keys):
            if i==1:
                d1[key] = parametro[i]
            else: 
                d1[key] = int(parametro[i])
              
        lista.append(d1)

    return lista

lista = armazena()



def diseasePerSex(lista):
    count = 0
    countM = 0
    countF = 0 
    dist = 0.0
     
    for d1 in lista: 
        if d1["temDoenÃ§a"] == 1: 
            count= count + 1 
            if d1["sexo"] == "M":
                 countM = countM + 1 

            elif d1["sexo"] == "F":
                 countF = countF + 1 
    dist = countM/count 

    return dist
                 
dist = diseasePerSex(lista)

print("A doença está presente em {:.2f}% de homens e em {:.2f}% de mulheres".format(dist,1-dist))


def diseasePerTier(lista):
    stat1 = 0
    stat2 = 0
    stat3 = 0
    stat4 = 0
    stat5 = 0
    stat6 = 0
    stat7 = 0
    stat8 = 0
    stat9 = 0
    stat10 = 0
    stat11 = 0
    stat12 = 0
    total = 0

    for d1 in lista:
        if d1["temDoenÃ§a"] == 1:
            total = total + 1
            if d1["idade"] in range(29,35):
                stat1 = stat1 + 1
            elif d1["idade"] in range(34,40):
                stat2 = stat2 + 1
            elif d1["idade"] in range(39,45):
                stat3 = stat3 + 1
            elif d1["idade"] in range(44,50):
                stat4 = stat4 + 1
            elif d1["idade"] in range(49,55):
                stat5 = stat5 + 1
            elif d1["idade"] in range(54,60):
                stat6 = stat6 + 1
            elif d1["idade"] in range(59,65):
                stat7 = stat7 + 1
            elif d1["idade"] in range(64,70):
                stat8 = stat8 + 1
            elif d1["idade"] in range(69,75):
                stat9 = stat9 + 1
            elif d1["idade"] in range(74,80):
                stat10 = stat10 + 1
            elif d1["idade"] in range(79,85):
                stat11 = stat11 + 1
            elif d1["idade"] in range(84,90):
                stat12 = stat12 + 1
    
    print("A distribuição de doença nas diferentes faixas etárias foi: {:.2f}%, {:.2f}%, {:.2f}%, {:.2f}%, {:.2f}%, {:.2f}%, {:.2f}%, {:.2f}%, {:.2f}%, {:.2f}%, {:.2f}%, {:.2f}%".format(stat1/total,stat2/total,stat3/total,stat4/total,stat5/total,stat6/total,stat7/total,stat8/total,stat9/total,stat10/total,stat11/total,stat12/total))

    return this

this= diseasePerTier(lista)



