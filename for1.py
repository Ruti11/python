promedio_general = 0
total = 0
cantidad = 0
calificacion = 1
while(calificacion != 0):
    #se permite solamente del 1 al 5 
    #while...if
 
    calificacion = int(input("Ing calif: "))

    if(calificacion >=1 and calificacion <= 5):
        
        total += calificacion
        cantidad += 1
    elif(calificacion == 0):
        print("______________")
        continue
    else:
        print("Ingrese del 1 al 5")
promedio_general = total / cantidad

print(f"El promedio general es {promedio_general}")

