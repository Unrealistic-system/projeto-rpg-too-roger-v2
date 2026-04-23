from model.missao import Missao

class Personagem:
    def __init__(self, nome:str):
        self.nome = nome
        # vai com _ antes para ficar privado, só pode ser alterado o nome.
        self._nivel = 1
        self._xp = 0
        self._vida = 100
        self._misoes = []

    @property
    def nome(self):
        return self._nome
    @property
    def nivel(self):
        return self._nivel
    @property
    def xp(self):
        return self._xp
    @property
    def vida(self):
        return self._vida
    @property
    def missoes(self):
        return self._misoes
    
    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError("O nome deve ser texto!")
        novo_nome = " ".join(novo_nome.split()) # numa linha só, separa e junta denovo
        if not novo_nome:
            raise ValueError("O nome não pode ser vazio!")
        self._nome = novo_nome
    
    def add_missao(self, missao_add):
        if not isinstance(missao_add, Missao):
            return (f"Falha ao adicionar misão, objeto de tipo inválido")
        if missao_add in self.missoes:
            return (f"Misão não atribuida, ela é igual a outra misão já aceita pelo personagem!")
        self.missoes.append(missao_add)
        Missao.iniciar_missao(missao_add)
        return (f"Misão atribuida a personagem!!!")
    
    def listar_Missao(self):
        print(f"Lista de missões do personagem [{self.nome}]:")
        for item in self.missoes:
            print(item)

    def exibir_dados(self):
        return (f"{'='*30}\n--- STATUS DO JOGADOR ---\n"
                f"Nome: {self.nome}\n"
                f"Nível: {self.nivel}\n"
                f"HP: {self.vida}\n"
                f"XP: {self.xp}\n{'='*30}")
    
    def __str__(self):
        return f" --{self.nome} LV:{self.nivel} XP:{self.xp} HP:{self.vida}-- "
    
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, Personagem):# verifica o tipo do objeto, se for diferente não dá erro, só retorna falso
            return False
        return (self.nome == outro.nome and self.nivel == outro.nivel 
                and self.xp == outro.xp and self.vida == outro.vida)
                # posso retornar o teste direto, o resultado vai ser true ou false
