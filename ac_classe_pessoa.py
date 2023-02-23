class Pessoa:
    def __init__(self, nome='', email='', telefone=''):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    def __str__(self):
        return f'{self.nome}, '+\
               f'{self.email}, {self.telefone}'
