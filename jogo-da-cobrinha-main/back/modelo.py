from config import *

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    macas_coletadas = db.Column(db.Integer, default=0)

    def coletar_maca(self):
        self.macas_coletadas += 1

    def __str__(self):
        return f'{self.id}, {self.nome}, {self.macas_coletadas}'
    
    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "maçãs coletadas":self.macas_coletadas
        }

