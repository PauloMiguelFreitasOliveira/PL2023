


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
                 





def diseasePerTier(lista):
    escaloes = [0]*12
    total = 0

    for d1 in lista:
        if d1["temDoenÃ§a"] == 1:
            total += 1
            if d1["idade"] in range(29,35):
                escaloes[0] += 1
            elif d1["idade"] in range(34,40):
                escaloes[1] += 1
            elif d1["idade"] in range(39,45):
                escaloes[2] += 1
            elif d1["idade"] in range(44,50):
                escaloes[3] += 1
            elif d1["idade"] in range(49,55):
                escaloes[4] += 1
            elif d1["idade"] in range(54,60):
                escaloes[5] += 1
            elif d1["idade"] in range(59,65):
                escaloes[6] += 1
            elif d1["idade"] in range(64,70):
                escaloes[7] += 1
            elif d1["idade"] in range(69,75):
                escaloes[8] += 1
            elif d1["idade"] in range(74,80):
                escaloes[9] += 1
            elif d1["idade"] in range(79,85):
                escaloes[10] += 1
            elif d1["idade"] in range(84,90):
                escaloes[11] += 1
    

    return total,escaloes



def diseasePerCholes(lista,total):

    dic1 = []
    
    for minimo in range(0,500,10):
        count = 0
        for i,d1 in enumerate(lista):
            if d1["temDoenÃ§a"] == 1 and minimo < d1["colesterol"] < minimo + 10:
                count+=1
        dic1.append(count/total)
    return dic1
    
                

def print_percentagem_sexo(dist):
    

    print("+------------------+--------------------+")
    print("|    Genero        |    Percentagem    |")
    print("+------------------+--------------------+")
    print("|    Masculino     |       {:.2f}       |".format(dist))
    print("|    Female        |       {:.2f}       |".format(dist))
    print("+------------------+--------------------+")



def print_percentagem_escalao(escaloes):
    
    print("+------------------+--------------------+")
    print("|    Escalao        |    Percentagem    |")
    print("+------------------+--------------------+")
    print(f"|    [29..35]     |      {escaloes[0]}       |")
    print(f"|    [34..40]     |      {escaloes[1]}        |")
    print(f"|    [39..45]     |      {escaloes[2]}        |")
    print(f"|    [44..50]     |      {escaloes[3]}        |")
    print(f"|    [49..55]     |      {escaloes[4]}        |")
    print(f"|    [54..60]     |      {escaloes[5]}        |")
    print(f"|    [59..65]     |      {escaloes[6]}        |")
    print(f"|    [64..70]     |      {escaloes[7]}        |")
    print(f"|    [69..75]     |      {escaloes[8]}        |")
    print(f"|    [74..80]     |       {escaloes[9]}       |")
    print(f"|    [79..85]     |       {escaloes[10]}       |")    
    print(f"|    [84..90]     |       {escaloes[11]}       |")                    
    print("+------------------+--------------------+")



def print_colesterol(dic1):
      
    print("+----------------------------+--------------------+")
    print("|    Nível-Colesterol        |    Percentagem    |")
    print("+----------------------------+---------------------+")
    for x,i in enumerate(dic1):
        print("|    {}..{}     |      {:.5f}       |".format(x*10,x*10+10,i))
    print("+------------------+--------------------+")



def menu():
    lista = armazena()
    print("Selecione a distribuição que quer ver:")
    print("1. Distribuição da doença por sexo.")
    print("2. Distruibuição por faixa etária.")
    print("3. Distribuição por níveis de colesterol.")
    entrada = input(">")
    if entrada == "1":
        dist = diseasePerSex(lista)
        print_percentagem_sexo(dist)
    elif entrada == "2":
        total,escaloes = diseasePerTier(lista)
        print_percentagem_escalao(escaloes)
    elif entrada == "3":
        total,escaloes = diseasePerTier(lista)
        dic1 = diseasePerCholes(lista,total)
        print_colesterol(dic1)
    

menu()
