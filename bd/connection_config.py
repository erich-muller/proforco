import pymysql

# Conectando ao banco de dadps
def createConnection(local=True):
    # Dados do banco de dados online
    
    bd_online = {
        'host': 'sql10.freesqldatabase.com',
        'name': 'sql10620948',
        'user': 'sql10620948',
        'password': 'nCZyq6rlFj',
        'port': 3306
    }

    bd_local1 = {
        'host': 'localhost',
        'name': 'sisu',
        'user': 'root',
        'password': '',
        'port': 3306
    }

    bd_local2 = {
        'host': 'localhost',
        'name': 'proforco',
        'user': 'root',
        'password': '',
        'number': 3306
    }
    
    bd = bd_local2 if local else bd_online
    connection = pymysql.connect(host=bd['host'], user=bd['user'], password=bd['password'], database=bd['name'])
    return connection
