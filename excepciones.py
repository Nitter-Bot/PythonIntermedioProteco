#Curso python intermedio    Samuel Hernandez Chavez
#Programa que calculara el imc usando excepciones

def datos():
    peso,altura = 0,0
    #Pedir peso
    while peso<=0:
        try:
            peso = float(input("\nIngresa tu peso en kg : "))
            if peso<=0:
                print("Ingresa solo numeros positivos mayores a 0")
        except:
            print("Ingresa solo numeros")
    
    #Pedir altura
    while altura<=0 or altura>=3:
        try:

            altura = float(input("\nIngresa tu altura en metros: "))
            if altura<=0:
                print("\aIngresa numeros positivos mayores a 0")
            elif altura>=3:
                print("\aPorfavor nadie mide mas de 3 metros")

        except:
            print("\aSolo ingresa un numero en metros")

    return peso,altura

def imc(kg,m):
    indice = kg/(m**2)
    return indice


#Funcion principal
try:
    #Pedimos los datos 
    x,y = datos()
    
    #Sacamos el imc y lo redondeamos con 2 decimales
    z=round(imc(x,y),2)

    #Imprimimos los daos
    print(f"Tu indice de maza corporal es: {z}")
    print("Esto indica que: ")

    #Determinamos una leyenda de acuerdo al IMC
    if z<18.5:
        print("\tEstas bajo de peso")
    elif z>25:
        print("\tTienes sobrepeso")
    else:
        print("\tEstas en el peso saludable")
    
except:
    print("Solo ingresa numeros")
