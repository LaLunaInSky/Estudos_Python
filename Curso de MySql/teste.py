from pymysql import *
from .conexão_com_o_banco_de_dados import Conexão

dado = Conexão()

conexão = connect(
    host= dado.get_dado()[0],
    user= dado.get_dado()[1],
    password= dado.get_dado()[2]
)

cursor = conexão.cursor()
cursor.execute('SHOW DATABASES')

for x in cursor:
    print(x)