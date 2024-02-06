from pygame import mixer
class Reproductor:
    #atributos
    archivo = None

    #constructor
    def __init__(self, archivo):
        self.archivo = archivo
        mixer.init()
        mixer.music.load(archivo)

    def play(self):
        mixer.music.play()
        return"Reproduciendo música"

    def pause(self):
        mixer.music.pause()
        return "La música se ha pausado"

    def stop(self):
        mixer.music.pause()
        return"La música se detuvo"

    def volume (self, v):
        mixer.music.set_volume(v)
        return "Definiendo volumen a", (100*v), "%"

if __name__ == "__main__":
    file ="another_love.mp3"
    musica = Reproductor(file)
    while True:
        print("1- PLAY  | 2- PAUSE | 3- STOP | 4- VOL")
        accion = int(input("Opción: "))
        if(accion == 1):
            resp = musica.play()

        if(accion == 2):
            rep = musica.pause()

        if(accion == 3):
            resp = musica.stop()

        if(accion == 4):
            vol = float(input("volumen"))
            resp = musica.volume(vol)



        print(resp)

