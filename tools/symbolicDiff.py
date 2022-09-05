import sympy as sp
def derv(symbolicFx):
    var = sp.Symbol('x')
    return sp.lambdify(var, sp.diff(symbolicFx(var)),'numpy')