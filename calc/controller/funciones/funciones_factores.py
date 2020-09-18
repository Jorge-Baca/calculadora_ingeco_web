"""
Created on 2/08/2020
@author: Jorge Miguel Baca
__author__: "Diego Ramirez, Jorge Baca"
__copyright__: "Copyright 2020"
__license__: "GLP"
__version__: "1.0.1"
__emalil__: "jorge.baca@pucp.edu.pe"
__status__: "Production"
"""
#uso de python3 -> 3.6.8
import math
from sympy import symbols, Eq, solve, solveset

def InteresSimple(interes, tiempo):
    if isinstance(interes, str):
        interes = symbols('interes')
    elif isinstance(tiempo, str):
        tiempo = symbols('tiempo')
    interes = interes/100
    return interes*tiempo

def CambioTasaEfec(interes, pNuevo):
    if isinstance(interes, str):
        interes = symbols('interes')
    elif isinstance(tiempo, str):
        tiempo = symbols('tiempo')
    interes = interes/100
    fin = (1+interes)**pNuevo
    fin = (fin-1)/100
    return fin

def FDP(interes, tiempo):
    if isinstance(interes, str):
        interes = symbols('interes')
    elif isinstance(tiempo, str):
        tiempo = symbols('tiempo')
    interes = interes/100
    x = pow((1+interes),tiempo)
    return x

def PDF(interes, tiempo):
    if isinstance(interes, str):
        interes = symbols('interes')
    elif isinstance(tiempo, str):
        tiempo = symbols('tiempo')
    interes = interes/100
    x = 1/pow((1+interes),tiempo)
    return x


def FDA(interes, tiempo):
    if isinstance(interes, str):
        interes = symbols('interes')
    elif isinstance(tiempo, str):
        tiempo = symbols('tiempo')
    interes = interes/100
    x = pow((1+interes),tiempo)-1
    return x/interes

def PDA(interes, tiempo):
    if isinstance(interes, str):
        interes = symbols('interes')
    elif isinstance(tiempo, str):
        tiempo = symbols('tiempo')
    interes = interes/100
    exp = pow(1+interes,tiempo)
    x = (exp-1)/(interes*exp)
    return x

def FDG(interes, tiempo):
    if isinstance(interes, str):
        interes = symbols('interes')
    elif isinstance(tiempo, str):
        tiempo = symbols('tiempo')
    interes = interes/100
    exp = pow(1+interes,tiempo) - interes*tiempo
    x = (exp-1)/pow(interes,2)
    return x

def PDG(interes, tiempo):
    if isinstance(interes, str):
        interes = symbols('interes')
    elif isinstance(tiempo, str):
        tiempo = symbols('tiempo')
    interes = interes/100
    exp = pow(1+interes,tiempo)
    x = (exp-(interes*tiempo)-1)/(pow(interes,2)*exp)
    return x

def PDAG(tasa, interes, tiempo):
    if isinstance(interes, str):
        interes = symbols('interes')
    elif isinstance(tasa, str):
        tasa = symbols('tasa')
    elif isinstance(tiempo, str):
        tiempo = symbols('tiempo')
    tasa = tasa/100
    interes = interes/100
    if interes == tasa:
        x = tiempo/(1+interes)
    else:
        exp = 1 - pow((1+tasa)/(1+interes), tiempo)
        x = exp/(interes-tasa)
    return x
