from model.missao import Missao
from model.enums import Status_Missao
from model.Item import Item
from model.geral import *
from model.enums import Tipo_item

class Personagem:
    def __init__(self, nome:str):


        self.nome = nome
        # vai com _ antes para ficar privado, só pode ser alterado o nome.
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 100
        self.__misoes: list[Missao] = []
        self.__ataque_Base = 0                  # ataque base do personagem 
        self.__arma_equipada: Item | None = None
        self.__vestimenta_equipada: Item | None = None
        self.__utilitario_equipado: Item | None = None
        self.__inventario: list[Item] = []
        

    @property
    def nome(self):
        return self._nome
    @property
    def nivel(self):
        return self.__nivel
    @property
    def xp(self):
        return self.__xp
    @property
    def vida(self):
        return self.__vida
    @property
    def missoes(self):
        return self.__misoes
    @property
    def ataque_base(self):
        return self.__ataque_Base
    @property
    def inventario(self):
        return self.__inventario
    @property
    def arma_equipada(self):
        return self.__arma_equipada
    @property
    def vestimenta_equipada(self):
        return self.__vestimenta_equipada
    @property
    def utilitario_equipado(self):
        return self.__utilitario_equipado
    
    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError("O nome deve ser texto!")
        novo_nome = " ".join(novo_nome.split())
        if not novo_nome:
            raise ValueError("O nome não pode ser vazio!")
        self._nome = novo_nome

    @ataque_base.setter
    def ataque_base(self, novo_ataque):
        self.__ataque_base = novo_ataque

    def __reduzir_vida(self, valor):
        if self.__vida > 0:
            if valor <= self.__vida:
                self.__vida -= valor
            elif valor <= 0:
                return (f"valor inválido")
            else:
                self.__vida = 0
                raise Exception("Game Over")
    
    def add_missao(self, missao_add):
        if not isinstance(missao_add, Missao):
            return(f"Falha ao adicionar misão, objeto de tipo inválido")
        if missao_add in self.missoes:                               # missão está nas misões já
            return(f"Misão não atribuida, ela é igual a outra misão já aceita pelo personagem!")
        self.missoes.append(missao_add)
        Missao.iniciar_missao(missao_add)
        return(f"Misão atribuida a personagem!!!")
    
    def listar_Missao(self):
        msg = f"Lista de missões do personagem [{self.nome}]:\n"
        for item in self.missoes:
            msg += f"{item}\n"
        return msg

    def concluir_missao(self, missao: Missao, valor):
            for m in self.__misoes:
                if m == missao:
                    resultado = m.concluir_missao(valor)
                    if m.status == Status_Missao.CONCLUIDA:
                        self.__xp += m.recompensa
                        if self.__xp >= 20:
                            ganho_vida = self.__xp // 20
                            self.__nivel += ganho_vida
                            self.__xp = self.__xp % 20
                    elif m.status == Status_Missao.FRACASSADA:
                        self.__reduzir_vida(10)      
                    return resultado
            raise ValueError("Missão não encontrada")

    def mostrar_inventario(self):
        msg = f"--Itens no Inventário de [{self.nome}] :--\n"
        for i, valor in enumerate(self.__inventario):
            msg += f"{i} - {valor.exibir_dados()}\n"
        return msg

    def add_item(self, item):
        if not isinstance(item, Item):
            return(f"Falha ao adicionar Item, objeto de tipo inválido")
        if item in self.__inventario:
            return(f"Falha ao adicionar Item, item Já no inventário")
        self.__inventario.append(item)
        return(f"Item [{item._nome}] adicionado ao inventário de [{self._nome}]!")

    def remover_item(self, item):
        if item in self.__inventario:
            self.__inventario.remove(item)
            return(f"Item removido do inventário!!")
        else:
            return(f"Item não encontrado no inventário!!")
        
    def equipar_itens(self):
        # while self.__arma_equipada == None or self.vestimenta_equipada == None or self.utilitario_equipado == None:
        while True:
            limpar_terminal()
            print(self.mostrar_inventario())
            try:
                indice = int(input(f"Digite o número do item a ser equipado:"))
                item_equipar = self.inventario[indice]
                if item_equipar.tipo == Tipo_item.ARMA:
                    self.ataque_base += item_equipar.valor_efeito
                    self.__arma_equipada = item_equipar
                elif item_equipar.tipo == Tipo_item.VESTIMENTA:
                    self.__vida += aumenta_porcentagem(self.__vida, item_equipar.valor_efeito)
                    self.__vestimenta_equipada = item_equipar
                elif item_equipar.tipo == Tipo_item.UTILITARIO:
                    self.__vida += aumenta_porcentagem(self.__vida, item_equipar.valor_efeito)
                    self.__utilitario_equipado = item_equipar
                return f"Item equipado com sucesso!!!"
            except IndexError or ValueError:
                print(f"item digitado não existe!")
                pausa()
    def desequipar(self):
        self.__arma_equipada = None
        self.__vestimenta_equipada = None
        self.__utilitario_equipado = None

    def mostrar_itens_equipados(self):
        msg = f"\n-- Itens Equipados de [{self.nome}]: --\n"
        e = "Nenhum" # texto se vazio
        msg += (f"Arma: "
                f"{self.__arma_equipada if self.__arma_equipada is not None else e}\n")
        msg += (f"Vestimenta: "
                f"{self.__vestimenta_equipada if self.__vestimenta_equipada is not None else e}\n")
        msg += (f"Utilitário: "
                f"{self.__utilitario_equipado if self.__utilitario_equipado is not None else e}\n")
        return msg

## padrão
    def exibir_dados(self):
        return (f"{'='*30}\n--- STATUS DO JOGADOR ---\n"
                f"Nome: {self.nome}\n"
                f"Nível: {self.nivel}\n"
                f"HP: {self.vida}\n"
                f"XP: {self.xp}\n{'='*30}")
    
    def __str__(self):
        return (f" --{self.nome} LV:{self.nivel}"
                f" XP:{self.xp} HP:{self.vida}-- ")
    
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, Personagem):
            return False
        return (self.nome == outro.nome 
                and self.nivel == outro.nivel 
                and self.xp == outro.xp 
                and self.vida == outro.vida)