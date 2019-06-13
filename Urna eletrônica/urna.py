import PyGravador
q = True
esta = True
eleitores = PyGravador.recuperaEleitores()
candidatos = PyGravador.recuperaCandidatos()


while q == True:
        p = True
        print("-------------------")
        print("--------URNA-------")
        print("-------------------")
        print("(1)Cadastro de eleitores                          (2)Listar eleitores ")
        print("(3)Alterar dados do eleitor                       (4)Cadastrar candidato")
        print("(5)Listar Candidatos                              (6)Alterar dados candidato")
        print("(7)Registar voto                                  (8)Consultar votos por candidato")
        print("(9)Consultar numero de eleitores que ja votaram   (10)Consultar numero de eleitores que não votaram")
        print("(11) sair")
        print("\n" )
        x = input("Escolha uma opção\n").upper()
        print("\n"*50)
        if x == "1":
                ç = True
                y = input("Digite o nome e o número do eleitor separados por ';' \n").split(";")
                if len(y) == 2 :
                        for k in eleitores:
                                if k[1] == y[1]:
                                        ç = False
                                        print("Eleitor já cadastrado")
                else:
                        print("Dados incorretos")
                        ç = False
               
                
                if ç == True :
                        y.append("False")
                        eleitores.append(y)
                        print("Eleitor cadastrado com sucesso")

                                        
                                
        elif x == "2":
                print("Lista de eleitores:")
                for k in eleitores:
                        print("Nome : %s ; Número : %s "%(k[0],k[1]))
                print("Total de %i eleitores"%len(eleitores))
                
        elif x == "3":
                print("(1) Para alterar o nome ")
                print("(2) Para alterar o número")
                m = input()
                if m == "1" :
                        numero = input("Digite o numero do eleitor\n")
                        n = input("Digite o novo nome\n")
                        função.alterarNomeEleit(eleitores,numero,n)
                elif m == "2":
                        nome = input("Digite o numero do eleitor\n")
                        n = input("Digite o novo número\n")
                        l = False
                        for k in eleitores:
                                if k[1] == n:
                                        l = True
                        if l == False:
                                função.alterarNumeroEleit(eleitores,nome,n)
                        else:
                                print("Número já cadastrado")

        
                        
                else:
                        print("Opção inválida")
        elif x == "4" :
                y = input("Digite o nome do candidato e o número separados por ';'\n").split(";")
                ç = True
                if len(y) == 2 :        
                        for k in candidatos:
                                if k[1] == k :
                                        print("Candidato já cadastrado")
                                        ç = False
                else:
                        print("Dados incorretos")
                        ç = False
                if ç == True:
                        y.append("0")
                        y.append("\n")
                        candidatos.append(y)
                        
                        print("Candidato cadastrado com sucesso")

        elif x == "5":
                print("Lista de candidatos")
                for k in candidatos:
                        print("Nome : %s ; Número : %s"%(k[0],k[1]))
                print("Total de %i candidato(s)"%len(candidatos))

        elif x == "6":
                print("(1) Para alerar nome ")
                print("(2) Para alterar número")
                m = input()
                if m == "1":
                      n = input("Digite o numero do candidato\n")
                      nome = input("Digite o novo nome\n")
                      função.alterarNomeCandidato(candidatos,n,nome)
                if m == "2":
                        n = input("Digite o número do candidato\n")
                        numero = input("Digite o novo número\n")
                        l = False
                        for k in candidatos:
                                if k[1] == numero:
                                        l = True
                        if l == False:
                                função.alterarNumeroCandidato(candidatos,n,numero)
                        else:
                                print("Número já cadastrado")
        elif x == "7":
                v = input("Digite o seu número\n")
                for k in range(len(eleitores)):
                        if eleitores[k][1] == v :                                
                                if eleitores[k][2] == "False":
                                        c = input("Digite o número do seu candidato\n")
                                        for k in range(len(candidatos)):
                                                if candidatos[k][1] == c :
                                                        print(função.registraVoto(candidatos,v,c,eleitores))

                                else:
                                        print("Você já votou")
                        else:
                                print("sdognd")

        elif x == "8":
                
                for k in candidatos :
                        print(" O candidato %s recebeu %s votos"%(k[0],k[2]))

        elif x == "9":
                g = 0
                for k in eleitores:
                        if k[2] == "True":
                                g += 1
                print("O número de eleitores que já votaram é : %s"%g)

        elif x == "10":
                g = 0
                for k in eleitores:
                        if k[2] == "False":
                                g += 1
                print("O número de eleitores que não votaram é : %s"%g)
                                

        elif x == "11":
                if eleitores !=  [ ]:
                        função.gravaEleitores(eleitores)
                if candidatos != [ ]:
                        função.gravaCandidatos(candidatos)
                break
