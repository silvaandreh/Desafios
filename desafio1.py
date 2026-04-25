import os
import math

def limpar_tela():
    os.system('cls' if os.name=='nt' else 'clear')

def calcular_garrafas(qtd_ml, pessoas):
    litros = (qtd_ml*pessoas)/1000
    return math.ceil(litros/2)

def calcular_total(qtd_ml, pessoas):
    return (qtd_ml*pessoas)/1000

def main ():
    seguir = "S"
    while seguir == "S":
        limpar_tela()
        pessoas = int(input("Quantas pessoas vão participar?"))
        qtd_ml = int(input("Quantos ml cada pessoa consome?"))
        print(f'Quantidade de pessoas: {(pessoas)}')
        print(f'consumo por pessoa: {(qtd_ml)} \n')
        print(f'Total em ml: {(qtd_ml*pessoas)} ml')
        total_ml = calcular_total(qtd_ml, pessoas)
        print(f'Total em litros: {total_ml:.2f} L')
        qtd_garrafas = calcular_garrafas(qtd_ml, pessoas)
        print(f'Total de garrafas de 2L: {qtd_garrafas} garrafas')
        seguir = input("Deseja prosseguir?(S/N)").strip().upper()

main ()