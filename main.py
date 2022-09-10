import PySimpleGUI as sg
import tkinter as tk

from cotacao import pegar_cotacoes

layout=[
    [sg.Text("Cambio de Moeda")],
    [sg.InputText(key="nome_moeda")],
    [sg.Button("Pegar Cotação"),sg.Button("Cancelar")],
    [sg.Text(key="text_moeda")],
]
janela=sg.Window("Titulo da Janela",layout)
while True:
    event,value=janela.read()
    if event==sg.WIN_CLOSED or event=="Cancelar":
        break
    if event=="Pegar Cotação":
        name_moeda=value["nome_moeda"]
        moeda=pegar_cotacoes(name_moeda)
        janela["text_moeda"].update(f"O cambio do {name_moeda} é de {moeda}")

janela.close()
