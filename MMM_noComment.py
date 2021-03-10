from os import system

while(True):
    
    system('cls')

    print("\n\033[35m▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣\033[m\n")
    arquivo = str(input("\033[1mDigite o nome do arquivo (txt):\033[m "))
    print("\n\033[35m▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣\033[m\n")

    if (not ".txt" in arquivo):

        arquivo = arquivo + ".txt"

    valores = []

    try:

        with open(arquivo, "r") as entrada:

            for valor in entrada:

                valor = valor.split(" ")
                
                if (type(valor) == list):

                    for i in valor:

                        valores.append(float(i))

                else: valores.append(float(valor))

            entrada.close()

            raiz = 0
            conta = 0

            while(raiz**2 < len(valores)):

                raiz+=1


            print("\n\033[1;35m       Valores do arquivo:\033[m\n")

            while(conta < len(valores)):

                print("\033[1;35m   |\033[m", end = " ")
                for i in range(raiz):
                    if(conta==len(valores)):

                        break

                    print("%.2f" % valores[conta], end = "  ")
                    conta+=1

                print("\033[1;35m|\033[m\n")

            print("\n\033[35m▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣\033[m")
            print("\033[33m▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣\033[m")

            print("""\033[1;33m
______________________________________________
|                 /                          |
|    |\    /|  _____   ____                  |
|    | \  / | |       |    \   0    /\       |
|    |  \/  | |____   |     |  |   /  \      |
|    |      | |       |     |  |  /----\     |
|    |      | |_____  |____/   | /      \    |
|____________________________________________|
            \033[m""")

            soma = 0
            quantidade = len(valores)

            for valor in valores:

                soma = soma + valor

            media = soma / quantidade

            print("\n  \033[1;33mMédia\033[m é a soma de todos os valores de um conjunto de dados\n  dividido pela quantidade de dados.")
            print("\n  Somatória = %.2f" % soma)
            print("  Quantidade = %i" % quantidade)
            print("""
            %.2f                  
            ▬▬▬▬▬▬▬▬ =  \033[1;33m%.2f\033[m = Média
                %i
            """ % (soma, media, quantidade))

            print("\033[33m▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣\033[m")
            print("\033[31m▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣\033[m")


            print("""\033[1;31m
______________________________________________________________
|                                                            |
|             |\    /|  _____   ____                         |
|             | \  / | |     | |    \     /\                 |
|             |  \/  | |     | |     |   /  \                |
|             |      | |     | |     |  /----\               |
|             |      | |_____| |____/  /      \              |
|____________________________________________________________|
            \033[m""")

            print("\n\033[1;31mModa\033[m é o valor mais frequente em um conjunto de dados.")

            moda = []
            repeticoes = []

            classe = ["AMODAL", "MODAL", "BIMODAL", "MULTIMODAL"]
            indice = 0

            maioresRepeticoes = []
            modas = []
            
            multimodal = []
            united = []

            valores.sort()

            for i in range(quantidade):

                conta = valores.count(valores[i])
                repeticoes.append(conta)
                moda.append(valores[i])

            if(sum(repeticoes)/quantidade == 1):

                indice = 0

                print("\nA classificação desse conjunto de dados é: \033[1;31m%s\033[m." % classe[indice])
                print("Quando não há repetições no conjunto de dados.")

            elif(sum(repeticoes)/quantidade == max(repeticoes)):

                indice = 0

                print("\nA classificação desse conjunto de dados é: \033[1;31m%s\033[m." % classe[indice])
                print("Quando não há repetições no conjunto de dados.")

            else:
                
                for i in range(3):

                    maior = max(repeticoes)
                    modinha = repeticoes.index(maior)
                    maioresRepeticoes.append(maior)
                    modas.append(moda[modinha])
                    del moda [modinha : modinha + maior]
                    del repeticoes [modinha : modinha + maior]

                if (max(maioresRepeticoes)==min(maioresRepeticoes)):

                    indice = 3
                    for i in valores:

                        if(not i in united):

                            united.append(i)

                    for j in united:

                        if(valores.count(j)>=max(maioresRepeticoes)):
                            multimodal.append(j)
                            
                    print("\nA classificação desse conjunto de dados é: \033[1;31m%s\033[m." % classe[indice])
                    print("Quando há mais de dois valores que se repetem em mesma frequência no\nconjunto de dados.")
                    print("\nValores que se repetem: \033[1;31m%a\033[m, que se repetem \033[1;31m%i\033[m vezes." % (multimodal, max(maioresRepeticoes)))

                else: 
                    
                    del modas[maioresRepeticoes.index(min(maioresRepeticoes))]
                    del maioresRepeticoes[maioresRepeticoes.index(min(maioresRepeticoes))]
                    if (max(maioresRepeticoes)==min(maioresRepeticoes)):
                        
                        indice = 2

                        print("\nA classificação desse conjunto de dados é: \033[1;31m%s\033[m." % classe[indice])
                        print("Quando há dois valores que se repetem em mesma frequência no\nconjunto de dados.")
                        print("\nValores que se repetem: \033[1;31m%.2f\033[m e \033[1;31m%.2f\033[m, que se repetem \033[1;31m%i\033[m vezes." % (modas[0], modas[1], max(maioresRepeticoes)))

                    else:

                        indice = 1
                        print("\nA classificação desse conjunto de dados é: \033[1;31m%s\033[m." % classe[indice])
                        print("Quando há um valor que se repete em maior frequência no\nconjunto de dados.")
                        print("\nO valor que mais se repete é: \033[1;31m%.2f\033[m, que se repete \033[1;31m%i\033[m vezes." % (modas[maioresRepeticoes.index(max(maioresRepeticoes))], max(maioresRepeticoes)))


            print("\n\033[31m▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣\033[m")
            print("\033[36m▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣\033[m")

            print("""\033[1;36m
______________________________________________________________
|                                                            |
|    |\    /|  _____   ____                                  |
|    | \  / | |       |    \   0    /\    |\   |    /\       |
|    |  \/  | |____   |     |  |   /  \   | \  |   /  \      |
|    |      | |       |     |  |  /----\  |  \ |  /----\     |
|    |      | |_____  |____/   | /      \ |   \| /      \    |
|____________________________________________________________|
            \033[m""")

            porcent = "%"

            print("A \033[1;36mMediana\033[m é o valor central em um conjunto de dados.\n")
            print("O \033[1;36m1° Quartil\033[m é o valor aos 25%s da amostra ordenada.\n" % porcent)
            print("O \033[1;36m3° Quartil\033[m é o valor aos 75%s da amostra ordenada.\n" % porcent)

            if (quantidade%2 == 0):

                posicaoSQ = int(quantidade/2)-1
                segundoQuartil = (valores[posicaoSQ] + valores[posicaoSQ+1]) /2

                primeiroQuartil = valores[0:posicaoSQ+1]
                terceiroQuartil = valores[posicaoSQ+1:quantidade]
                
                if (len(primeiroQuartil)%2==0):

                    posicaoPQ = int(len(primeiroQuartil)/2)-1
                    primeiroQuartil = (primeiroQuartil[posicaoPQ] + primeiroQuartil[posicaoPQ+1])/2
                    posicaoTQ = posicaoPQ+len(terceiroQuartil)+1
                    terceiroQuartil = (terceiroQuartil[posicaoPQ] + terceiroQuartil[posicaoPQ+1])/2

                    valores.insert(posicaoPQ+1, 0) 
                    valores.insert(posicaoTQ+1, 0)  
                    valores.insert(posicaoSQ+2, 0)   

                    for i in range(len(valores)):

                        if(i==posicaoPQ+1):

                            print("\033[1;36m ─────── %.2f 1° Quartil\033[m" % primeiroQuartil)

                        elif(i==posicaoSQ+2):

                            print("\033[1;36m ─────── %.2f 2° Quartil\033[m" % segundoQuartil)

                        elif(i==posicaoTQ+2):

                            print("\033[1;36m ─────── %.2f 3° Quartil\033[m" % terceiroQuartil)

                        else: print("║%.2f" % valores[i])

                else:

                    posicaoPQ = int((len(primeiroQuartil)+1)/2)-1
                    primeiroQuartil = primeiroQuartil[posicaoPQ]
                    posicaoTQ = posicaoPQ+len(terceiroQuartil)+1
                    terceiroQuartil = terceiroQuartil[posicaoPQ]

                    valores.insert(posicaoSQ+1, 0)

                    for i in range(len(valores)):

                        if(i==posicaoPQ):

                            print("\033[1;36m╠%.2f ─── 1° Quartil\033[m" % valores[i])

                        elif(i==posicaoSQ+1):

                            print("\033[1;36m ─────── %.2f 2° Quartil\033[m" % segundoQuartil)

                        elif(i==posicaoTQ):

                            print("\033[1;36m╠%.2f ─── 3° Quartil\033[m" % valores[i])

                        else: print("║%.2f" % valores[i])

                
            else:

                posicaoSQ = int((quantidade+1)/2)-1
                segundoQuartil = valores[posicaoSQ]

                primeiroQuartil = valores[0:posicaoSQ]
                terceiroQuartil = valores[posicaoSQ+1:quantidade]
                
                if (len(primeiroQuartil)%2==0):

                    posicaoPQ = int(len(primeiroQuartil)/2)-1
                    primeiroQuartil = (primeiroQuartil[posicaoPQ] + primeiroQuartil[posicaoPQ+1])/2
                    posicaoTQ = posicaoPQ+len(terceiroQuartil)+2
                    terceiroQuartil = (terceiroQuartil[posicaoPQ] + terceiroQuartil[posicaoPQ+1])/2

                    valores.insert(posicaoPQ+1, 0)
                    valores.insert(posicaoTQ+1, 0)

                    for i in range(len(valores)):

                        if(i==posicaoPQ+1):

                            print("\033[1;36m ─────── %.2f 1° Quartil\033[m" % primeiroQuartil)

                        elif(i==posicaoSQ+1):

                            print("\033[1;36m╠%.2f ─── 2° Quartil\033[m" % valores[i])

                        elif(i==posicaoTQ+1):

                            print("\033[1;36m ─────── %.2f 3° Quartil\033[m" % terceiroQuartil)

                        else: print("║%.2f" % valores[i])
                
                else:

                    posicaoPQ = int((len(primeiroQuartil)+1)/2)-1
                    primeiroQuartil = primeiroQuartil[posicaoPQ]
                    posicaoTQ = posicaoPQ+len(terceiroQuartil)+1
                    terceiroQuartil = terceiroQuartil[posicaoPQ]

                    for i in range(len(valores)):

                        if(i==posicaoPQ):

                            print("\033[1;36m╠%.2f ─── 1° Quartil\033[m" % valores[i])

                        elif(i==posicaoSQ):

                            print("\033[1;36m╠%.2f ─── 2° Quartil\033[m" % valores[i])

                        elif(i==posicaoTQ):

                            print("\033[1;36m╠%.2f ─── 3° Quartil\033[m" % valores[i])

                        else: print("║%.2f" % valores[i])

            print("\n\033[36m▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣\033[m\n")


            print("\033[1;42m[1]\033[m - \033[32mContinuar\033[m")
            print("\033[1;41m[2]\033[m - \033[31mSair\033[m\n")

            resposta = int(input())

            if(resposta==2):

                break

            elif(resposta==1):
            
                system('cls')

            else:

                print("\n\033[35mEste valor não é válido!\033[m\n")
                break

    except FileNotFoundError:

        print("\n\033[1;35mArquivo não encontrado...\033[m\n")
        print("\033[1;42m[1]\033[m - \033[32mTentar novamente\033[m ")
        print("\033[1;41m[2]\033[m - \033[31mSair\033[m\n")

        resposta = int(input())
 
        if(resposta==2):

            break

        elif(resposta==1):
            
            system('cls')

        else:

            print("\n\033[35mEste valor não é válido!\033[m\n")
            break