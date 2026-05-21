
class menu:
    def __init__(self, titulo, qntd, itens):
        self.titulo = titulo
        self._qntd = qntd
        self.itens: list[str] = itens
        self.selecao = None

    @property
    def selecao(self):
        return self.selecao
    
    @selecao.setter
    def selecao(self):
        opc= 1
        self.selecao = opc

    
    def exibir(self)->str:
        if len(self.itens) == 0:
            return f"{self.titulo}: \nNenhuma opcão disponível"
        
        msg = f"\n{self.titulo}:\n"
        for i, valor in enumerate(self.itens, 0):
            msg += f"{i} - {valor}\n"
        print("\nSelecione: ")
        return msg
    