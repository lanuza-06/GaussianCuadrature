#!/usr/bin/env python3

"""
Utilización de Cuadratura Gaussiana para la solución de está integral:
I = ∫_1^3 dx [ x^6 - x^2 sin(2x) ] 

Debe incluir:
    @Solución analítica de la Integral
    @Funciones para obtener los pesos (Leggauss)
    @Funcion cuadratura que calcule el valor
    @Comprobación del valor de N mínimo para la tolerancia
"""


#Resumen
"""
- funciones gaussxw / gaussxwab (usando numpy, según el lab 4)
- rutina de integración por cuadratura Gauss-Legendre
- ejemplo polinomial (f(x) = x^4 - 2 x^3 + 1) en [0,2] con N=2,3,4 (muestra por qué N=3 es exacto) (En el caso de la integral será otro valor de N)
- integración del problema original: I = ∫_1^3 ( x^6 - x^2 sin(2x) ) dx
  * expresión analítica cerrada y valor numéricoi
  * tabla de convergencia para N=1..Nmax y búsqueda del N mínimo para una tolerancia dada

"""
 #Código

from scipy.special import legendre
import matplotlib.pyplot as plt
import numpy as np


#Acá en esta parte definimos la función que da los polinomios de Legendre(IMPORTANTE) de grado N
#--------------POLINOMIOS DE LEGENDRE-----------------------

def GaussLegendrexW(N): 
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def GaussXWAB(a, b, x, w):
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

#Acá defino la función a integrar y estudiar

def FuncIntegrar(x):
    return (x ** 6) - ( x ** 2) * np.sin(2.0 * x)

#Hacer que lo calcule para N valores, que me de la gana

#-------------------Valor Exacto----------------
def ValorExacto_1_a_3():
    """Para integral en [1, 3]"""
    def F(x):
        return (x**7)/7.0 + (x**2 * np.cos(2*x))/2.0 - (x * np.sin(2*x))/2.0 - np.cos(2*x)/4.0
    
    return F(3.0) - F(1.0)
#-----------------------------------------------
def CalcIntegrales(NValores):
    ResultadosInt = {}
    for N in NValores:
        #Obtener los puntos y pesos para los hps valores de N
        xBase, wBase = GaussLegendrexW(N)
        #Transformar en el intervalo dado [1, 3]
        xTrans, wTrans = GaussXWAB (1, 3, xBase, wBase)

        #Calcular la integral
        ResultadosInt[N] = np.sum(wTrans * FuncIntegrar(xTrans))

    return ResultadosInt

#El main()

if __name__ == "__main__":
    print("Ingresar los valores de N separados por comas (ejemplo: 2,3,4,5,...,N")
    Entrada = input().strip()
    NLista = [int(n) for n in Entrada.split(',')]

    #Imprimir valor analítico

    exacto = ValorExacto_1_a_3()
    print(f"\nValor exacto analítico: {exacto:.16f}\n")

    #Calcular todas las Integrales
    ResultadosInt = CalcIntegrales(NLista)
    
    #Mostrar el resultado de las integrales según cada valor de N
    print("\nResultados de la integración:")
    for N, valor in ResultadosInt.items():
        error = abs(valor - exacto)
        print(f"N = {N} : {valor:20.12f} Error = {error: .3e} ")
        


                           
    




