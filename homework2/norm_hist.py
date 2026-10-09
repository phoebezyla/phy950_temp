import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

def main() -> int():
    print_hello()
    return 0

def print_hello():
    print("Hello World!")

def hist_create(n=10000,mu=16,dev=4,bins=30):
    ''' This builds a histogram from a normal distribution
    with mean = mu, standard deviation = dev. n points are
    binned. The mean value of the histogram is returned. '''


    # Build array of values w normal distribution
    r = norm.rvs(size=n,scale=dev,loc=mu)

    # Histogram fit
    xarr = np.linspace(min(r),max(r),1000)
    yarr = norm.pdf(xarr,loc=mu,scale=dev) 

    # build figure
    fig, ax = plt.subplots()
    
    ax.hist(r, bins=bins, density=True,
            label="Random values histogram")
    ax.plot(xarr,yarr,'r-',alpha=0.6,label="Norm PDF")

    ax.legend()
    plt.show()
    plt.savefig(f"normhist_mu{mu}_std{dev}_{bins}bins.png")
    plt.close()

    return np.mean(r)

def mod(m: float,n=100) -> None:
    ''' Creates aand plots function f(x) = x + Mx**2
    over [0,10]. M = int(1e6*m)%10 '''

    M = int(float(1e6)*m) % 10

    # build function object
    def f(x):
        return x + M*x**2

    # draw function
    xarr = np.linspace(0,10,n)

    plt.figure()
    plt.plot(xarr,f(xarr),label=fr"f(x) = $x+{M}x^2$")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()
    plt.savefig("function_plot.png")
    plt.close()

###

if __name__ == "__main__":
    main()
    mu = hist_create()
     
    mod(mu)

