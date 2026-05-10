from model.missao import Missao
from model.personagem import Personagem
from model.Missao_coleta import MissaoColeta
from model.Missao_combate import MissaoCombate
from model.Missao_exploracao import MisssaoExploracao
from model.Item import Item
from model.enums import Tipo_item
from model.geral import *
from tkinter import messagebox

#help(mostrar_lista) # teste de documentação
#pausa()

# criar listas de missões, personagens e itens para o jogo
lista_Personagens: list[Personagem] = []
lista_Missoes: list[Missao] = []
lista_itens: list[Item] = []

#itens default
lista_itens.append(Item("Espada de Edward", "espada que pertencia a um antigo pirata", 40, Tipo_item.ARMA))
lista_itens.append(Item("Capacete de Comerciante", "capacete formal usado por comerciantes", 10, Tipo_item.VESTIMENTA))
lista_itens.append(Item("Espelho Miraculoso", "espelho que aumenta a vida de quem o equipa", 30, Tipo_item.UTILITARIO))

#missoes default
lista_Missoes.append(MissaoColeta("Coletar maças", "Colete maças pela montanha de olindo", 40,"Macas", 10))
lista_Missoes.append(MissaoCombate("Derrotar Goblin", "Derrote os goblins da arena", 40, 50,"Goblin"))

# personagens default
lista_Personagens.append(Personagem("Chitãozinho"))
lista_Personagens.append(Personagem("Xororó"))
lista_Personagens.append(Personagem("Zé Ramalho"))

menu = 1
while menu != 0:
    limpar_terminal()
    menu = int(input(
        f"0 - sair\n"
        f"1 - Criar Personagem\n"
        f"2 - listar e detalhar Personagens\n"
        f"3 - listar e atribuir Missões\n"
        f"4 - listar e adicionar Itens à inventário\n"
        f"5 - Jogar Missão\n"
        f"Escolha: "
    ))
    match menu:
        case 0:
            print("\nSaindo...\n")
        case 1:
            lista_Personagens.append(Personagem(input("Digite o nome do novo personagem a ser criado: ")))
        case 2:
           print(mostrar_lista(lista_Personagens, "Personagens", 1)) # mostra a lista de personagens, conta a partir de 1
           sel = int(input("Digite um numero da lista para detalhar, 0 para sair: "))# input para detalhar
           if sel == 0:
               continue
           try:
               print(Personagem.exibir_dados(lista_Personagens[sel-1]))
           except IndexError:
               print("Não encontrado personagem correspondente ao número digitado")
        case 3:
            print(mostrar_lista(lista_Missoes, "Missões", 1))
            pausa()
            messagebox.askquestion("Atribuição", "Atribuir Misão a algum personagem?")
        case 4:
            print(mostrar_lista(lista_itens, "Itens Disponíveis", 1))
        case 5:
            pass
        case _:
            print(f"Opção {menu} inválida! tente novamente")
    pausa()

'''
print(ps.mostrar_itens_equipados())
print(ps.equipar_itens())

'''
