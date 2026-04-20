from model.missao import Missao
#from model.Misao_coleta import MissaoColeta
#from model.Missao_combate import MissaoCombate
#from model.Missao_exploracao import MisssaoExploracao
from personagem import Personagem
from entradas_imput import entrada_missao, entrada_personagem

ms = entrada_missao() # digitar missão
#ms = missao("Do Disapered Demons See God?", "Determine de cause of the disapperances from the Oni tribe", 50)
print(ms.exibir_dados())
ms2 = Missao("Do Disapered Demons See God?", "Determine de cause of the disapperances from the Oni tribe", 50)
if ms == ms2:
    print(f"Misões são iguais: {ms2}")
else:
    print(f"Misões: {ms} e {ms2} sao diferentes")


ps = entrada_personagem() # digitar personagem
#ps = personagem("Crim")
print(ps.exibir_dados())
ps2 = Personagem("Bianca")
if ps == ps2:
    print(f"personagens são iguais: {ps2}")
else:
    print(f"personagens: {ps} e {ps2} sao diferentes")
