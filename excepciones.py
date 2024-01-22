#Curso python intermedio    Samuel Hernandez Chavez
#Programa que calculara el imc usando excepciones

def datos():
    peso,altura = 0,0
    while peso<=0:
        try:
            peso = float(input("\nIngresa tu peso en kg : "))
            if peso<=0:
                print("Ingresa solo numeros positivos mayores a 0")
        except:
            print("Ingresa solo numeros")
    while altura<=0 or altura>=3:
        try:

            altura = float(input("\nIngresa tu altura en metros: "))
            if altura<=0:
                print("\aIngresa numeros positivos mayores a 0")
            elif altura>=0:
                print("\aPorfavor nadie mide mas de 3 metros")

        except:
            print("\aSolo ingresa un numero en metros")

    return peso,altura


try:
    x,y = datos()

    print(x)
    print(y)
except:
    print("Solo ingresa numeros")
