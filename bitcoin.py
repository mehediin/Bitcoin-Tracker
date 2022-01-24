import requests
import tkinter as tk
from datetime import datetime

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,BRL"
    response = requests.get(url).json()
    price = response["BRL"]
    time = datetime.now().strftime("%H:%M:%S")

    LabelPrice.config(text = str(price) + " R$")
    LabelTime.config(text = "Atualizado em: "+ time)

    canvas.after(1000, trackBitcoin)

canvas = tk.Tk()
 # canvas.configure(bg = 'blue') troca a cor do app
canvas.tk.call("wm", "iconphoto", canvas._w, tk.PhotoImage(file = 'C:/Users/jpmeh/Desktop/VSCode/Curso de Python/bitcoin.png'))# pega o icone como .png
canvas.geometry("400x500")
canvas.title("Bitcoin Stock")
# fontes
f1 = ("poppins", 24, "bold")
f2 = ("poppins", 24,"bold")
f3 = ("poppins", 18, "normal")


Label = tk.Label(canvas,text = "Bitcoin Preço", font = f1)
Label.pack(pady = 20)

LabelPrice = tk.Label(canvas, font= f2)
LabelPrice.pack(pady= 20)

LabelTime = tk.Label(canvas, font = f3)
LabelTime.pack(pady = 20)


trackBitcoin ()
canvas.mainloop()
