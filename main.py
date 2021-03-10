from os import system
import modfunctions

# Laço de repetição infinito que servirá como chave de controle para fechar ou manter aberto o programa ao término de execução.
while(True):
    
    system('cls')
    
    # Entrada do nome do Arquivo.
    print("\n\033[35m▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣\033[m\n")
    arquivo = str(input("\033[1mDigite o nome do arquivo (txt):\033[m "))
    print("\n\033[35m▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣\033[m\n")

    # Identifica se na entrada o usuário digitou o nome do arquivo com ou sem extensão e corrige.
    if (not ".txt" in arquivo):

        arquivo = arquivo + ".txt"

    found, valores = modfunctions.entrada_de_dados(arquivo)

    if(found):

        modfunctions.rolDeDados(valores)
        modfunctions.media(valores)
        modfunctions.moda(valores)
        modfunctions.mediana(valores)

        # Verifica se o usuário quer continuar no programa ou sair.
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

    else:
        
        resposta = valores

        if(resposta==2):

            break

        elif(resposta==1):
                    
            system('cls')

        else:

            print("\n\033[35mEste valor não é válido!\033[m\n")
            break