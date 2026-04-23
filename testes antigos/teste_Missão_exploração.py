from model.Missao_exploracao import MisssaoExploracao
from model.Status import Status_Missao

msexp = MisssaoExploracao("Andando em meio as pedras", "Explorar a região", 45, "Matil", 1.78, 50, Status_Missao.EM_ANDAMENTO)
msexp2 = MisssaoExploracao("Caminho dos rios", "Explorar a região", 45, "Kaulium", 2.78, 50, Status_Missao.FRACASSADA)


if (msexp == msexp2):
    print(f"Misões são iguais: {msexp}")
else:
    print(f"Misões: {msexp} e {msexp2} sao diferentes")

MisssaoExploracao.iniciar_missao(msexp)

print(MisssaoExploracao.exibir_dados(msexp))
MisssaoExploracao.concluir_missao(msexp)
print(MisssaoExploracao.exibir_dados(msexp))

# msexp2.status = "teste" # retorna typeError
print(MisssaoExploracao.exibir_dados(msexp2))
MisssaoExploracao.concluir_missao(msexp2)