from model.missao import Missao
from model.enums import Status_Missao
from model.Item import Item
from model.base import *
from model.enums import Tipo_item

class Personagem:
    def __init__(self, nome:str):


        self.nome = nome
        # vai com _ antes para ficar privado, só pode ser alterado o nome.
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 80
        self.__misoes: list[Missao] = []
        self._ataque_Base = 0 
        self.__arma_equipada: Item | None = None
        self.__vestimenta_equipada: Item | None = None
        self.__utilitario_equipado: Item | None = None
        self.__inventario: list[Item] = []
# getters:
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
        return self._ataque_Base
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
# setters:
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
        self._ataque_base = novo_ataque

# outros métodos:
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
        if missao_add in self.missoes:# missão já está nas misões, não atribuir novamente
            return(f"Misão não atribuida, ela é igual a outra misão já aceita pelo personagem!")
        if len(self.inventario) > 0:
            while self.__arma_equipada == None and self.vestimenta_equipada == None and self.utilitario_equipado == None:
                print(self.equipar_item(self))
            self.missoes.append(missao_add)
            Missao.iniciar_missao(missao_add)
            return(f"Misão atribuida a personagem!!!")
        else:
            return("Impossivel atribuir Missões, inventário vazio!!!")

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
        
    def equipar_item(self, item_equipar):
        if not isinstance(item_equipar, Item):
            return "Item não equipado, erro!!"
        if item_equipar.tipo == Tipo_item.ARMA:
            if self.arma_equipada != None:
                self.ataque_Base -= self.arma_equipada.valor_efeito
            self.ataque_base += item_equipar.valor_efeito
            self.__arma_equipada = item_equipar
        elif item_equipar.tipo == Tipo_item.VESTIMENTA:
            if self.vestimenta_equipada != None:
                self.__vida = diminui_porcentagem(self.vida, self.vestimenta_equipada.valor_efeito)
            self.__vida = aumenta_porcentagem(self.__vida, item_equipar.valor_efeito)
            self.__vestimenta_equipada = item_equipar
        elif item_equipar.tipo == Tipo_item.UTILITARIO:
            if self.utilitario_equipado != None:
                self.__vida = diminui_porcentagem(self.vida, self.utilitario_equipado.valor_efeito)
            self.__vida = aumenta_porcentagem(self.__vida, item_equipar.valor_efeito)
            self.__utilitario_equipado = item_equipar
        return f"Item equipado com sucesso!!!"
            


    def desequipar(self):
        self.__arma_equipada = None
        self.__vestimenta_equipada = None
        self.__utilitario_equipado = None

## Exibição de dados:
    def mostrar_itens_equipados(self):
        msg = (f"Arma: "
                f"{self.__arma_equipada if self.__arma_equipada is not None else "Desequipado"}\n")
        msg += (f"Vestimenta: "
                f"{self.__vestimenta_equipada if self.__vestimenta_equipada is not None else "Desequipado"}\n")
        msg += (f"Utilitário: "
                f"{self.__utilitario_equipado if self.__utilitario_equipado is not None else "Desequipado"}\n")
        return msg
    
    def mostrar_inventario(self):
        return mostrar_lista(self.inventario, f"Itens no Inventário de [{self.nome}]", 1)
    
    def listar_Missao(self):
        return mostrar_lista(self.missoes, f"Lista de missões do personagem [{self.nome}]", 1)

    def exibir_dados(self):
        return (f"{'='*30}\n--- STATUS DO JOGADOR ---\n"
                f"Nome: {self.nome}\n"
                f"Nível: {self.nivel}\n"
                f"HP: {self.vida}\n"
                f"XP: {self.xp}\n"
                f"ATK base: {self.ataque_base}\n"
                f"{self.mostrar_itens_equipados()}"
                f"{'='*30}")
    
    def __str__(self):
        return (f" --{self.nome} LV:{self.nivel}"
                f" XP:{self.xp} HP:{self.vida}-- ")

## métodos padrão:
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, Personagem):
            return False
        return (self.nome == outro.nome) # só comparar o nome para poder bloquear crição de personagens com mesmo nome