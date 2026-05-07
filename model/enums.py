from enum import Enum

class Status_Missao (Enum):
    PENDENTE = "PENDENTE"
    EM_ANDAMENTO = "EM ANDAMENTO"
    CONCLUIDA = "CONCLUIDA"
    FRACASSADA = "FRACASSADA"

class Tipo_item (Enum):
    ARMA = "Arma"
    VESTIMENTA = "Vestimenta"
    UTILITARIO = "Utilitário"
    