from model.missao import *
from model.Missao_coleta import *
from model.Missao_combate import *
from model.Missao_exploracao import *

class factoryMissao():

    @staticmethod
    #def criar_missao(tipo_missao: str, nome, descricao, recompensa, valor_str: str, valor_num, tempo_limite = 50):
    def criar_missao(tipo_missao:str, nome:str, descricao:str, recompensa, **kwargs):
        
        tipo_missao = tipo_missao.strip().lower()
        if tipo_missao == "combate":
            # nome, descricao, recompensa, inimigo:str, inimigos_a_derrotar:int, status=Status_Missao.PENDENTE):
            return MissaoCombate(
                nome,
                descricao,
                recompensa,
                kwargs.get("tipo_inimigo"),
                kwargs.get("qnt_inimigos")
            )
        elif tipo_missao == "coleta":
            # nome, descricao, recompensa, item, quantidade:int, status=Status_Missao.PENDENTE):
            return MissaoColeta(
                nome,
                descricao,
                recompensa,
                kwargs.get("tipo_item"),
                kwargs.get("quantidade")
            )
        elif tipo_missao == "exploracao":
            # nome, descricao, recompensa, regiao_destino:str, distancia_em_km:float, tempo_limite:int, status=Status_Missao.PENDENTE):
            return MisssaoExploracao(
                nome,
                descricao,
                recompensa,
                kwargs.get("regiao_destino"),
                kwargs.get("distancia_em_km"),
                kwargs.get("tempo_limite")
            )
        else:
            raise Exception("Não foi possivel criar Missão")