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
        if isinstance(valor, int):
            if self.status == Status_Missao.CONCLUIDA:
                print(f"Missão '{self.nome}' Já foi concluida, não é possivel concluir novamente.")
                return
            elif self.status == Status_Missao.FRACASSADA:
                print(f"Missão '{self.nome}' Já foi Terminada com Fracasso, não é possivel concluir novamente.")
                return
            elif self.status == Status_Missao.PENDENTE:
                print(f"Missão '{self.nome}' não foi iniciada, não é possivel finalizar.")
                return
            else:
                if valor >= self.quantidade:
                    self.status = Status_Missao.CONCLUIDA
                    print(f"Missão '{self.nome}' foi concluída com sucesso. A contabilidade do "
                        f"prêmio de {self.recompensa} XP agora está pronta para retirada financeira.")
                else:
                    print(f"Missão '{self.nome}' não foi concluída, a quantidade de {self.item_necesario} não foi atingida. Faltam {self.quantidade-valor}")
        else:
            print(f"Tipo de dado inválido!!")
            # raise ValueError (f"")
        


    def exibir_dados(self):
        str = super().exibir_dados()
        str += (f"Item necessário: {self.item_necesario}\n"
                f"Quantidade: {self.quantidade}\n{'='*30}")
        return str
    '''
        return (f"{'='*30}\n--- MISSÃO DE COLETA: ---"
                f"\nNome da Missão: {self.nome}\n"
                f"Descrição: {self.descricao}\n"
                f"Recompensa: {self.recompensa} XP\n"
                f"Status: {self.status.name}\n"
                f"Item necessário: {self.item_necesario}\n"
                f"Quantidade: {self.quantidade}\n{'='*30}")
    '''

    def __str__(self):
        str = super().__str__()
        str += ", item: {self.item_necesario} X [{self.quantidade}]"
        return str
        # return f"{self.nome} ({self.descricao}) XP:[{self.recompensa}] [{self.status.value}]
   
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, MissaoColeta):
            return False
        return (self.nome == outro.nome and self.descricao == outro.descricao 
                and self.recompensa == outro.recompensa and self.status == outro.status
                and self.item_necesario == outro.item_necesario 
                and self.quantidade == outro.quantidade)
    