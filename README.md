# Projeto rpg too Róger Campos
Repositório para o projeto de rpg da matéria Tecnologia de orientação à objetos.

### nome jogo: Ecos de Arcadia

# Comentários pessoais
## Anotações pessoais não relacionadas ao código eu vou deixar aqui

python convenções: [link](https://peps.python.org/pep-0008/)

### declaração variaveis:
variavel:tipo -> type hint, não bloqueia só sujere o tipo pro editor
precisa verificar com isinstance p/ bloquear testes entre tipos diferentes (str vs personagem por exemplo)

### PROPERTY's -> esse é o getter, pra poder receber de volta os dados
    @property 
    def nome(self):
        return self._nome
        
### SETTER's -> é como gravar os dados do objeto
    @nome.setter
    def nome(self, novo_nome):
        # testes aqui
        self._nome = novo_nome
