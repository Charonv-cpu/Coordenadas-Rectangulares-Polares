from pydoc import ModuleScanner
import numpy as np
import matplotlib.pyplot as plt
from math import acos, degrees
from sympy import *
from tkinter import *
from tkinter import messagebox
import math
import tkinter as tk 

#DECLARANDO LA INTETFAZ DE USUARIO
ventana = Tk()
ventana.title("Coordenadas rectangulares a polares")
ventana.geometry("350x400")
ventana.resizable(False,False)

plt.axes(projection = 'polar')



valorEjeX = IntVar()
valorX = Entry(ventana, textvariable=valorEjeX)

valroEjeY = IntVar()
valorY = Entry(ventana, textvariable=valroEjeY)

esoacui = Label(ventana, text=" ", width=2, height=17)
informacion = Label(ventana, text="                               Version: 0.1")


valorX.grid(column=1, row=0)
valorY.grid(column=1, row=1)
esoacui.grid(column=1, row=5)
informacion.grid(column=1,row=6)


def clear():
    valorEjeX = 0
    valroEjeY = 0

def globalTotal():

    def grafica():
        y = valroEjeY.get()
        x = valorEjeX.get()
        distancia = np.sqrt(x**2 + y**2)

    #Obteniendo la operación de la tangente menos 1
        div = (x/y)


        tangenteMenoUno = np.arctan(div) #Valo de 0.6435
        inv_tan1 = atan(div) #valor de 0.6435
        conversion = (math.pi / div) #valor de 4.1887
        conversion2 = degrees(pi/div)#valor de 0.119366
        conversion3 = ((math.pi/2) * div /math.pi)#valor de 0.375
        conversion4 = np.rad2deg(tangenteMenoUno)
        grados = "{0:.2f}".format(conversion4)


        print("Valor de X en distancia: " + "{0:.2f}".format(distancia))
        print("Valor de la converión Grados: " + "{0:.2f}".format(conversion4))


        plt.scatter(y=distancia, x=conversion4)
        plt.show()

    def salir():
        extension = messagebox.askyesno(message="¿Segur@ que quieres cerrar el programa'", title="Finalizar")
        if extension == True:
            ventana.destroy()

    def mas():
        messagebox.askyesnocancel(message="Programa desarrollado por Ricardo Escobedo, version 0.1", title="Informacion")

    def mensajes():
        indicadorX = Label(ventana, text="Ingresa la coordenada X: ")
        indicadorY = Label(ventana, text="Ingresa la coordenada Y: ")

        indicadorX.grid(column=0, row=0)
        indicadorY.grid(column=0, row=1)

    def botones():
        graficar = Button(ventana, text="Graficar", font="Arial 10", width=12, command=grafica)
        mostrar = Button(ventana, text="Mostrar", font="Arial 10", width=12)
        cerar = Button(ventana, text="Cerrar", font="Arial 10", width=12, command=salir)
        #informacion = Button(ventana, text="Informacion", font="Arial 10", width=12, command=mas)
        #espacio = Label(ventana, text="", width=15, height=2)
        cuadrado = Button(ventana, text="x² Numero",font="Arial 10", width=12)
        nuevo = Button(ventana, text="Nuevo Punto",font="Arial 10", width=12, command=clear)

        # espacio.grid(column=0, row=2)
        graficar.grid(column=0, row=3)
        nuevo.grid(column=1, row=3)
        cuadrado.grid(column=0, row=4)
        cerar.grid(column=1, row=4)
        #informacion.grid(column=0, row=5)


    mensajes()
    botones()
    ventana.mainloop()

globalTotal()