from model.Status import Status_Missao
from model.missao import Missao

class MisssaoExploracao (Missao):
    def __init__(self, nome, descricao, recompensa, regiao_destino:str, distancia_em_km:float, tempo_limite:int, status=Status_Missao.PENDENTE):
        super().__init__(nome, descricao, recompensa, status)
        self.local = regiao_destino
        self.distancia = distancia_em_km
        self.tempo = tempo_limite

    @property
    def local(self):
        return self.__local
    @local.setter
    def local(self, local):
        if not isinstance(local, str):
            raise TypeError("Local precisa ser string.")
        local = local.split()
        local = ' '.join(local)
        local = local.title() #maiuscula primeira
        self.__local = local

    @property
    def distancia(self):
        return self.__distancia
    @distancia.setter
    def distancia(self, dt):
        if not isinstance(dt, float):
            raise TypeError("Distancia precisa ser decimal.")
        if 0 <= dt > 50:
            raise ValueError("Distancia precisa ser maior que 0 e menor que 50 Km")
        self.__distancia = dt
    
    @property
    def tempo(self):
        return self.__tempo
    @tempo.setter
    def tempo(self, tempo):
        if not isinstance(tempo, int):
            raise TypeError("Tempo precisa ser minutos em inteiro.")
        if 0 <= tempo > 180:
            raise ValueError("Tempo precisa ser maior que 0 e menor que 180 minutos (3 Horas)")
        self.__tempo = tempo
    

    def exibir_dados(self):
        str = super().exibir_dados()
        str += (f"Regiao destino: {self.local}\n"
                f"Distancia: {self.distancia} Km\n"
                f"Tempo limite: {self.tempo} Minutos\n{'='*30}")
        return str
    '''
        return (f"{'='*30}\n--- MISSÃO DE COMBATE: ---"
                f"\nNome da Missão: {self.nome}\n"
                f"Descrição: {self.descricao}\n"
                f"Recompensa: {self.recompensa} XP\n"
                f"Status: {self.status.name}\n"
    '''            

    def __str__(self):
        return (f"{self.nome} ({self.descricao}) XP:[{self.recompensa}]"
                f"[{self.status.value}], em: {self.local} - {self.distancia} Km - {self.tempo} min.")
   
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, MisssaoExploracao):
            return False
        return (self.nome == outro.nome and self.descricao == outro.descricao 
                and self.recompensa == outro.recompensa and self.status == outro.status
                and self.local == outro.local 
                and self.distancia == outro.distancia
                and self.tempo == outro.tempo)