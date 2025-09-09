from db import db

class Carro(db.Model):
    __tablename__ = 'carros'

    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(80), nullable=False)
    marca = db.Column(db.String(80), nullable=False)
    ano = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'modelo': self.modelo,
        }
    from db import db
# Define a classe Carro que representa a tabela 'carros' no banco de dados
class Carro(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'carros'
    # Define as colunas da tabela 'carros'
    id = db.Column(db.Integer, primary_key=True)  # Coluna para o ID do carro, chave primária
    modelo = db.Column(db.String(80), nullable=False)  # Coluna para o modelo do carro, não pode ser nulo
    marca = db.Column(db.String(80), nullable=False)  # Coluna para a marca do carro, não pode ser nulo
    ano = db.Column(db.Integer, nullable=False)  # Coluna para o ano do carro, não pode ser nulo
    # Método para retornar os dados do carro como um dicionário
    def json(self):
        return {
            'id': self.id,  # ID do carro
            'modelo': self.modelo,  # Modelo do carro
            'marca': self.marca,  # Marca do carro
            'ano': self.ano  # Ano do carro
        }