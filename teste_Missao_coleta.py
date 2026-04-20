from model.missao import Missao
from model.Misao_coleta import MissaoColeta
from model.Status import Status_Missao

msco = MissaoColeta("Coletar frutas", "Colete maças", 40,"Macas", 10)
msco2 = MissaoColeta("Coletar frutas", "Colete maças", 40,"Macas", 10)


if (msco == msco2):
    print(f"Misões são iguais: {msco}")
else:
    print(f"Misões: {msco} e {msco2} sao diferentes")

Missao.iniciar_missao(msco)

print(MissaoColeta.exibir_dados(msco))
Missao.concluir_missao(msco, 50)
print(MissaoColeta.exibir_dados(msco))

msco2.status = Status_Missao.FRACASSADA
print(MissaoColeta.exibir_dados(msco2))
Missao.concluir_missao(msco2, 20)