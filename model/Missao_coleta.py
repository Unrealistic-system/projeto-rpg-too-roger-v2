from model.Status import Status_Missao
from model.missao import Missao

class MissaoColeta (Missao):
    def __init__(self, nome, descricao, recompensa, item, quantidade:int, status=Status_Missao.PENDENTE):
        super().__init__(nome, descricao, recompensa, status)
        self.item_necessario = item
        self.quantidade = quantidade
    
    @property 
    def item_necesario(self):
        return self.__item_necessario
    @item_necesario.setter
    def item_necessario(self, it):
        if not isinstance(it, str):
            raise TypeError("Item precisa ser texto.")
        it = it.split()
        it = ' '.join(it)
        self.__item_necessario = it

    @property 
    def quantidade(self):
        return self.__quantidade
    @quantidade.setter
    def quantidade(self, qt):
        if not isinstance(qt, int):
            raise TypeError("Quantidade precisa ser um número inteiro.")
        if qt <= 0:
            raise ValueError("quantidade precisa ser maior que zero!")
        else:
            self.__quantidade = qt

    def concluir_missao (self, valor):
            super().concluir_missao(valor)
            if isinstance(valor, int):
                if valor >= self.quantidade:
                    self.status = Status_Missao.CONCLUIDA
                    return(f"Missão '{self.nome}' foi concluída com sucesso. A contabilidade do "
                        f"prêmio de {self.recompensa} XP agora está pronta para retirada financeira.")
                else:
                    self.status = Status_Missao.FRACASSADA
                    return(f"Missão '{self.nome}' não foi concluída, a quantidade de {self.item_necesario} "
                          f"não foi atingida. Faltam {self.quantidade-valor}")
            else:
                return(f"Tipo de dado inválido!!")
        


    def exibir_dados(self):
        str = super().exibir_dados()
        str += (f"Item necessário: {self.item_necesario}\n"
                f"Quantidade: {self.quantidade}\n{'='*30}")
        return str

    def __str__(self):
        str = super().__str__()
        str += f", item: {self.item_necesario} X [{self.quantidade}]"
        return str
        # return f"{self.nome} ({self.descricao}) XP:[{self.recompensa}] [{self.status.value}]
   
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, MissaoColeta):
            return False
        return (self.nome == outro.nome 
                and self.descricao == outro.descricao 
                and self.recompensa == outro.recompensa 
                and self.item_necesario == outro.item_necesario 
                and self.quantidade == outro.quantidade)
    