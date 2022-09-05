import time
import numpy as np

from tools.isReady import isReady

def secant(e,x0,xp0,f):
    prevAX=xp0
    prevX=xp0
    x=x0
    df = lambda prevX, prevAX: ( f(prevX) - f(prevAX) ) / (prevX - prevAX) 
    results={
        "name":"Secante",
        "x0": x0,
        "x1": xp0,
        "root": 0, 
        "condition": "",
        "n": 0,
        "time": 0}
    start= time.perf_counter()
    maxN=1000
    for i in range(maxN):
        prevAX=prevX
        prevX=x
        x=prevX-f(prevX)/df(prevX,prevAX)

        if(isReady(f(x),x,prevX,results,e)): break
        results["n"]+=1
        
    end=time.perf_counter()
    results['time']=end-start
    return results