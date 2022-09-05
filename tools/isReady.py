import numpy as np

def isReady(fx,x,prevX,data,e):
    if np.abs(fx)<e and np.abs(prevX-x)<e:
        data["condition"]="$|f(x_k)| < 10^{-6} \wedge |x_k-x_{k-1}| < 10^{-6}$"            
        data["root"]=x
        return True
    elif np.abs(fx)<e:
        data["condition"]="$|f(x_k)| < 10^{-6}$"
        data["root"]=x
        return True
    elif np.abs(prevX-x)<e:
        data["condition"]="$|x_k-x_{k-1}| < 10^{-6}$"
        data["root"]=x
        return True
    return False