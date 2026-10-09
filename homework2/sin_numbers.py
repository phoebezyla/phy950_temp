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
    ''' Plots a histogram of x values on above image, 
    and the distribution function f(x) on below image.
    '''

    fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2)

    ax1.hist(xarr,bins=nbins,alpha=0.6)
    ax1.set_title("Histogram of values")
    ax2.plot(xarr,f(xarr),'r',label="Distribution function")
    ax2.set_title(r"$f(x) = \frac{\pi}{2} sin(\pi x)$")

    plt.show()
    plt.savefig("sin_hist.png")
    plt.close

##########################################

rarr = np.linspace(0,1,1000)
xarr = transformation(rarr)

histogram(xarr)

