'''Passo a passo do preojeto
Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
Passo 2: Fazer login 
Passo 3: Importar a base de dados de produtos
Passo 4: cadastrar 1 produto
Passo 5: repetir o cadastro para todos os produtos
'''

# Bliblioteca é um pacote de dados feitos por outros programadores para automatizar

import pyautogui
import time

# NaN - not a number
# pyautogui.click -> Clicar com o meu mouse 
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> atalho (combinação de teclas)
# pyautogui.PAUSE = 1 / ele executa as ações 1 de cada vez esperando o tempo que eu determinar dps do =
pyautogui.PAUSE = 0.3

# abrir o chrome
pyautogui.press('win') 
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

# esperar o site carregar Marca Tipo    Categoria   Preco   Custo   Obs 
time.sleep(3)

# Passo 2: Fazer login 
##pyautogui.click(x=773, y=455, button='left')
##pyautogui.click(x=773, y=455)
pyautogui.press('tab')  # passar para o camp de email
pyautogui.write('Marques_bertin@hotmail.com')
pyautogui.press('tab') # passar para o camp de senha
pyautogui.write('12345')
pyautogui.press('tab') # passando para o botão entrar
pyautogui.press('enter')
time.sleep(1)

#Passo 3: Importar a base de dados de produtos
# pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

#Passo 4: cadastrar 1 produto
    pyautogui.click(x=713, y=281) # código do produto

    codigo = tabela.loc[linha, 'codigo']  # nome da variavel(linha) e nome (da coluna como esta no documeto).
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']

    # Preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs= tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # Apertar para enviar
    pyautogui.press('tab')
    pyautogui.press('enter')

    #fazendo o scroll
    pyautogui.scroll(5000) 
    
# scroll para cima com valor positivo
# pyautogui.scroll(-500) -> scroll para baixa com valor negativo

#Passo 5: repetir o cadastro para todos os produtos