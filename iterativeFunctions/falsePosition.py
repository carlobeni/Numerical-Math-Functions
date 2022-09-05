import time
import numpy as np

def falsePosition(e,range_value,f):
    [li,ls]=range_value
    prevX=0
    c=li
    results={
        "name:":"Falsa Posicion",
        "range": "["+str(li)+" ; "+str(ls)+"]",
        "root": 0, 
        "condition": "",
        "n": 0,
        "time": 0}
    start= time.perf_counter()
    maxN=1000
    for i in range(maxN):
        prevf=f(c)
        prevX=c

        c=(-li*f(li)+ls*f(ls))/(-f(li)+f(ls))
        if(f(c)*f(li)<0): ls=c
        else: li=c
        
        if np.abs(f(c))<e:
            results["condition"]="$|f(x_k)| < 10^{-6}$"
            results["root"]=c
            break
        if np.abs(prevX-c)<e:
            results["condition"]="$|x_k-x_{k-1}| < 10^{-6}$"
            results["root"]=c
            break
        results["n"]+=1

    end=time.perf_counter()
    results['time']=end-start
    return results