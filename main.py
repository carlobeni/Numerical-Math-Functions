from os import system

from iterativeFunctions.falsePosition import *
from iterativeFunctions.bisection import *
from iterativeFunctions.newton import *
from iterativeFunctions.secant import *

from tools.latexTable import showLatexTable
from tools.plot import plotFunction
from consts import *
import os

os.system('cls')

#Save Plots
#plotFunction(f_a,[1,4],100,"Funcion a")
#plotFunction(f_b,[1,4],100,"Funcion b")
#plotFunction(f_c,[1,4],100,"Funcion c")

nameF=f_a
interval=[1,4]

#latex table
resBis=list(bisection(e,interval,nameF).values())
resFalseP=list(falsePosition(e,interval,nameF).values())
listTable=[resBis,resFalseP]
dtype=["a" for i in range(len(resBis)-1)]
dtype.append("e")
titles=['$Method$','$Range$','$x$','$SC$', '$n$','$Time(s)$']
showLatexTable(titles,listTable,7,dtype)

resNewton=[list(newton(e,2,nameF).values())]
titles=['$Method$','$x_0$','$x$','$SC$', '$n$','$Time(s)$']
dtype=["a" for i in range(len(resNewton[0])-1)]
dtype.append("e")
showLatexTable(titles,resNewton,7,dtype)

resSec=[list(secant(e,2,2.1,nameF).values())]
titles=['$Method$','$x_0$','$x_1$','$x$','$SC$', '$n$','$Time(s)$']
dtype=["a" for i in range(len(resSec[0])-1)]
dtype.append("e")
showLatexTable(titles,resSec,7,dtype)