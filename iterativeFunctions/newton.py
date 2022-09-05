import numpy as np
import time

from tools.symbolicDiff import derv
from consts import symbolicF

def newton(e,x0,f):
    prevX=x0
    x=x0

    df=derv(symbolicF[f.__name__])

    results={
        "name":"Newton",
        "x0": x0,
        "root": 0, 
        "condition": "",
        "n": 0,
        "time": 0}
    start= time.perf_counter()
    maxN=1000
    for i in range(maxN):
        prevf=f(x)
        prevX=x

        x=prevX-f(prevX)/df(prevX)
        currentE=np.abs(prevX-x)

        if np.abs(f(x))<e:
            results["condition"]="$|f(x_k)| < 10^{-6}$"
            results["root"]=x
            break
        if np.abs(prevX-x)<e:
            results["condition"]="$|x_k-x_{k-1}| < 10^{-6}$"
            results["root"]=x
            break
        results["n"]+=1
        
    end=time.perf_counter()
    results['time']=end-start
    return results