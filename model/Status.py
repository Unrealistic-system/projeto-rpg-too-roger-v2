from abc import ABC, abstractmethod
from model.missao import Missao

""" class Status_Missao (Enum):
    PENDENTE = "PENDENTE"
    EM_ANDAMENTO = "EM ANDAMENTO"
    CONCLUIDA = "CONCLUIDA"
    FRACASSADA = "FRACASSADA" """

class EstadoMissao(ABC):
    def __init__(self, missao:Missao):
        self.missao = missao
    
    @property 
    def missao(self):
        return self._missao
    
    @missao.setter
    def missao(self, atribuir_missao):
        if not isinstance(atribuir_missao, Missao):
            raise TypeError("Erro, objeto não é uma missão")
        self._missao = atribuir_missao

    @abstractmethod
    def iniciar(self) -> 'EstadoMissao':
        pass

    @abstractmethod
    def concluir(self, valor) -> 'EstadoMissao':
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
        super().iniciar()
        return self

    def concluir(self, valor):
        super().concluir(valor)
        return EstadoAndamento(self.missao) 

class EstadoAndamento(EstadoMissao):
    def __init__(self, missao: Missao):
        super().__init__(missao)

    def iniciar(self):
        super().iniciar()
        return EstadoAndamento(self.missao)

    def concluir(self, valor):
        super().concluir(valor)
        if valor < self.missao.
        return EstadoConcluida(self.missao) 
    
class EstadoConcluida(EstadoMissao):
    def __init__(self, missao: Missao):
        super().__init__(missao)

    def iniciar(self):
        super().iniciar()
        return self

    def concluir(self, valor):
        super().concluir(valor)
        return self
    
class EstadoFracassada(EstadoMissao):
    def __init__(self, missao: Missao):
        super().__init__(missao)

    def iniciar(self):
        super().iniciar()
        return self

    def concluir(self, valor):
        super().concluir(valor)
        return self