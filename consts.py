from pyclbr import Function
import numpy as np
import sympy as sp

#error
e=10e-6

#sympy  format
symbolicF={
    "f_a": lambda x: (np.e)**(-x*x)+sp.sin(x),
    "f_b": lambda x: sp.sin(x*x+x-1),
    "f_c": lambda x: x*sp.log(x)-1
}

#numpy format
def f_a(x): return (np.e)**(-x*x)+np.sin(x)
def f_b(x): return np.sin(x*x+x-1)
def f_c(x): return x*np.log(x)-1