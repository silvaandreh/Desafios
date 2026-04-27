import os

lista = [10,20,30,40,50]

def limparTela():
    os.system('cls' if os.name=='nt' else 'clear')

def adicionaNumero(num):
    lista.append(num)
    print(f"Número {num} adicionado com sucesso")
    return

def removerNumero(num):
    if num in lista:
        lista.remove(num)
        print(f"Número {num} removido com sucesso")
        return
    else:
        print('Número não encontrado na lista')
        return
    
def mostrarMenu():
    print("*=============MENU=============*")
    print("1- Adicionar Número na lista")
    print("2- Remover número da lista")
    print("3- Visualizar lista")
    print("4- Sair")


def main ():
    limparTela()
    while True:
        mostrarMenu()
        opcao = int(input('Digite uma opção: '))
        if opcao == 1:
            limparTela()
            num = int(input("Digite um número para ser adicionado: "))
            adicionaNumero(num)
        elif opcao == 2:
            limparTela()
            num = int(input("Digite um número para ser removido: "))
            removerNumero(num)
        elif opcao == 3:
            limparTela()
            for i in lista:
                print(i)
        else:
            limparTela()
            print("Obrigado por utilizar nossa ferramenta")
            break

main ()