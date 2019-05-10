import os
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine("mssql+pyodbc:///?odbc_connect=Driver%3D%7BSQL+Server+Native+Client+11.0%7D%3BServer%3D%28localdb%29%5CMSSQLLocalDB%3BDatabase%3DBD_Python%3BTrusted_Connection%3Dyes%3B")

db = scoped_session(sessionmaker(bind=engine))

#Meu
'''session = sessionmaker()
session.configure(bind=engine)'''
#fim

def main():
    voos = db.execute("SELECT origem, destino, duracao FROM voos").fetchall()
    
    for voo in voos:
        print(f"{voo.origem} para {voo.destino}, {voo.duracao} minuto.")

if __name__ == "__main__":
    main()
