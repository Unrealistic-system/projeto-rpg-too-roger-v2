import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.personagem import Personagem
from model.FactotyMissao import factoryMissao
from model.Item import Item, Tipo_item
from model.base import *
#from model.missao import Missao
""" from tkinter import messagebox

messagebox.showinfo("janela", "teste2")
messagebox.askquestion("teste", "informe:") """

item_1 = Item("Capacete de Comerciante", "capacete formal usado por comerciantes", 10, Tipo_item.VESTIMENTA)
missao_1 = factoryMissao.criar_missao(tipo_missao="coleta",nome="Coletar maças", 
                                                descricao="Colete maças pela montanha de olindo", 
                                                recompensa=40, quantidade= 10, tipo_item= "maças")
missao_2 = factoryMissao.criar_missao("exploracao","Terranova", "busca tesouro em castelo", 10, 
                                                regiao_destino= "Novigards", distancia_em_km= 15.5, tempo_limite= 50)
person = Personagem("Milena")
person2 = Personagem("Criz")

person.add_item(item_1)
person2.add_item(item_1)

print(person.add_missao(missao_1))
print(person2.add_missao(missao_2))

person.equipar_item(item_1)
person2.equipar_item(item_1)

print(person.concluir_missao(missao_1, 2000))
print(person2.concluir_missao(missao_2, 7))

print(person.exibir_dados())
print(person2.exibir_dados())