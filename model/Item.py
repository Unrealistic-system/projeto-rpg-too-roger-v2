from model.Tipo_Item import Tipo_item
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, nome,descricao, atributo, tipo= Tipo_item)
        self.nome = nome
        self.__descricao = descricao
        self.__atributo = atributo
        self.__tipo = tipo