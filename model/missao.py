from abc import ABC, abstractmethod
from model.Status import *

class Missao(ABC): # começar classe com maiusculo - convenção python
    def __init__(self, nome, descricao, recompensa):
        """ self.nome = None
        self._descricao = None
        self._recompensa = 0
        self._estado = None """
        
        self.nome = nome
        self._descricao = descricao
        self._recompensa = recompensa
        self._estado = EstadoPendente(self)

    @property 
    def nome(self):
        return self._nome
        
    @property
    def descricao(self):
        return self._descricao
    @property
    def recompensa(self):
        return self._recompensa
    @property
    def estado(self):
        return self._estado
    
    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError ("Nome precisa ser texto!!!")
        novo_nome = novo_nome.split()# separa
        novo_nome = ' '.join(novo_nome)# junta sem espaço a mais
        if not novo_nome: # pega qualquer coisa, " " ou none tmb
            raise ValueError ("Nome é obrigatório!!!")
        self._nome = novo_nome

    @descricao.setter
    def descricao(self, n_desc):
        if not isinstance(n_desc, str):
            raise TypeError ("descrição precisa ser texto!!!")
        n_desc = n_desc.split()
        n_desc = ' '.join(n_desc)
        if  not n_desc:
            raise ValueError ("Descrição é obrigatória!!!")
        self._descricao = n_desc

    @recompensa.setter
    def recompensa(self, n_rec):
        if not isinstance(n_rec, int):
            raise TypeError("Recompensa precisa ser número inteiro.")
        if 0 <= n_rec > 50:
            raise Exception ("Recompensa precisa ser positiva e menor que 50!!!")
        self._recompensa = n_rec

    @estado.setter
    def estado(self, n_st):
        if isinstance(n_st, EstadoMissao):
            self._estado = n_st
        else:
            raise TypeError("Estado inválido.")

    def iniciar_missao (self):
        if isinstance(self.estado, EstadoPendente):
            self.estado = self.estado.iniciar()
            return (f"Missão: {self.nome}, começou! Objetivo central da missão: {self.descricao}")
        else:
            return (f"Erro não foi possivel iniciar!")
        
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, Missao):
            return False
        return (self.nome == outro.nome)

    @abstractmethod
    def concluir_missao (self, valor):
        pass

    @abstractmethod
    def exibir_dados(self):
        return (f"{self.__class__.__name__}\n"
                f"{'='*30}\n--- MISSÃO ---\nNome da Missão: {self.nome}\n"
                f"Descrição: {self.descricao}\nRecompensa: {self.recompensa} XP\n"
                f"Status: {self.estado.__class__.__name__}\n")
    
    @abstractmethod
    def __str__(self):
        return (f"{self.__class__.__name__}: {self.nome} ({self.descricao}) "
                f"XP:[{self.recompensa}] [{self.estado.__class__.__name__}]")