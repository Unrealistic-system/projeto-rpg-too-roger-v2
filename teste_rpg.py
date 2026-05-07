from model.missao import Missao
from model.personagem import Personagem
from model.Missao_coleta import MissaoColeta
from model.Missao_combate import MissaoCombate
from model.Missao_exploracao import MisssaoExploracao
from model.item import Item
from model.enums import Tipo_item
from model.geral import *

msco = MissaoColeta("Coletar maças", "Colete maças pela montanha de olindo", 40,"Macas", 10)
msco2 = MissaoColeta("Coletar maças", "Colete maças pela montanha de olindo", 40,"Macas", 10)
mscomb1 = MissaoCombate("Derrotar Goblin", "Derrote os goblins da arena", 40, 50,"Goblin")
item_1 = Item("Espada de Edward", "espada que pertencia a um antigo pirata", 40, Tipo_item.ARMA)
item_2 = Item("Capacete de Comerciante", "capacete formal usado por comerciantes", 10, Tipo_item.VESTIMENTA)
item_3 = Item("Espelho Miraculoso", "espelho que aumenta a vida de quem o equipa", 30, Tipo_item.UTILITARIO)

ps = Personagem("Milena")

menu = 1
while menu != 0:
    limpar_terminal()
    menu = int(input(
        f"0 - sair\n"
        f"1 - Criar Personagem\n"
        f"2 - Mostrar Personagem\n"
        f"3 - Criar Missão\n"
        f"4 - Mostrar missão\n"
        f"5 - Atribuir Missão\n"
        f"6 - Concluir Misão\n"
        f"7 - Equipar Personagem\n"
        f"8 - Mostrar Inventário\n"
        f"9 - Mostrar Missões\n"
        f"Escolha: "
    ))
    match menu:
        case 0:
            print("\nSaindo...\n")
        case 1:
            print("\nNAO IMPLEMENTADO\n")
        case 2:
           print(ps.exibir_dados())
        case 3:
            pass
        case 4:
            pass
        case 5:
            print(ps.add_missao(msco))
            print(ps.add_missao(msco2))
            print(ps.add_missao(mscomb1))
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



