from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.missao import Missao

class EstadoMissao(ABC):
    def __init__(self, missao):
        self.missao = missao
    
    @property 
    def missao(self):
        return self._missao
    
    @missao.setter
    def missao(self, atribuir_missao):
        from model.missao import Missao
        if not isinstance(atribuir_missao, Missao):
            raise TypeError("Erro, objeto não é uma missão")
        self._missao = atribuir_missao

    @abstractmethod
    def iniciar(self) -> 'EstadoMissao':
        pass

    @abstractmethod
    def concluir(self, valor_exigido, valor_obtido) -> 'EstadoMissao':
        pass

    def __str__(self):
        return (f"{self.__class__.__name__}")
   
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, EstadoMissao):
            return False
        return (self.__class__.__name__ == outro.__class__.__name__)
    
class EstadoPendente(EstadoMissao):
    def __init__(self, missao: 'Missao'):
        super().__init__(missao)

    def iniciar(self):
        super().iniciar()
        return EstadoAndamento(self.missao)

    def concluir(self, valor_exigido, valor_obtido):
        super().concluir(valor_exigido, valor_obtido) # não usa no pendente os valores, mas precisa ter
        return EstadoAndamento(self.missao) 

class EstadoAndamento(EstadoMissao):
    def __init__(self, missao: 'Missao'):
        super().__init__(missao)

    def iniciar(self):
        super().iniciar()
        return EstadoAndamento(self.missao)

    def concluir(self, valor_exigido, valor_obtido):
        super().concluir(valor_exigido, valor_obtido)
        if valor_obtido >= valor_exigido:
            return EstadoConcluida(self.missao)
        else:
            return EstadoFracassada(self.missao)
    
class EstadoConcluida(EstadoMissao):
    def __init__(self, missao: 'Missao'):
        super().__init__(missao)

    def iniciar(self):
        super().iniciar()
        return self

    def concluir(self, valor_exigido, valor_obtido):
        super().concluir(valor_exigido, valor_obtido)
        print("Missão já concluida, não é possivel concluir novamente")
        return self
    
class EstadoFracassada(EstadoMissao):
    def __init__(self, missao: 'Missao'):
        super().__init__(missao)

    def iniciar(self):
        super().iniciar()
        return self

    def concluir(self, valor_exigido, valor_obtido):
        super().concluir(valor_exigido, valor_obtido)
        print("Missão fracassada, não é possivel concluir")
        return self