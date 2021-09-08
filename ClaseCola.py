import numpy as np
class Cola:
    __items= None
    __pr=0
    __ul=0
    __cant=0
    __max=0
    def __init__(self,xmax):
        self.__items= np.empty(xmax,dtype=int)
        self.__max= xmax
    def vacia(self):
        return self.__cant == 0
    def insertar(self,x):
        if self.__cant < self.__max:
            self.__items[self.__ul]=x
            self.__ul=(self.__ul + 1)%self.__max
            self.__cant += 1
            return x
        else:
            print("Cola llena")
    def suprimir(self):
        if self.vacia():
            print("Pila Vacia")
            return 0
        else:
            x= self.__items[self.__pr]
            self.__pr= (self.__pr + 1)%self.__max
            self.__cant -= 1
            return x
    def recorrer(self):
        if self.vacia() == False:
            for i in range(self.__cant):
                print(self.__items[(self.__pr+i)%self.__max])
            


