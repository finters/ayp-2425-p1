entrada=input("ingrese sus pasos").lower()
coordenadas=[int(0),int(0)]
posiciones=[[0,0]]
tamaño=int(len(entrada))
def posicion (x):
    n=int(0)
    while n< tamaño:
        if x[n]=="e":
            coordenadas[0]+=1
        elif x[n]=="w":
            coordenadas[0]-=1
        elif x[n]=="n":
            coordenadas[1]+=1
        elif x[n]=="s":
            coordenadas[1]-=1
        posiciones.append((coordenadas))
        print(posiciones)
        print(coordenadas)
        n+=1


print(entrada)
posicion(entrada)

