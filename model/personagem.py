from model.missao import Missao
from model.Status import Status_Missao
from model.Item import Item

class Personagem:
    def __init__(self, nome:str):
        self.nome = nome
        # vai com _ antes para ficar privado, só pode ser alterado o nome.
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 100
        self.__misoes: list[Missao] = []
        self.__ataque_Base = 0
        self.__arma_equipada = Item
        self.__vestimenta_equipada = Item
        self.__utilitario_equipado = Item
        self.__inventario = list[Item] = []

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
        if missao_add in self.missoes:# missão está nas misões já
            return(f"Misão não atribuida, ela é igual a outra misão já aceita pelo personagem!")
        self.missoes.append(missao_add)
        Missao.iniciar_missao(missao_add)
        return(f"Misão atribuida a personagem!!!")
    
    def listar_Missao(self):
        print(f"Lista de missões do personagem [{self.nome}]:")
        for item in self.missoes:
            print(item)

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
            raise Exception("Missão não encontrada")

    def mostrar_inventario(self):
        msg = f"Inventário do personagem [{self.nome}]:\n"
        cont = 1
        for it in self.inventario:
            msg += f"{cont} - {it}\n"
            cont += 1
        return msg

    def add_item(self, item):
        if not isinstance(item, Item):
            return(f"Falha ao adicionar Item, objeto de tipo inválido")
        if item in self.__inventario:
            return(f"Falha ao adicionar Item, item Já no inventário")
        self.inventario.append(item)

    def remover_item(self, item):
        if item in self.__inventario:
            self.__inventario.remove(item)
            return(f"Item removido do inventário!!")
        else:
            return(f"Item não encontrado!!")
        
    def equipar_itens(self):
        print(f"\n--Itens disponíveis para equipar:--\n")
        for i in self.__inventario:
            print(f"1 - {i}\n")
        add = print(f"Digite o número do item a ser adicionado:")
        






















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