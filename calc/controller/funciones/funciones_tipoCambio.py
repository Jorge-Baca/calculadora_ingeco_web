"""
Created on 3/08/2020
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

def devaluacion(TCini, TCfin):
    if isinstance(TCini, str):
        TCini = symbols('TCini')
    elif isinstance(TCfin, str):
        TCfin = symbols('TCfin')
    x = ((TCfin-TCini)/TCini)*100
    return x

def tipoCambio(TCini, psi):
    if isinstance(TCini, str):
        TCini = symbols('TCini')
    elif isinstance(psi, str):
        psi = symbols('psi')
    x = TCini*((1+(psi/100)))
    return x

def tipoCambioPeriodos(TCini, psi, nPer):
    if isinstance(TCini, str):
        TCini = symbols('TCini')
    elif isinstance(psi, str):
        psi = symbols('psi')
    elif isinstance(nPer, str):
        psi = symbols('nPer')
    x = TCini*pow(1+(psi/100),nPer)
    return x

def intSolesConst(intDolarConst, psi):
    if isinstance(intDolarConst, str):
        intDolarConst = symbols('intDolarConst')
    elif isinstance(psi, str):
        psi = symbols('psi')
    x = (1+(intDolarConst/100))*(1+(psi/100))-1
    return x
