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
import math
from sympy import symbols, Eq, solve, solveset

def valorCupon(valor, tasa):
    '''
    Esta función calcula el valor del cupon.
    @param valor : Valor del cupon.
    @param tasa : tasa del cupon.
    @param rspt: Respuesta.
    @type valor: double/char
    @type tasa: double/char
    @type rspt: double/char
    @return: lo q pidas p
    @rtype: double
    '''
    if isinstance(tasa, str):
        tasa = symbols('tasa')
    elif isinstance(valor, str):
        valor = symbols('valor')
    return (tasa/100)*valor

def calendarioBono(valor, tasa, periodos):
    cupon = valorCupon(valor, tasa)
    total_cupon = 0
    total_total = 0
    mat = []
    mat.append(['Cupón', 'Redención', 'Total'])

    for i in range(1, periodos+1):
        mat.append([])
        mat[i].append(cupon)
        total_cupon = total_cupon + cupon
        mat[i].append(0)
        mat[i].append(cupon)
        total_total = total_total + cupon

    mat[periodos][1] = valor
    mat[periodos][2] = mat[periodos][2] + valor
    total_total = total_total + valor

    mat.append([total_cupon, valor, total_total])

    return mat
