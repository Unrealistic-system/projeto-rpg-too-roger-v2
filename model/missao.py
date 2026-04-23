from model.Status import Status_Missao

class Missao: # começar classe com maiusculo - convenção python
    def __init__(self, nome, descricao, recompensa, status= Status_Missao.PENDENTE):
        self._nome = None
        self._descricao = None
        self._recompensa = None
        
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.status = status

    @property 
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError ("Nome precisa ser texto!!!")
        novo_nome = novo_nome.split()# separa
        novo_nome = ' '.join(novo_nome)# junta sem espaço a mais
        if not novo_nome: # pega qualquer coisa, " " ou none tmb
            raise ValueError ("Nome é obrigatório!!!")
        self._nome = novo_nome
        
    @property
    def descricao(self):
        return self._descricao
    @property
    def recompensa(self):
        return self._recompensa
    @property
    def status(self):
        return self._status
    
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

    @status.setter
    def status(self, n_st):
        if isinstance(n_st, Status_Missao):
            self._status = n_st
        else:
            raise TypeError(f"O status deve ser uma destas opções: {[s.name for s in Status_Missao]}")

    def iniciar_missao (self):
        if self.status == Status_Missao.EM_ANDAMENTO:
            print(f"Missão {self.nome} Já foi Iniciada, não é possivel iniciar novamente.")
            return
        # nasse caqso print não é uma boa prática, usar return
        elif self.status == Status_Missao.CONCLUIDA:
            print(f"Missão {self.nome} Já foi Concluida, não é possivel iniciar novamente.")
            return
        elif self.status == Status_Missao.FRACASSADA:
            print(f"Missão {self.nome} Já foi Terminada com Fracasso, não é possivel iniciar novamente.")
            return
        else:
            self.status = Status_Missao.EM_ANDAMENTO
            print(f"A missão '{self.nome}' começou! Objetivo central da missão: {self.descricao}")

    def concluir_missao (self, valor):
            if self.status == Status_Missao.CONCLUIDA:
                return(f"Missão '{self.nome}' Já foi concluida, não é possivel concluir novamente.")
            elif self.status == Status_Missao.FRACASSADA:
                return(f"Missão '{self.nome}' Já foi Terminada com Fracasso, não é possivel"
                       " concluir novamente.")
            elif self.status == Status_Missao.PENDENTE:
                return(f"Missão '{self.nome}' não foi iniciada, não é possivel finalizar.")
        
    def exibir_dados(self):
        return (f"{self.__class__.__name__}\n"
                f"{'='*30}\n--- MISSÃO ---\nNome da Missão: {self.nome}\n"
                f"Descrição: {self.descricao}\nRecompensa: {self.recompensa} XP\n"
                f"Status: {self.status.name}\n")
       
    def __str__(self):
        return (f"{self.__class__.__name__}: {self.nome} ({self.descricao}) "
                f"XP:[{self.recompensa}] [{self.status.value}]")
   
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, Missao):
            return False
        return (self.nome == outro.nome 
                and self.descricao == outro.descricao 
                and self.recompensa == outro.recompensa)
    
