#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      anderson
#
# Created:     15/08/2017
# Copyright:   (c) anderson 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Cola:
    def __init__(self):
        self.__datos = []

    def meter(self,valor):
        self.__datos.append(valor)

    def primero(self):
        return self.__datos[0]

    def sacar(self):
        p_ult = len(self.__datos) 
        if (p_ult > 0):
            self.__datos.pop(0)
    def getLista(self):
        return self.__datos

    def numElem(self):
        return int(len(self.__datos))


    