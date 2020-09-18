from .funciones.funciones_bonos import *
from .funciones.funciones_calendario import *
from .funciones.funciones_factores import *
from .funciones.funciones_tipoCambio import *
import sympy as sy

class Controller():
    sol = ''
    def solucionador(self, req):
        sol = self.transformador(req)
        x = sy.symbols('x')
        try:
            exec('global x; global sol; ' + sol, globals())
            sol = globals()['sol']
        except:
            sol = 'Syntax Error'

        if(isinstance(sol,float) | isinstance(sol,str)):
            return sol
        
        if(isinstance(sol[0],list)):
            return self.redondear(sol)
        return sol[0]

    def transformador(self,req):
        if(isinstance(req,str)):
            i = req.find('=')
            if(i != -1):
                cad = req.split('=')
                sol = 'sol=sy.solve(sy.Eq(' + cad[1] + ',' + cad[0] + '))'
            else:
                sol = 'sol=' + req
        i = sol.find('x')
        if(i != -1):
            sol = sol.replace('x','"x"')
        return sol

    def redondear(self,mat):
        for i in range(1, len(mat)):
            for j in range(0, len(mat[i])):
                mat[i][j] = round(mat[i][j],2)
        return mat
