from model.missao import Missao
from model.Status import EstadoConcluida, EstadoPendente


class MisssaoExploracao (Missao):
    def __init__(self, nome, descricao, recompensa, regiao_destino, distancia_em_km, tempo_limite):
        super().__init__(nome, descricao, recompensa)
        #self._estado = EstadoPendente(self)
        self.local = regiao_destino
        self.distancia = distancia_em_km
        self.tempo = tempo_limite

    @property
    def local(self):
        return self.__local
    @property
    def distancia(self):
        return self.__distancia
    @property
    def tempo(self):
        return self.__tempo
    
    @local.setter
    def local(self, local):
        if not isinstance(local, str):
            raise TypeError("Local precisa ser string.")
        local = local.split()
        local = ' '.join(local)
        local = local.title() #maiuscula primeira
        self.__local = local
    
    @distancia.setter
    def distancia(self, dt):
        if not isinstance(dt, float):
            raise TypeError("Distancia precisa ser decimal.")
        if 0 <= dt > 50:
            raise ValueError("Distancia precisa ser maior que 0 e menor que 50 Km")
        self.__distancia = dt
    
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

    def concluir_missao (self, valor):
            super().concluir_missao(valor)
            self.estado = self.estado.concluir(self.distancia, valor) # type: ignore

            if self.estado == EstadoConcluida:
                print(f"Missão '{self.nome}' foi concluída com sucesso. A contabilidade do "
                      f"prêmio de {self.recompensa} XP agora está pronta para retirada financeira.")
            else:
                print(f"Missão '{self.nome}' não foi concluída, a quantidade de {self.distancia} "
                      f"não foi atingida. Faltam {self.distancia-valor}")

    def __str__(self):
        str = super().__str__()
        str += f", em: {self.local} - {self.distancia} Km - {self.tempo} min."
        return str
   
    """ def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, MisssaoExploracao):
            return False
        return (self.nome == outro.nome 
                and self.descricao == outro.descricao 
                and self.recompensa == outro.recompensa 
                and self.local == outro.local 
                and self.distancia == outro.distancia
                and self.tempo == outro.tempo) """