import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import statistics
import math

#FMA 
def FMA(window,thresh,alpha,x,y):
    changes_k=[]
    mu_0=sum(y[:window])/window
    k=0
    while k < len(y):
        g=0
        for i in range(window):
            gamma=alpha*i
            g+=(y[k-i]-mu_0)*gamma
        if abs(g)>thresh:
            changes_k.append(k)
        k+=1
    return changes_k

#GMA
def GMA(window,thresh,alpha,x,y):
    changes_k=[]
    mu_0=sum(y[:window])/window
    k=0
    g=0
    while k < len(y):
        g=(1-alpha)*g+alpha*(y[k]-mu_0)
        if abs(g)>thresh:
            changes_k.append(k)
            g=0
        k+=1
    return changes_k

#GMA fitted for calculating the breaking dynamics. 
#A change is detected iff the new changevalue is bigger than the previous. 
#mu_0 doesnt change.
def GMAdensity1(window,thresh,alpha,x,y):
    changes_k=[[0,0]]
    mu_0=sum(y[:window])/window
    k=window
    g=0
    g_prev=0
    while k < len(y):
        g=(1-alpha)*g+alpha*(y[k]-mu_0)
        k+=1
        if abs(g)>g_prev:
            changes_k.append([k,abs(g)])
            g_prev=abs(g)
            g=0
    return changes_k


#GMA fitted for calculating the breaking dynamics.
#This is used when thresh=0 and thus g must be negative in order to be detected. 
#mu_0 changes from each detected change. 
def GMAdensity2(window,thresh,alpha,x,y):
    changes_k=[[0,0]]
    mu_0=sum(y[:window])/window
    k=window
    g=0
    while k < len(y):
        g=(1-alpha)*g+alpha*(y[k]-mu_0)
        k+=1
        if g<thresh:
            changes_k.append([k,abs(g)])
            mu_0=statistics.mean(y[k-window:k])
    return changes_k

#GLR. new_y is plotted as a step graph so its easy to see where it is a detected jump. 
def GLR(window,thresh,y,x,s,t):
    mu_0=statistics.mean(y[:window])
    variance=statistics.variance(y,mu_0)
    k=0
    m=0
    new_y=[]
    changes_k=[0]
    while k<len(y)-window:
        new_y.append(s)
        glist=[]
        for j in range(m,k+1):
            sum_k=0
            for i in range(j,k+1):
                sum_k=sum_k+(y[i]-mu_0)
            gtemp=(1/(k-j+1))*(sum_k**2)
            glist.append(gtemp)
        gk=(1/(2*variance))*max(glist)
        if abs(gk)-mu_0/2>thresh:
            m=k+1
            changes_k.append(k)
            #mu_0=statistics.mean(y[m:m+window])
            if mu_0>t:
                s=5
            else:
                s=0
        k+=1
    for i in range(window):
        new_y.append(s)
    return new_y,changes_k

#The algorithm used for detecting changes in the original soundtrack. 
# "start" and "stop" is used for splitting the data into smaller parts in order to reduce the runtime.
#m_0 does not change.
def GLR_mod(window,thresh,y,x,start,stop):
    mu_0=statistics.mean(y[:window])
    variance=statistics.variance(y,mu_0)
    k=start
    m=start
    changes_k=[0]#while k<len(y)
    while k<stop:#1000
        glist=[]
        for j in range(m,k+1):
            sum_k=0
            for i in range(j,k+1):
                sum_k=sum_k+(y[i]-mu_0)
            gtemp=(1/(k-j+1))*(sum_k**2)
            glist.append(gtemp)
        gk=(1/(2*variance))*max(glist)
        if abs(gk)>thresh:
            m=k+1
            changes_k.append(k)
        k+=1
    #k+=1000
    return changes_k


#GLR fitted for calculating the breaking dynamics. 
#A change is detected iff the new change value is bigger than the previous. 
#mu_0 doesnt change.
def GLR_density1(window,y,x):
    mu_0=statistics.mean(y[:window])
    variance=statistics.variance(y,mu_0)
    k=0
    m=0
    changes_k=[0,0]#while k<len(y)
    g_prev=0
    while k<len(y):#1000
        glist=[]
        for j in range(m,k+1):
            sum_k=0
            for i in range(j,k+1):
                sum_k=sum_k+(y[i]-mu_0)
            gtemp=(1/(k-j+1))*(sum_k**2)
            glist.append(gtemp)
        gk=(1/(2*variance))*max(glist)
        if abs(gk)>g_prev:
            m=k+1
            changes_k.append([k,abs(g)])
            g_prev=abs(gk)
        k+=1
    #k+=1000
    return changes_k


#GMA fitted for calculating the breaking dynamics.
#This is used when thresh=0 and thus g must be negative in order to be detected. 
#mu_0 changes from each detected change(each changing point is the new start). 
def GLR_density3(window,y,x,thresh):
    mu_0=statistics.mean(y[:window])
    variance=statistics.variance(y,mu_0)
    k=0
    m=0
    changes_k=[[0,0]]#while k<len(y)
    while k<len(y):#1000
        glist=[]
        for j in range(m,k+1):
            sum_k=0
            for i in range(j,k+1):
                sum_k=sum_k+(y[i]-mu_0)
            gtemp=(1/(k-j+1))*(sum_k**2)
            glist.append(gtemp)
        gk=(1/(2*variance))*max(glist)
        if gk<thresh:
            m=k+1
            changes_k.append([k,abs(g)])
            mu_0=statistics.mean(y[k-window:k])
        k+=1
    #k+=1000
    return changes_k










