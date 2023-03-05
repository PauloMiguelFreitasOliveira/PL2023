import re
import json

def ler():
    
    dados = []
    f = open("processos.txt")
    content = f.read()
    f.close()

    for linha in content:
        pessoa = {}
        split = re.split(r'::+', linha)
        split = split[:-1]

        for x in split:
            danificado = len(re.findall(r'Doc.Danificado', linha))

            if danificado == 0:
                if len(split) > 0:
                    pessoa['pasta'] = split[0]
                if len(split) > 1:
                    pessoa['data'] = split[1]
                if len(split) > 2:
                    pessoa['nome'] = split[2]
                if len(split) > 3:
                    pessoa['Pai'] = split[3]
                if len(split) > 4:
                    pessoa['Mãe'] = split[4]
                if len(split) > 5:
                    pessoa['Observações'] = split[5]
                if pessoa:
                    dados.append(pessoa)
    return dados

def freqAno(dados):

    freq = {}

    for pessoa in dados:
        data = re.split(r'-', pessoa['data'])

        ano = data[0]

        if ano in freq:
            freq[ano] += 1
            
        else: 
            freq[ano] = 1
    
    return freq

def top5freq(dados):

    final = {f'Século {i}':[[]] for i in range(1,21)}
    for pessoa in dados:
        nome = re.split(r' ', pessoa['nome'])
        primeiro_ultimo_nome = [nome[0],nome[2]]

        data = re.split(r'-', pessoa['data'])
        ano = data[0]
        seculo = re.findall(r'\d\d',ano) + 1
        final[seculo].append(primeiro_ultimo_nome) 

        

def freqRelacao(dados):
    freq = {}
    for pessoa in dados:
        obs = pessoa.get("Observações")

        if obs:
            relacoes = re.findall(r",((Tio|Irmao|Sobreinho|Tia|Avo)s*)[.|]",obs)
            if relacoes:
                for relacao in relacoes:
                    if relacao[0] in freq:
                        freq[relacao[0]] += 1
                    else:
                        freq[relacao[0]] = 1
    return freq

def toJason(dados):
    f = open("processos.json", 'w')
    i = 0
    while i < 20:
        pessoa = dados[i]
        f.write(json.dumps(pessoa))
        if i < 19:
            f.write(",")
        i += 1
    f.close()


dados = ler()
freqAno(dados)
top5freq(dados)
freqRelacao(dados)
toJason(dados)


        






        
