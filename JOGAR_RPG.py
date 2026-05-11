from model.missao import Missao
from model.personagem import Personagem
from model.Missao_coleta import MissaoColeta
from model.Missao_combate import MissaoCombate
from model.Missao_exploracao import MisssaoExploracao
from model.Item import Item
from model.enums import Tipo_item
from model.geral import *
from tkinter import messagebox
'''
help(mostrar_lista) # teste de documentação
pausa()

'''


# criar listas de missões, personagens e itens para o jogo
lista_Personagens: list[Personagem] = []
lista_Missoes: list[Missao] = []
lista_itens: list[Item] = []

#itens default
lista_itens.append(Item("Espada de Edward", "espada que pertencia a um antigo pirata", 40, Tipo_item.ARMA))
lista_itens.append(Item("Capacete de Comerciante", "capacete formal usado por comerciantes", 10, Tipo_item.VESTIMENTA))
lista_itens.append(Item("Espelho Miraculoso", "espelho que aumenta a vida de quem o equipa", 30, Tipo_item.UTILITARIO))
'''
it: Item | None = None # teste itens
print(Item.__str__(lista_itens[1]))
print(Item.__str__(it))
pausa()
'''




#missoes default
lista_Missoes.append(MissaoColeta("Coletar maças", "Colete maças pela montanha de olindo", 40,"Macas", 10))
lista_Missoes.append(MissaoCombate("Derrotar Goblin", "Derrote os goblins da arena", 40, 50,"Goblin"))

# personagens default
lista_Personagens.append(Personagem("Chitãozinho"))
lista_Personagens.append(Personagem("Xororó"))
lista_Personagens.append(Personagem("Zé Ramalho"))

menu = 1
personagem_padrao: Personagem | None = None # personagem padrao é nenhum, deve ser selecionado ou criado
while menu != 0:
    limpar_terminal()
    menu = int(input(
        f"=== ECOS DE ARCADIA ===\n"
        f"0 - sair\n"
        f"1 - Criar ou escolher Personagem\n"
        f"2 - Detalhar Personagem\n"
        f"3 - Atribuir Missões\n"
        f"4 - Adicionar Itens à inventário\n"
        f"5 - Jogar Missão\n"
        f"Escolha: "
    ))
    match menu:
        case 0:

            print("\nSaindo...\n")
            break

        case 1:

            print(mostrar_lista(lista_Personagens, "Personagens Padrão", 1))
            try:
                sel = int(input("Digite o numero do Personagem para escolher, 0 para criar: "))
                if sel == 0:
                    personagem_padrao = Personagem(input("Digite o nome do novo personagem a ser criado: "))
                    lista_Personagens.append(personagem_padrao) # util para a troca de personagem
                    print(f"Personagem {personagem_padrao} criado com sucesso!!")
                else:
                    personagem_padrao = lista_Personagens[sel-1]# atribui padrão ao personagem escolhido
                    print(f"Personagem {personagem_padrao} escolhido!!")
            except IndexError:
               print("Não encontrado Personagem correspondente ao número digitado")
            except ValueError:
                print("Entrada de dados inválida!!")

        case 2:

            if not isinstance(personagem_padrao, Personagem):
                print("Você deve criar ou escolher um personagem primeiro")
            else:
                print(Personagem.exibir_dados(personagem_padrao))
                print(personagem_padrao.listar_Missao())
                print(personagem_padrao.mostrar_inventario())

        case 3:

            print(mostrar_lista(lista_Missoes, "Missões Disponíveis", 1))
            if not isinstance(personagem_padrao, Personagem):
                print("Você deve criar ou escolher um personagem para poder atribuir Missões!!!")
            else:
                try:
                    id_missao = int(input("Digite um numero da lista para atibuir, 0 para sair: "))
                    if id_missao == 0:
                        continue
                    print(personagem_padrao.add_missao(lista_Missoes[id_missao-1]))# -1 para pegar o indice correto
                except IndexError:
                    print("Não encontrado Missão correspondente ao número digitado")
                except ValueError:
                    print("Entrada de dados inválida!!")

        case 4:

            print(mostrar_lista(lista_itens, "Itens Disponíveis", 1))
            if not isinstance(personagem_padrao, Personagem):
                print("Você deve criar ou escolher um personagem para poder adicionar itens no inventário!!!")
            else:
                try:
                    id_item = int(input("Digite um numero da lista para adicionar, 0 para sair: "))
                    if id_item == 0:
                        continue
                    print(personagem_padrao.add_item(lista_itens[id_item-1]))# -1 para pegar o indice correto
                except IndexError:
                    print("Não encontrado item correspondente ao número digitado")
                except ValueError:
                    print("Entrada de dados inválida!!")

        case 5:

            if isinstance(personagem_padrao, Personagem):
                print(personagem_padrao.listar_Missao())
            
        case _:
            print(f"Opção {menu} inválida! tente novamente")
    pausa()

'''
print(ps.mostrar_itens_equipados())
print(ps.equipar_itens())

'''
