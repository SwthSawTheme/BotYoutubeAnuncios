import pyautogui as py
import time
import os


def Anuncio():
    py.confirm(text='Olá, vamos começar com a automação!', title='BotAnuncio', buttons=['Iniciar', 'Cancelar'])
    while True:
        try:
            time.sleep(1)
            ico = os.path.join("assets/pular.png")
            position = py.locateCenterOnScreen(ico,confidence=0.7)
            
        except:
            time.sleep(1)
            print('Não foi encontrado imagem na tela!')
        else:
            py.click(position)
            print('Imagem Encontrada!')
        
            
Anuncio()
quit()   

