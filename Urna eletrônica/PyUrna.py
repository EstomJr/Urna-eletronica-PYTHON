import os,time
import PyGravador 

listadeVotos = PyGravador.recuperaVotos()
eleitores = PyGravador.recuperaEleitores()
candidatos = PyGravador.recuperaCandidatos()

print("""
##########################################################################
                                           
                                           
            ================  ===========   ============
            =              =  ==        ==  ============ 
            ======    ======  ==        ==  ==
                  =  =        ==        ==  ==
                  =  =        ==========    ===========
                  =  =        ===           ===========         
                  =  =        == ==         ==
                  =  =        ==  ==        ==
                  =  =        ==   ==       ============
                  ====        ==    ==      ============        
                                             
                           ⚡ -DO TRABSON- ⚡


#########################################################################
""")                                 
    
print()
print ("DIGITE -OK- PARA INICIAR")
opcao = input()
if opcao == "ok" or "OK":
   os.system("cls")

sair = True
while (sair):
   print("BEM VINDO AO TRE - UFPB, ESCOLHA UMA DAS OPÇÕES")
   print ()
   print("""1) Cadastrar eleitor;
   2) Listar eleitores;
   3) Alterar dados do eleitor;
   4) Cadastrar candidato;
   5) Listar candidatos;
   6) Alterar candidato;
   7) Registrar voto indicando a matrícula do eleitor e o número do seu candidato;
   8) Consultar votos obtidos por candidato;
   9) Consultar número de eleitores que já votaram;
   10) Consultar número de eleitores que ainda não votaram;
   11) Sair""")

   menu = int(input())

   if menu == 1:
       nome = input ("Nome do eleitor: ")
       ID = int(input ("Número de identificação: "))
       eleitores.append([nome, ID])
       PyGravador.gravaEleitores(eleitores)

   elif menu == 2:
       print ("Carregando %")
       time.sleep(1)
       for k in eleitores:
          print (k)

   elif menu == 3:
       print(eleitores)
       menu = input("Informe o ID de quem você deseja alterar os dados: ")
       for k in eleitores:
         if menu in k:
           k == input("Informe o NOME ou o ID desejado: ") 
           PyGravador.gravaEleitores(eleitores)

   elif menu == 4:
     nome = input ("Nome do candidato: ")
     voto = int(input("Número do candidato"))
     candidatos.append([nome, voto])
     PyGravador.gravaCandidatos(candidatos)

   elif menu == 5:
      for k in candidatos:
         print (k)

   elif menu == 6:
     menu = input("informe o PARTIDO de qeum você deseja alterar os dados: ")
     for k in candidatos:
         if menu in k:
           k == input("Infome o NOME ou o PARTIDO ou o NÚMERO desejado: ")
           PyGravador.gravaCandidatos(candidatos)

   elif menu == 7:
        confirmar = False
        condicao = False
        os.system("cls")
        ID = input('digite seu ID: ')
        for k in eleitores:
            if k[1] == ID:
                print(k[0])
                condicao = True
        if condicao==False:
            confirmar=True
                
        if confirmar == True:
            print("Eleitor não cadastrado")
            opcao = input("Aperte qualquer tecla para voltar ")
            
        while confirmar == False:
            VOTO = int(input("Digite o Número do seu candidato: "))
            for y in candidatos:
               if VOTO == y[1]:
                       print(y)
            confirma = input("Deseja confirmar seu voto? ")
            if confirma == "S" or confirma == "s":
                listadeVotos.append(VOTO)
                listadeVotos.append("\n")
                PyGravador.gravaVoto(listadeVotos)    
                confirmar = True
                condicao = True          
                k[2] = True
   elif menu == 8:
        TotalValidos = 0
        Total = 0
        Alckimin = 0 #
        Alvaro = 0 #
        Amoedo = 0 #
        Bolsonaro = 0 #
        Boulos = 0 #
        Ciro = 0 #
        Daciolo = 0 #
        Vera = 0 #
        Marina = 0 #
        Meirelles = 0 #
        Eymael = 0 #
        Haddad = 0 #
        Goulart = 0 #
        Nulo = 0
        Branco = 0
        votos=[]
        for k in listadeVotos:
            votos.append(k)
            if k == "17\n":
                Bolsonaro+=1
                Total+=1
                TotalValidos+=1
            elif k== "30\n":
                Amoedo+=1
                Total+=1
                TotalValidos+=1
            elif k== "12\n":
                Ciro+=1
                Total+=1
                TotalValidos+=1
            elif k== "13\n":
                Haddad+=1
                Total+=1
                TotalValidos+=1
            elif k== "45\n":
                Alckimin+=1
                Total+=1
                TotalValidos+=1
            elif k== "19\n":
                Alvaro+=1
                Total+=1
                TotalValidos+=1
            elif k== "50\n":
                Boulos+=1
                Total+=1
                TotalValidos+=1
            elif k== "51\n":
                Daciolo+=1
                Total+=1
                TotalValidos+=1
            elif k== "16\n":
                Vera+=1
                Total+=1
                TotalValidos+=1
            elif k== "18\n":
                Marina+=1
                Total+=1
                TotalValidos+=1
            elif k== "15\n":
                Meirelles+=1
                Total+=1
                TotalValidos+=1
            elif k== "27\n":
                Eymael+=1
                Total+=1
                TotalValidos+=1
            elif k== "54\n":
                Goulart+=1
                Total+=1
                TotalValidos+=1
            elif k== "0\n":
                Branco +=1
                Total+=1
            else:
                Nulo+=1
                Total+1
        os.system('cls')
        print("Alvaro Dias: ",Alvaro)
        print("Cabo Daciolo: ",Daciolo)
        print("Ciro Gomes: ",Ciro)
        print("Eymael: ",Eymael)
        print("Fernando Haddad: ",Haddad)
        print("Geraldo Alckmin: ",Alckimin)
        print("Guilherme Boulos: ",Boulos)
        print("Henrique Meirelles: ",Meirelles)
        print("Jair Bolsonaro: ",Bolsonaro)
        print("João Amoêdo: ",Amoedo)
        print("Marina Silva: ",Marina)
        print("Vera: ",Vera)
        print("Total Votos: ",Total)
        print("Total Votos Válidos: ",TotalValidos)
        print("Brancos: ",Branco)
        print("Nulos: ",Nulo)


   elif menu == 9:
                g = 0
                for k in eleitores:
                        if k[2] == "True":
                                g += 1
                print("O número de eleitores que já votaram é : %s"%g)

   elif menu == 10:
                g = 0
                for k in eleitores:
                        if k[2] == "False":
                                g += 1
                print("O número de eleitores que não votaram é : %s"%g)


   elif menu == 11:
            print("Até logo!")
            break
         
      
   
      
         


   


       



