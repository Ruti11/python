from reproductor import *
from tkinter import *

musica = Reproductor("another_love.mp3")
resp = ""
def play_musica():
    resp = musica.play()


master = Tk()
master.geometry("200x200")
master.title("Reproductor de Windows")

etiqueta = Label(master, text = "Desarrollado por Rut")
etiqueta.pack(pady = 5 )

btn_play = Button(master, text="play", command=play_musica)

btn_play.pack(pady = 10)

mainloop()