import os

def gravaEleitores(listaEleitores):
    Eleitores = open("eleitores.txt",'w')
    for eleitor in listaEleitores:
        Eleitores.write("%s;%s\n" % (eleitor[0],eleitor[1]))
    Eleitores.close()
    


def recuperaEleitores():
    listaEleitores = []
    if (os.path.exists("eleitores.txt")):
        Eleitores = open("eleitores.txt",'r')
        for linha in Eleitores:
            eleitor = linha.strip().split(";")
            listaEleitores.append(eleitor)
        Eleitores.close()
    return listaEleitores

def gravaCandidatos(listaCandidatos):
    Candidatos = open("candidatos.txt",'w')
    for candidato in listaCandidatos:
            Candidatos.write("%s;%s;%s\n" % (candidato[0],candidato[1],candidato[2]))

def recuperaCandidatos():
    listaCandidatos = []
    if (os.path.exists("candidatos.txt")):
        Candidatos = open("candidatos.txt",'r')
        for linha in Candidatos:
            Candidato = linha.strip().split(";")
            listaCandidatos.append(Candidato)
        Candidatos.close()
    return listaCandidatos

def gravaVoto(listaVotos):
    Votos = open("listaVotos.txt",'w')
    for voto in listaVotos:
        Votos.write("%s" % voto)
    Votos.close()

def recuperaVotos():
    listaVotos = []
    if (os.path.exists("listaVotos.txt")):
        Votos = open("listaVotos.txt",'r')
        for linha in Votos:
            listaVotos.append(linha)
        Votos.close()
    return listaVotos
