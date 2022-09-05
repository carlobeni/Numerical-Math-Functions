import numpy as np
import time
from tools.isReady import isReady

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
        prevX=x
        x=prevX-f(prevX)/df(prevX)
        if(isReady(f(x),x,prevX,results,e)): break
        results["n"]+=1
        
    end=time.perf_counter()
    results['time']=end-start
    return results