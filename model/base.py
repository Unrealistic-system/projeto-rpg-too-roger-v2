'''
Aqui ficam algumas funções usadas no jogo:
'''
import os 

def limpar_terminal():
    '''Função para limpar o terminal, funciona tanto em windows como em mac:'''
    os.system('cls' if os.name == 'nt' else 'clear')# 'nt': Windows, 'posix': Linux/MacOS

def aumenta_porcentagem(valor_original, aumento):
    '''
    Calcular aumento de porcentagem em cima de um valor:

    Args:
        valor_original (int, float): valor.
        aumento (int, float): porcentagem de aumento.

    Returns:
        float: valor + porcentagem.
    '''
    return valor_original + (valor_original * aumento / 100)

def diminui_porcentagem(valor_original, diminuicao):
    '''
    Calcular desconto de porcentagem em cima de um valor:

    Args:
        valor_original (int, float): valor.
        diminuicao (int, float): porcentagem de redução.

    Returns:
        float: valor - porcentagem.
    '''
    return valor_original - (valor_original * diminuicao / 100)

def pausa():
    '''função para pausar o terminal e exigir pressionamento de tecla:'''
    os.system('pause')

def mostrar_lista(lista_origem: list, texto_saida = "Lista", iniciar_em = 0):
    '''
    funcão que retorna os itens de uma lista com o título:

    Args:
        lista_origem (list): uma lista de qualquer tipo.
        texto_saida (str): Título que vai ser exibido antes, default "Lista".
        iniciar_em (int): por onde vai começar a contar, default 0.

    Returns:
        str: título seguido da lista.
    '''
    if len(lista_origem) == 0:
        return f"{texto_saida}: Vazio(a)"
    msg = f"\n{texto_saida}:\n"
    for i, valor in enumerate(lista_origem, iniciar_em):
        msg += f"{i} - {valor}\n"
    return msg