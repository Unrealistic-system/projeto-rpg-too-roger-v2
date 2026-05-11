from model.enums import Tipo_item

class Item():
    def __init__(self, nome,descricao, valor_efeito, tipo: Tipo_item):
        self.nome = nome
        self.descricao = descricao
        self.valor_efeito = valor_efeito
        self.__tipo = tipo

    @property
    def nome(self):
        return self._nome
    @property
    def descricao(self):
        return self.__descricao
    @property
    def valor_efeito(self):
        return self.__valor_efeito
    @property
    def tipo(self):
        return self.__tipo
    
    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError("O nome deve ser texto!")
        novo_nome = " ".join(novo_nome.split())
        if not novo_nome:
            raise ValueError("O nome não pode ser vazio!")
        self._nome = novo_nome

    @descricao.setter
    def descricao(self, n_desc):
        if not isinstance(n_desc, str):
            raise TypeError ("descrição precisa ser texto!!!")
        n_desc = n_desc.split()
        n_desc = ' '.join(n_desc)
        if  not n_desc:
            raise ValueError ("Descrição é obrigatória!!!")
        self.__descricao = n_desc

    @valor_efeito.setter
    def valor_efeito(self, n_valor):
        if not isinstance(n_valor, int):
            raise TypeError("Valor de efeito precisa ser número inteiro.")
        if n_valor < 0 or n_valor > 50:
            raise Exception ("Valor de efeito precisa ser positiva e menor que 50!!!")
        self.__valor_efeito = n_valor

    def __str__(self) -> str:
        return f"[{self.nome}], {self.valor_efeito}, {self.descricao}"
    
    def exibir_dados(self) -> str:
        return f"{self.tipo.name}: [{self.nome}], {self.valor_efeito}, {self.descricao}"
    
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, Item):
            return False
        return (self.nome == outro.nome)