from model.Status import Status_Missao
from model.missao import Missao

class MissaoCombate (Missao):
    def __init__(self, nome, descricao, recompensa, inimigos_a_derrotar:int, 
                 inimigo:str, status=Status_Missao.PENDENTE):
        super().__init__(nome, descricao, recompensa, status)
        self.inimigos_a_derrotar = inimigos_a_derrotar
        self.inimigo = inimigo

    @property 
    def inimigo(self):
        return self.__inimigo
    @inimigo.setter
    def inimigo(self, it):
        if not isinstance(it, str):
            raise TypeError("Inimigo precisa ser string.")
        it = it.split()
        it = ' '.join(it)
        it = it.title() #maiuscula primeira
        self.__inimigo = it

    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar
    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, qt):
        if not isinstance(qt, int):
            raise TypeError("Inimigos a derrotar precisa ser inteiro.")
        self.__inimigos_a_derrotar = qt
        
    
    def exibir_dados(self):
        str = super().exibir_dados()
        str += (f"Inimigo : {self.inimigo}\n"
                f"Inimigos a derrotar: {self.inimigos_a_derrotar}\n{'='*30}")
        return str        

    def concluir_missao (self, valor):
            super().concluir_missao(valor)
            if isinstance(valor, int):
                if valor >= self.inimigos_a_derrotar:
                    self.status = Status_Missao.CONCLUIDA
                    print(f"Missão '{self.nome}' foi concluída com sucesso. A contabilidade do "
                        f"prêmio de {self.recompensa} XP agora está pronta para retirada financeira.")
                else:
                    print(f"Missão '{self.nome}' não foi concluída, a quantidade de {self.inimigos_a_derrotar} "
                          f"não foi atingida. Faltam {self.inimigos_a_derrotar-valor}")
                    self.status = Status_Missao.FRACASSADA
            else:
                return(f"Tipo de dado inválido!!")

    def __str__(self):
        str = super().__str__()
        str += f" inimigo: {self.inimigo} X [{self.inimigos_a_derrotar}]"
        return str
   
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, MissaoCombate):
            return False
        return (self.nome == outro.nome 
                and self.descricao == outro.descricao 
                and self.recompensa == outro.recompensa 
                and self.inimigo == outro.inimigo 
                and self.inimigos_a_derrotar == outro.inimigos_a_derrotar)
    
