from model.missao import Missao
from model.Missao_combate import MissaoCombate
from model.Status import Status_Missao

mscomb1 = MissaoCombate("Derrotar Goblin", "Derrote os goblins da arena", 40, 50,"Goblin")
mscomb2 = MissaoCombate("Derrotar Grifo", "Derrote os grifos da arena", 30, 20,"Grifo", Status_Missao.FRACASSADA)


if (mscomb1 == mscomb2):
    print(f"Misões são iguais: {mscomb1}")
else:
    print(f"Misões: {mscomb1} e {mscomb2} sao diferentes")

MissaoCombate.iniciar_missao(mscomb1)

print(MissaoCombate.exibir_dados(mscomb1))
Missao.concluir_missao(mscomb1)
print(MissaoCombate.exibir_dados(mscomb1))

MissaoCombate.iniciar_missao(mscomb2)
print(MissaoCombate.exibir_dados(mscomb2))
Missao.concluir_missao(mscomb2)