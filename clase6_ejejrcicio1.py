import os
resp = 1
while resp != 0:
    print("Paint (1)")
    print("classroom (2)")
    print("Apagar la PC en 2 horas (3)")
    print("Salir (0)")
    resp = int(input("Selecione: "))
    if(resp == 1):
        os.system("mspaint")
    elif(resp == 2):
        os.system("start msedge classroom.google.com")
    elif(resp == 3):
        os.syste("shutdown -s -t 7200")
    else:
        print("No comprendo esa orden")

        