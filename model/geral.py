'''
Aqui ficam funções usadas em vários lugares:
'''
import os 

def limpar_terminal():
    '''
    Função para limpar o terminal, funciona tanto em windows como em mac:
    '''
    os.system('cls' if os.name == 'nt' else 'clear')# 'nt' é Windows, 'posix' é Linux/MacOS

def aumenta_porcentagem(valor_original, aumento):
    '''
    Calcular aumento de porcentagem em cima de um valor:
    '''
    return valor_original + (valor_original * aumento / 100)

def diminui_porcentagem(valor_original, diminuicao):
    '''
    Calcular desconto de porcentagem em cima de um valor:
    '''
    return valor_original - (valor_original * diminuicao / 100)

def pausa():
    os.system('pause')