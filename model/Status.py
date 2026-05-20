from abc import ABC, abstractmethod
from model.missao import Missao
class Status_Missao (Enum):
    PENDENTE = "PENDENTE"
    EM_ANDAMENTO = "EM ANDAMENTO"
    CONCLUIDA = "CONCLUIDA"
    FRACASSADA = "FRACASSADA"

class EstadoMissao(ABC): # começar classe com maiusculo - convenção python
    def __init__(self, missao:Missao):
        self.missao = missao
    
    @property 
    def missao(self):
        return self.missao
    
    @missao.setter
    def missao(self, atribuir_missao):
        if not isinstance(atribuir_missao, Missao):
            raise TypeError("Erro, objeto não é uma missão")
        self.missao = atribuir_missao

    @abstractmethod
    def iniciar(self):
        pass
    @abstractmethod
    def concluir(self, valor):
        pass

    def __str__(self):
        return (f"{self.__class__.__name__}")
   
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, EstadoMissao):
            return False
        return (self.__class__.__name__ == outro.__class__.__name__)
    
class EstadoPendente(EstadoMissao):
    def __init__(self, missao: Missao):
        super().__init__(missao)
    def iniciar(self):
        return super().iniciar()
    def concluir(self, valor):
        return super().concluir(valor)
    
class EstadoAndamento(EstadoMissao):
    def __init__(self, missao: Missao):
        super().__init__(missao)
    def iniciar(self):
        return super().iniciar()
    def concluir(self, valor):
        return super().concluir(valor)
    
class EstadoConcluida(EstadoMissao):
    def __init__(self, missao: Missao):
        super().__init__(missao)
    def iniciar(self):
        return super().iniciar()
    def concluir(self, valor):
        return super().concluir(valor)
    
class EstadoFracassada(EstadoMissao):
    def __init__(self, missao: Missao):
        super().__init__(missao)
    def iniciar(self):
        return super().iniciar()
    def concluir(self, valor):
        return super().concluir(valor)