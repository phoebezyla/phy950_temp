import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

def f(x):
    ''' Constant A = pi/2 '''
    return (np.pi/2) * np.sin(np.pi*x)


def transformation(rarr):
    ''' Transforms an array of uniformly distributed
    random numbers (rarr) to an array (xarr) that 
    follows the distribution described by f(x,A). 
    Only valid if rarr is between 0 and 1.

    The transformation method is described in 
    Cowan 3.2. The integral of f(x') from 0 to x(r)
    is set equal to r, and solved.  
    '''

    xarr = (1/np.pi) * np.arccos(1-2*rarr)
    
    return xarr


def histogram(xarr,nbins=20):
    plt.figure()

    plt.hist(xarr,bins=nbins,alpha=0.6)
    plt.plot(xarr,f(xarr),'r',label="Distribution function")

    plt.xlabel("x")
    plt.ylabel("Counts")
    plt.legend()
    plt.show()
    plt.savefig("sin_hist.png")
    plt.close

##########################################

rarr = np.linspace(0,1,1000)
xarr = transformation(rarr)

histogram(xarr)

