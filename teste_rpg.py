from model.missao import Missao
from personagem import Personagem
from model.Missao_coleta import MissaoColeta
from model.Missao_combate import MissaoCombate

#ms1= Missao("a", "a", 15)
















msco = MissaoColeta("Coletar maças", "Colete maças pela montanha de olindo", 40,"Macas", 10)
msco2 = MissaoColeta("Coletar maças", "Colete maças pela montanha de olindo", 40,"Macas", 10)
mscomb1 = MissaoCombate("Derrotar Goblin", "Derrote os goblins da arena", 40, 50,"Goblin")

ps = Personagem("Milena")

print(ps.add_missao(msco))
print(ps.add_missao(msco2))
print(ps.add_missao(mscomb1))

ps.listar_Missao()
ps.concluir_missao(msco, 9)
#msco.concluir_missao(9)# implementação na misao
#mscomb1.concluir_missao(50)
ps.concluir_missao(mscomb1, 50)

ps.listar_Missao()
print(ps.exibir_dados())