"""
Created on 4/08/2020
@author: Jorge Miguel Baca
__author__: "Diego Ramirez, Jorge Baca"
__copyright__: "Copyright 2020"
__license__: "GLP"
__version__: "1.0.1"
__emalil__: "jorge.baca@pucp.edu.pe"
__status__: "Production"
"""
import math
from sympy import symbols, Eq, solve, solveset

def ADP(interes, tiempo):
    if isinstance(interes, str):
        interes = symbols('interes')
    elif isinstance(tiempo, str):
        tiempo = symbols('tiempo')
    interes = interes/100
    equ = pow(1+interes,tiempo)
    x = (interes*equ)/(equ-1)
    return x

def intEfecAdel(interes):
    if isinstance(interes, str):
        interes = symbols('interes')
    interes = interes/100
    x = (interes/(1-interes))*100
    return x

def cuotasConst(monto, interes, tiempo):
    total_amort = 0
    total_int = 0
    total_cuot = 0

    cuota = monto*ADP(interes, tiempo)
    interes = interes/100
    sdi = monto
    mat = []
    mat.append(["Saldo inicial", "Intereses", "Cuota", "Saldo Final"])

    for i in range(1,tiempo+1):
        mat.append([])
        mat[i].append(sdi)
        intereses = sdi*interes
        amortiz = cuota-intereses
        mat[i].append(amortiz)
        mat[i].append(intereses)
        mat[i].append(cuota)
        sdf = sdi-amortiz
        mat[i].append(sdf)
        sdi = sdf
        total_amort = total_amort + amortiz
        total_int = total_int + intereses
        total_cuot = total_cuot + cuota

    mat.append([0, total_amort, total_int, total_cuot, 0])
    return mat

def amortizacionConst(monto, interes, tiempo):
    total_amort = 0
    total_int = 0
    total_cuot = 0

    amortiz = monto/tiempo
    interes = interes/100
    sdi = monto
    mat = []
    mat.append(["Saldo inicial", "Amortizacion", "Intereses", "Cuota", "Saldo Final"])

    for i in range(1,tiempo+1):
        mat.append([])
        mat[i].append(sdi)
        intereses = sdi*interes
        cuota = amortiz-intereses
        mat[i].append(amortiz)
        mat[i].append(intereses)
        mat[i].append(cuota)
        sdf = sdi-amortiz
        mat[i].append(sdf)
        sdi = sdf
        total_amort = total_amort + amortiz
        total_int = total_int + intereses
        total_cuot = total_cuot + cuota

    mat.append([0, total_amort, total_int, total_cuot, 0])
    return mat

def cuotaCreciente(monto, interes, tiempo):
    total_amort = 0
    total_int = 0
    total_cuot = 0

    sdd = tiempo*(tiempo+1)/2
    interes = interes/100
    sdi = monto
    mat = []
    mat.append(["Saldo inicial", "Amortizacion", "Intereses", "Cuota", "Saldo Final"])

    for i in range(1,tiempo+1):
        mat.append([])
        mat[i].append(sdi)
        factor = i/sdd
        amortiz = factor*monto
        intereses = sdi*interes
        cuota = amortiz+intereses
        mat[i].append(amortiz)
        mat[i].append(intereses)
        mat[i].append(cuota)
        sdf = sdi-amortiz
        mat[i].append(sdf)
        sdi = sdf
        total_amort = total_amort + amortiz
        total_int = total_int + intereses
        total_cuot = total_cuot + cuota

    mat.append([0, total_amort, total_int, total_cuot, 0])
    return mat

def periodosGracia(monto, interes, tiempo):
    interes = interes/100
    sdi = monto
    intereses = sdi*interes
    sdf = sdi
    mat = []
    mat.append(["Saldo inicial", "Amortizacion", "Intereses", "Cuota", "Saldo Final"])

    for i in range(1,tiempo+1):
        mat.append([])
        mat[i].append(sdi)
        mat[i].append(0)
        mat[i].append(intereses)
        mat[i].append(intereses)
        mat[i].append(sdi)

    return mat

def periodoGraciaTotal(monto, interes, tiempo):
    sdi = monto
    interes = interes/100
    mat = []
    mat.append(["Saldo inicial", "Amortizacion", "Intereses", "Cuota", "Saldo Final"])

    for i in range(1,tiempo+1):
        mat.append([])
        sdf = sdi*(1+interes)
        mat[i].append(sdi)
        mat[i].append(0)
        mat[i].append(0)
        mat[i].append(0)
        mat[i].append(sdf)
        sdi = sdf

    return mat

def intAdelCuotas(monto, interes, tiempo):
    total_amort = 0
    total_int = 0
    total_cuot = 0

    interes = interes/100
    cuota = (monto-(interes*monto))*ADP(intEfecAdel(interes*100), tiempo) 
    mat = []
    mat.append(["Saldo inicial", "Amortizacion", "Intereses", "Cuota", "Saldo Final"])

    for i in range(1,tiempo+3):
        mat.append([0,0,0,0,0])

    mat[tiempo+1] = [cuota, cuota, 0, cuota, 0]
    total_amort = cuota
    total_cuot = cuota
    mat[1] = [monto, 0, monto*interes, 0, monto]

    for i in range(tiempo, 1, -1):
        sdf = mat[i+1][0]
        intereses = mat[i+1][0]*interes
        amortiz = cuota - intereses
        sdi = sdf + amortiz
        mat[i] = [sdi, amortiz, intereses, cuota, sdf]
        total_amort = total_amort + amortiz
        total_int = total_int + intereses
        total_cuot = total_cuot + cuota


    mat[tiempo+2] = [0, total_amort, total_int, total_cuot, 0]
    return mat

def intAdelAmortizado(monto, interes, tiempo):
    total_amort = 0
    total_int = 0
    total_cuot = 0

    interes = interes/100
    amortiz = monto/tiempo
    mat = []
    mat.append(["Saldo inicial", "Amortizacion", "Intereses", "Cuota", "Saldo Final"])

    for i in range(1,tiempo+3):
        mat.append([0,0,0,0,0])

    mat[tiempo+1] = [amortiz, amortiz, 0, amortiz, 0]
    total_amort = amortiz
    total_cuot = amortiz
    mat[1] = [monto, 0, monto*interes, 0, monto]

    for i in range(tiempo, 1, -1):
        sdf = mat[i+1][0]
        intereses = mat[i+1][0]*interes
        cuota = amortiz + intereses
        sdi = sdf + amortiz
        mat[i] = [sdi, amortiz, intereses, cuota, sdf]
        total_amort = total_amort + amortiz
        total_int = total_int + intereses
        total_cuot = total_cuot + cuota


    mat[tiempo+2] = [0, total_amort, total_int, total_cuot, 0]
    return mat
