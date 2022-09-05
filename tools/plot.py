from matplotlib import pyplot as plt
import numpy as np

def plotFunction(f,range,partitions,title=""):
    plt.xlabel("x")
    plt.ylabel("f(x)")
    x = np.linspace(range[0], range[1], partitions)
    plt.plot(x, f(x),label=title)
    plt.axhline(0,color="black",label="_nolegend_")
    plt.grid()
    fileName=title+".png"
    images_dir = '.\graphs'
    plt.savefig(f"{images_dir}\{fileName}")
    print(title+" was saved")

    plt.show()