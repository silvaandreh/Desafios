import os

produtos = ["Hamburguer", "Pizza", "Refrigerante"]
precos = {"1": 15.00 ,"2": 40.00,"3": 8.00}
pedido = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("*=============MENU=============*")
    print("||1 - Hambúrguer → R$ 15.00   ||")
    print("||2 - Pizza → R$ 40.00        ||")
    print("||3 - Refrigerante → R$ 8.00  ||")
    print("||4 - Sair                    ||")
    print("*==============================*")

def salvar_pedido(pedido, opcao, quantidade):
    pedido.append({
        "item": opcao,
        "quantidade": quantidade
    })

def calcular_total(pedido):
    total = 0
    for p in pedido:
        preco = precos[p['item']]
        subtotal = preco * p['quantidade']
        total += subtotal
    return total

def main():
    seguir = "S"
    while seguir == "S":
        limpar_tela()
        mostrar_menu()
        opcao = input(("Digite uma opção:"))
        if opcao not in ('1', '2', '3', '4'):
            print('Opção inválida')
            continue
        elif (opcao == '4'):
            break
        else:
            quantidade = int(input(("Digite a quantidade:")))
            salvar_pedido(pedido, opcao, quantidade)
            print (f"Subtotal atual: R$ {calcular_total(pedido):.2f}")
            seguir = input("Mais algum pedido? (S/N)").strip().upper()
    total_pedido = calcular_total(pedido)
    limpar_tela()
    for item in pedido:
        nome = produtos[int(item['item'])-1]
        preco = precos[item['item']]
        subtotal = preco * item['quantidade']
        print (f"{item['quantidade']}x {nome} - Valor unitário: {preco:.2f} - Subtotal: R$ {subtotal:.2f}")

    print (f'Total: R$ {total_pedido:.2f}')

main()