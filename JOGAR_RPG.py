from model.missao import Missao
from model.personagem import Personagem
from model.Missao_coleta import MissaoColeta
from model.Missao_combate import MissaoCombate
from model.Missao_exploracao import MisssaoExploracao
from model.Item import Item
from model.enums import Tipo_item
from model.geral import *
from tkinter import messagebox

# criar listas de missões e personagens para o jogo
lista_Personagens: list[Personagem] = []
lista_Missoes: list[Missao] = []


#msco = MissaoColeta("Coletar maças", "Colete maças pela montanha de olindo", 40,"Macas", 10)
#msco2 = MissaoColeta("Coletar maças", "Colete maças pela montanha de olindo", 40,"Macas", 10)
#mscomb1 = MissaoCombate("Derrotar Goblin", "Derrote os goblins da arena", 40, 50,"Goblin")
item_1 = Item("Espada de Edward", "espada que pertencia a um antigo pirata", 40, Tipo_item.ARMA)
item_2 = Item("Capacete de Comerciante", "capacete formal usado por comerciantes", 10, Tipo_item.VESTIMENTA)
item_3 = Item("Espelho Miraculoso", "espelho que aumenta a vida de quem o equipa", 30, Tipo_item.UTILITARIO)

lista_Missoes.append(MissaoColeta("Coletar maças", "Colete maças pela montanha de olindo", 40,"Macas", 10))
lista_Missoes.append(MissaoCombate("Derrotar Goblin", "Derrote os goblins da arena", 40, 50,"Goblin"))

ps = Personagem("Milena")

menu = 1
while menu != 0:
    limpar_terminal()
    menu = int(input(
        f"0 - sair\n"
        f"1 - Criar Personagem\n"
        f"2 - Mostrar Personagens\n"
        f"3 - listar Missões\n"
        f"4 - Mostrar Inventário\n"
        f"Escolha: "
    ))
    match menu:
        case 0:
            print("\nSaindo...\n")
        case 1:
            nome_personagem = input("Digite o nome do novo personagem a ser criado: ")
            novo_personagem = Personagem(nome_personagem)
            lista_Personagens.append(novo_personagem)
        case 2:
           msg = f"Personagens:\n"
           for i, valor in enumerate(lista_Personagens):
                msg += f"{i+1} - {valor}\n"
           print(msg)
        case 3:
            msg = f"Misões Disponíveis:\n"
            for i, valor in enumerate(lista_Missoes):
                    msg += f"{i+1} - {valor}\n"
            print(msg)
            pausa()
            messagebox.askquestion("diálogo", "Atribuir Misão a algum personagem?")
        case 4:
            pass
        case 6:
            try:
                ps.concluir_missao(msco, 9)
                ps.concluir_missao(mscomb1, 50)
            except ValueError as e:
                print(e)
        case 7:
            print(ps.add_item(item_1))
            print(ps.add_item(item_2))
            print(ps.add_item(item_3))
            print(ps.equipar_itens())
            print(ps.mostrar_itens_equipados())
        case 8:
            print(ps.mostrar_inventario())
        case 9:
            print(ps.listar_Missao())
        case _:
            print(f"Opção {menu} inválida! tente novamente")
    pausa()



