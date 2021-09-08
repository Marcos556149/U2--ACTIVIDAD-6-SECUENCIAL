from ClaseCola import Cola
if __name__=='__main__':
    maximo=int(input('Ingrese el tamaño de la cola: '))
    unaCola=Cola(maximo)
    unaCola.insertar(4)
    unaCola.insertar(89)
    unaCola.insertar(7)
    unaCola.recorrer()
