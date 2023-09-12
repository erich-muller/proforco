import pymysql

# Conectando ao banco de dadps
def createConnection(local=False):
    # Dados do banco de dados online

    bd_online = {
        'host': 'sql10.freesqldatabase.com',
        'name': 'sql10645816',
        'user': 'sql10645816',
        'password': 'tIP7ncYq7c',
        'port': 3306
    }

    bd_local = {
        'host': 'localhost',
        'name': 'proforco',
        'user': 'root',
        'password': '',
        'number': 3306
    }
    
    bd = bd_local if local else bd_online
    connection = pymysql.connect(host=bd['host'], user=bd['user'], password=bd['password'], database=bd['name'])
    return connection
