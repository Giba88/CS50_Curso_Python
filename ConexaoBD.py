 #Com sqlAlchemy conexao local segura
from sqlalchemy import create_engine

engine = create_engine("mssql+pyodbc:///?odbc_connect=Driver%3D%7BSQL+Server+Native+Client+11.0%7D%3BServer%3D%28localdb%29%5CMSSQLLocalDB%3BDatabase%3DBD_Python%3BTrusted_Connection%3Dyes%3B")

with engine.connect() as con:
    rs = con.execute('SELECT * FROM voos')
    for ln in rs:
        print(ln)


''' #Com sqlAlchemy conexao remota
import sqlalchemy as sa
from urllib.parse import quote_plus

parametros = (
    # Driver que será utilizado na conexão
    'DRIVER={ODBC Driver 17 for SQL Server};'
    # IP ou nome do servidor\Versão do SQL.
    'SERVER=192.168.100.178\SQLEXPRESS;'
    # Porta
    'PORT=1433;'
    # Banco que será utilizado.
    'DATABASE=PythonMSSQL;'
    # Nome de usuário.
    'UID=python;'
    # Senha.
    'PWD=123456')

url_db = quote_plus(parametros)

engine = sa.create_engine("mssql+pyodbc:///?odbc_connect=%s" % url_db)
with engine.connect() as con:

    rs = con.execute('SELECT * FROM voos')
'''

''' # Somente pyodbc conexao local segura
import pyodbc 
print([x for x in pyodbc.drivers() if x.startswith('ODBC Driver 17 for SQL Server')])
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=(localdb)\MSSQLLocalDB;'
                      'Database=BD_Python;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM voos')

for row in cursor:
    print(row)
'''

''' Com sqlAlchemy conexao local segura com conversão 
import pyodbc    
from urllib.parse import quote_plus
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

# String de conexão Windows Server.
parametros = ('Driver={SQL Server Native Client 11.0};'
                      'Server=(localdb)\MSSQLLocalDB;'
                      'Database=BD_Python;'
                      'Trusted_Connection=yes;')

# Convertendo a string para um padrão de URI HTML.
url_db = quote_plus(parametros)

# Conexão.
engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % url_db)

print('\nmssql+pyodbc:///?odbc_connect=%s\n%s' % (url_db, url_db))

db = scoped_session(sessionmaker(bind=engine))

voos = db.execute("SELECT origem, destino, duracao FROM voos").fetchall()

for voo in voos:
    print(f"{voo.origem} para {voo.destino}, {voo.duracao} minuto.")
'''