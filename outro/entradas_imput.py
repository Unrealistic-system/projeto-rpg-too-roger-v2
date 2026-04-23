from model.missao import Missao
from personagem import Personagem

def entrada_missao() -> Missao:
    while True:
        try:
            nome = input(f"{'-'*10}\nDigite o nome da Misão: ")
            desc = input(f"{'-'*10}\nDigite a descrição: ")
            rec = int(input(f"{'-'*10}\nDigite a recompensa: "))
            ''' # remover para aceitar somente tipo do enum
            st = input(f"{'-'*10}\nDigite o status:\ntipos: PENDENTE, EM ANDAMENTO OU CONCLUIDA\nou pule com enter: ")
            if not st:
                missao_criada = Missao(nome, desc, rec)
            else:
                missao_criada = Missao(nome, desc, rec, st) # type: ignore
                # O type:ignore 
            '''
            missao_criada = Missao(nome, desc, rec)
            return missao_criada
        except TypeError as e:
            print(f"{'+'*10}\nErro de Digitação: {e}\n{'+'*10}")
        except ValueError as e:
            print(f"{'+'*10}\nValor Inválido: {e}\n{'+'*10}")
        except Exception as e:
            print(f"{'+'*10}\nERRO: {e}\n{'+'*10}")

def entrada_personagem() -> Personagem:
    while True:
        try:
            nome = input(f"{'-'*10}\nDigite o nome do personagem: ")
            criar_personagem = Personagem(nome)
            return criar_personagem
        except TypeError as e:
            print(f"{'+'*10}\nErro de Digitação: {e}\n{'+'*10}")
        except ValueError as e:
            print(f"{'+'*10}\nValor Inválido: {e}\n{'+'*10}")
        except Exception as e:
            print(f"{'+'*10}\nERRO: {e}\n{'+'*10}")