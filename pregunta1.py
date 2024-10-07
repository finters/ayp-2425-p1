entrada=[str(x) for x in input("ingrese palabras").lower().split( )]
valores=[False,False,False]
aprobados=[]
def verificador(a):
    contador=0
    while contador <= len(a):
        for n in a:
            if n == "a" or "s" or "d" or "f"or "g"or "h"or "j" or "k" or "l" or "l" or "ñ":
                valores[1]=True
            if n == "q" or "w" or "e" or "r"or "t"or "y"or "u" or "i" or "o" or "p":
                valores[0]=True
            if n == "z" or "x" or "c" or "v"or "b"or "n"or "m" or "," or ".":
                valores[2]=True
        if  valores[0] and valores[1]==False:
            aprobados.append(n)
        elif valores[0] and valores[2]==False:
            aprobados.append(n)
        elif valores[1] and valores[2]==False:
            aprobados.append(n)
    contador+=1

verificador(entrada)
print(aprobados)
    