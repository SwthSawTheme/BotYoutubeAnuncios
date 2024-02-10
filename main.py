import pyautogui as py
import time
import os
import threading
import tkinter as tk

# Classe onde irei fazer de forma ordenada todos os métodos para a execução do bot!
class Bot:
    def __init__(self):
        # threading.Event() para sinalizar a parada do bot
        self.parar_event = threading.Event()
        # Configuração da janela de controle
        self.janela_parada()

    def verificar_e_clicar(self):
        imagens = ["pular1.png", "pular2.png", "pular3.png","pular4.png","pular5.png","pular6.png","pular7.png","pular8.png","pular9.png","pular10.png"]
        while not self.parar_event.is_set():
            for imagem in imagens:
                try:
                    ico = os.path.join("assets/", imagem)
                    position = py.locateCenterOnScreen(ico, confidence=0.7)
                    if position:
                        py.click(position)
                        time.sleep(0.5)
                except py.ImageNotFoundException:
                    time.sleep(0.5)

    def janela_parada(self):
        # Configuração da janela de controle usando Tkinter
        self.root = tk.Tk()
        self.root.title('BotAnuncio - Controle')
        
        label = tk.Label(self.root, text='Clique em "Parar" para encerrar o bot.')
        label.pack()

        # Botão para parar o bot
        botao_parar = tk.Button(self.root, text='Parar', command=self.parar_bot)
        botao_parar.pack()

        # Configuração para fechar a janela
        self.root.protocol("WM_DELETE_WINDOW", self.fechar_janela)

    def parar_bot(self):
        # Função chamada quando o bot é parado pelo usuário
        self.parar_event.set()  # Sinaliza a parada do bot
        self.root.destroy()     # Fecha a janela

    def fechar_janela(self):
        # Função chamada quando a janela é fechada pelo usuário
        self.parar_event.set()  # Sinaliza a parada do bot
        self.root.destroy()     # Fecha a janela

    def iniciar_bot(self):
        # Inicia a verificação em uma thread separada
        self.thread_verificacao = threading.Thread(target=self.verificar_e_clicar)
        self.thread_verificacao.start()

        # Inicia o loop de eventos da GUI
        self.root.mainloop()

        # Aguarda o término da thread de verificação
        self.thread_verificacao.join()

# Verifica se o código está sendo executado como script principal
if __name__ == "__main__":
    bot = Bot()
    bot.iniciar_bot()

