import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import statistics
import random
from scipy.stats import halfnorm
import plot

"""y=0
yi=[0]
xi=[0]
theta=0
alph=0.1
def graph(y,theta,alph):
    for i in range(99):
        k=random.gauss(0,0.5)
        theta=abs(theta+k*alph+(1-alph)*0.7)
        y=theta*y+theta
        yi.append(y)

    for x in range (1,100):
        xi.append(x)
    return xi,yi"""


def graph2(var_b):
    x=0
    y=0
    yi=[0]
    xi=[0]
    btemp=0
    while y<100:
        k=random.randint(0,10)
        if k%3==0:
            b=btemp+np.random.laplace(0.3,var_b)
            btemp=b
            print(b)
        else:
            b=0
        y=y+b
        x+=1
        yi.append(y)
        xi.append(x)
    return xi,yi


def graph3(var_a,var_b):
    x=0
    y=0
    yi=[0]
    xi=[0]
    beta=1
    while y<100:
        alpha=np.random.laplace(1,var_a)
        beta=beta+np.random.laplace(0.002,var_b)
        print(beta)
        k=random.randint(1,24)
        if k==1:#Brukes 1 t hver dag??
            u=1
        else:
            u=0
        y=alpha*y+beta*u
        x+=1
        yi.append(y)
        xi.append(x)
    return xi,yi

def graph4(var_a,var_b):
    x=0
    y=0
    yi=[0]
    xi=[0]
    beta=1
    theta=0.00005
    v=0.5
    while y<100:
        meanbeta=x*theta
        varbeta=(theta**2*v+var_b**2)
        alpha=random.gauss(1,var_a)
        beta=np.random.laplace(meanbeta,varbeta)
        print(beta)
        k=random.randint(1,24)
        if k==1:#Brukes 1 t hver dag??
            u=1
        else:
            u=0
        y=alpha*y+beta*u
        x+=1
        yi.append(y)
        xi.append(x)
    return xi,yi

def graph5():
    x=0
    y=0
    yi=[0]
    xi=[0]
    beta=1
    while y<100:
        beta=beta+np.random.laplace(0.002,0.001)
        print(beta)
        k=random.randint(1,24)
        if k==1:#Brukes 1 t hver dag??
            u=np.random.laplace(0.03,0.01)
        else:
            u=0
        y=y+beta*u
        x+=1
        yi.append(y)
        xi.append(x)
    return xi,yi




xi,yi=graph5()

plot.plotgraph(xi,yi,'b','time(h)','probability','Breaking dynamics')

