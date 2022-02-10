import qrcode
import os
from tkinter import filedialog
from datetime import datetime as date 

link = input(str('Insira o link da rota para o QRCode: '))
image_qrcode =qrcode.make(link)

motorista = input(str('Qual o motorista:  '))
data = date.today().strftime('%Y-%m-%d')
regiao = input(str('Qual a região de entrega: '))


nm_arq = motorista + ' ' + data + ' ' + regiao + '.png'
#
destino = filedialog.askdirectory()


image_qrcode.save(os.path.join(destino, nm_arq))


