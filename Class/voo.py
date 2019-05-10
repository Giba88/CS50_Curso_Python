#from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
class Voo:

    def __init__(self, origem, destino, duracao):
        self.origem = origem
        self.destino = destino
        self.duracao = duracao

    def imprime_info(self):
        print(f"Voo origem: {self.origem}")
        print(f"Voo destino: {self.destino}")
        print(f"Voo duração: {self.duracao}")

    def atraso(self, quantidade):
        self.duracao += quantidade


def main():
    f1 = Voo(origem="New York", destino="Paris", duracao=540)
    f1.atraso(10)
    f1.imprime_info()


if __name__ == "__main__":
    main()
