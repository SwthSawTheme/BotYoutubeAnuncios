import pyautogui as py
import time
import os
import threading
import tkinter as tk

class Bot:
    def __init__(self):
        self.parar_event = threading.Event()
        self.janela_parada()

    def verificar_e_clicar(self):
        while not self.parar_event.is_set():
            try:
                ico = os.path.join("assets/pular.png")
                position = py.locateOnScreen(ico, confidence=0.7)
                if position:
                    py.click(position)
                    time.sleep(1)  # Adiciona um atraso após o clique
                    print('Imagem Encontrada!')
            except py.ImageNotFoundException:
                time.sleep(1)
                print('Não foi encontrado imagem na tela!')

    def janela_parada(self):
        self.root = tk.Tk()
        self.root.title('BotAnuncio - Controle')
        
        label = tk.Label(self.root, text='Clique em "Parar" para encerrar o bot.')
        label.pack()

        botao_parar = tk.Button(self.root, text='Parar', command=self.parar_bot)
        botao_parar.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.fechar_janela)

    def parar_bot(self):
        print('Bot encerrado pelo usuário.')
        self.parar_event.set()
        self.root.destroy()

    def fechar_janela(self):
        print('Bot encerrado pelo usuário.')
        self.parar_event.set()
        self.root.destroy()

    def iniciar_bot(self):
        # Inicia a verificação em uma thread separada
        self.thread_verificacao = threading.Thread(target=self.verificar_e_clicar)
        self.thread_verificacao.start()

        # Inicia o loop de eventos da GUI
        self.root.mainloop()

        # Aguarda o término da thread de verificação
        self.thread_verificacao.join()

if __name__ == "__main__":
    bot = Bot()
    bot.iniciar_bot()
