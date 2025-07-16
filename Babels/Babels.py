import random
def convertir(num):
    lista=[]
    i=0
    while i <3:
        lista.insert(0,num%10)
        num=int(num/10)
        i+=1
    return lista

def buscar(num1,num2):
    lista1=convertir(num1)
    lista2=convertir(num2)
    contador=0
    pico=0
    fermi=0
    for i in range(3):
        for j in range(3):
            if lista1[i]==lista2[j] and i!=j:
                print('Pico')
                pico+=1
            elif lista1[i]==lista2[j] and i==j:
                print('Fermi')
                fermi+=1
                contador+=1
    if pico==0 and fermi==0:
        print('Bagels')
    if contador==3:
        print('Ganaste')


def main():
    numero_adivinar=random.randint(100,999)
    contador=0
    while contador<10:
        num=int(input("Introduce el numero: "))
        buscar(num,numero_adivinar)
        contador+=1

    print('Perdiste')
    print('El numero era: ',numero_adivinar)

main()