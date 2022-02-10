from optparse import Values
import qrcode
import os
import PySimpleGUI as sg
from tkinter import Button, filedialog
from datetime import datetime as date 

class RotaGUI():
    def __init__(self):
        layout = [
            [sg.Text('Insira o link da rota: '), sg.Input(key='link')],
            [sg.Text('Motorista'), sg.Input(key='motorista')],
            [sg.Text('Data da rota: '+date.today().strftime('%Y-%m-%d'))],
            [sg.Text('Região'), sg.Input(key='regiao')],
            [sg.Button('Confirmar')]
        ]

        janela = sg.Window('Rota em QRCode').layout(layout)

        while True:
            self.button, self.values = janela.Read()

            def Iniciar(self):
                link = self.values['link']
                motorista = self.values['motorista']
                regiao = self.values['regiao']
                if self.button == 'Confirmar':
                    img = qrcode.make(link)
                    nome_arq = motorista + ' ' + date.today().strftime('%Y-%m-%d') + ' ' + regiao
                    destino = filedialog.askdirectory()
                    img.save(os.path.join(destino, nome_arq))

        

    

rota = RotaGUI()
rota.Iniciar()

