import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.personagem import Personagem
from model.FactotyMissao import factoryMissao
from model.Item import Item, Tipo_item
from model.base import *
from model.missao import Missao
#from tkinter import messagebox

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

def preparar_para_missao(personagem):
    limpar_terminal()
    try:
        print(personagem.mostrar_inventario())
        indice = int(input(f"Digite o número do item a ser equipado: "))
        item_equipar = personagem.inventario[indice-1]
        print(personagem.equipar_item(item_equipar))
    except IndexError:
        return f"item digitado não existe!"
    except ValueError:
        return f"entrada digitada inválida!"
    except TypeError:
        return f"entrada digitada inválida!"

#missoes default 
'''
Argumentos: tipo_missao:str, nome:str, descricao:str, recompensa
**kwargs:
        combate: "tipo_inimigo", "qnt_inimigos"
        coleta: "nome_item", "quantidade"
        exploração: "regiao_destino", "distancia_em_km", "tempo_limite"
'''
lista_Missoes.append(factoryMissao.criar_missao(tipo_missao="coleta",nome="Coletar maças", descricao="Colete maças pela montanha de olindo", recompensa=40, quantidade= 10, tipo_item= "maças"))
#lista_Missoes.append(MissaoCombate("Derrotar Goblin", "Derrote os goblins da arena", 40, 50,"Goblin"))

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
        f"5 - Completar Missão\n"
        f"Escolha: "
    ))

    if menu == 1:
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
    elif isinstance(personagem_padrao, Personagem):
        try:
            match menu:
                case 0:
                    pass
                case 2:

                    print(personagem_padrao.exibir_dados())
                    print(personagem_padrao.listar_Missao())
                    print(personagem_padrao.mostrar_inventario())

                case 3:

                    print(mostrar_lista(lista_Missoes, "Missões Disponíveis", 1))
                    id_missao = int(input("Digite um numero da lista para atibuir, 0 para sair: "))
                    if id_missao == 0:
                        continue
                    preparar_para_missao(personagem_padrao)
                    print(personagem_padrao.add_missao(lista_Missoes[id_missao-1]))# -1 para pegar o indice correto

                case 4:

                    print(mostrar_lista(lista_itens, "Itens Disponíveis", 1))
                    id_item = int(input("Digite um numero da lista para adicionar, 0 para sair: "))
                    if id_item == 0:
                        continue
                    print(personagem_padrao.add_item(lista_itens[id_item-1]))# -1 para pegar o indice correto

                case 5:
                    
                    if len(personagem_padrao.missoes) > 0:
                        print(personagem_padrao.listar_Missao())
                        sel = int(input("Digite o numero da missão para escolher, 0 para sair: "))
                        if sel == 0:
                            continue
                        valor_obtido = int(input("digite a quantidade de itens/area/inimigos que você derrotou/completou: "))
                        print(personagem_padrao.concluir_missao(personagem_padrao.missoes[sel-1], valor_obtido))
                    else:
                        print("Nenhuma misão para concluir!!!")
                    
                case _:
                    print(f"Opção {menu} inválida! tente novamente")
        except IndexError:
            print("Não encontrado item correspondente ao número digitado")
        except ValueError:
            print("Entrada de dados inválida!!")
        except:
            print("Erro!!")   
    elif menu != 0 and not isinstance(personagem_padrao, Personagem):
        print("Você deve criar ou escolher um personagem primeiro")
    else:
        print("\nSaindo...\n")
    pausa()
