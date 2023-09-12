from helium import *
from login import *
# from time import sleep


def wait_until_exists(word):
    keep = True
    while keep:
        try: 
            wait_until(Text(word).exists)
            keep = False
        except: pass


# LINK DA PLANILHA
link = "https://docs.google.com/spreadsheets/d/1WAUGezrlXr7-qec3uzMey76M_QQkcwZx/edit#gid=1126414855"

helium.start_firefox(link)
wait_until_exists("Fazer login")
write(login, into="E-mail ou telefone")
press(ENTER)
wait_until_exists("Olá")
write(senha, into="Digite sua senha")
press(ENTER)

# Na planilha
wait_until_exists('Arquivo')
click(Text('Arquivo'))
wait_until_exists('Fazer Download')
click(Text('Fazer Download'))
wait_until_exists('Microsoft Excel (.xlsx)')
click(Text('Microsoft Excel (.xlsx)'))

# Planilha salva na pasta downloads (tudo certo até aqui)