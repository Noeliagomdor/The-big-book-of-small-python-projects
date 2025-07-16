frecuencia = [['a', 0, 0.1253], ['b', 1, 0.0142], ['c', 2, 0.0468], ['d', 3, 
    0.0586], ['e', 4, 0.1368], ['f', 5, 0.0069], ['g', 6, 0.0101], ['h', 7, 
    0.007], ['i', 8, 0.0625], ['j', 9, 0.0044], ['k', 10, 0.0001], ['l', 11, 
    0.0497], ['m', 12, 0.0315], ['n', 13, 0.0671], ['ñ', 14, 0.0031], ['o', 
    15, 0.0868], ['p', 16, 0.0251], ['q', 17, 0.0088], ['r', 18, 
    0.0687], ['s', 19, 0.0798], ['t', 20, 0.0463], ['u', 21, 0.0393], ['v', 
    22, 0.009], ['w', 23, 0.0002], ['x', 24, 0.0022], ['y', 25, 0.009], ['z', 
    26, 0.0052]]

Alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def Indice_Mixto(w):
    suma=0
    for i in frecuencia:
        suma=suma + i[2]*(w.count(i[0])/len(w))
    return suma

def traducdir(frecuencia,elemento):
    for j in frecuencia:
        if j[0]==elemento:
            return j[1]
        

def traducinv(frecuencia,numero):
    for j in frecuencia:
        if j[1]==numero:
            return j[0]

def decodificar(car1, car2):
    num1 = traducdir(frecuencia, car1)
    num2 = traducdir(frecuencia, car2)
    num = (num1 + num2) % 27
    return traducinv(frecuencia, num)



def clave_cesar():
    mensaje = input("Introduce el  mensaje encriptado: ")
    longitud = len(mensaje)
    lista = []
    
    for i in range(27):
        desencriptado = []  # Aquí se inicializa correctamente
        for j in range(longitud):
            desencriptado.append(decodificar(mensaje[j], Alfabeto[i]))
        lista.append([Alfabeto[i], Indice_Mixto(desencriptado)])
    
    return lista


list=clave_cesar()
print(list)





