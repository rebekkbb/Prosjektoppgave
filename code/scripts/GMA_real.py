import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import statistics
import math


def FMA(window,thresh,alpha,x,y,s,t):
    new_y=[]
    mu_0=sum(y[:window])/window
    k=window
    while k < len(y):
        new_y.append(s)
        g=0
        for i in range(window):
            gamma=alpha*i
            g+=(y[k-i]-mu_0)*gamma
        print(g)
        if abs(g)>thresh:
            print('gg',g)
            l=int((k-window)/2)
            plt.plot(x[k-window],y[k-window],'o')
            mu_0=sum(y[k-window:k])/window
            if mu_0>t:
                s=5
            else:
                s=0
        k+=1
    for j in range(window):
        if s==0:
            new_y.append(5)
        else:
            new_y.append(0)
    return new_y

def GMA(window,thresh,alpha,x,y):
    changes_k=[]
    mu_0=sum(y[:window])/window
    k=0
    g=0
    #new_y=[]
    while k < len(y):
        #new_y.append(s)
        g=(1-alpha)*g+alpha*(y[k]-mu_0)
        k+=1
        if abs(g)>thresh:
            #mu_0=sum(y[k-int(window/2):k+int(window/2)])/window
            changes_k.append(k)
            g=0
            #if mu_0>t:
                #s=5
            #else:
                #s=0

    return changes_k

def GMA_mod(window,thresh,alpha,x,y):
    changes_k=[[0,0]]
    mu_0=sum(y[:window])/window
    k=window
    g=0
    g_prev=0
    #new_y=[]
    while k < len(y):
        #new_y.append(s)
        g=(1-alpha)*g+alpha*(y[k]-mu_0)
        k+=1
        if abs(g)>g_prev:
            #mu_0=sum(y[k-int(window/2):k+int(window/2)])/window
            changes_k.append([k,abs(g)])
            g_prev=abs(g)
            g=0
            #if mu_0>t:
                #s=5
            #else:
                #s=0
    return changes_k

#With v/min.change=0 ???, 
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

def GLR_mod(window,thresh,y,x,s):
    mu_0=statistics.mean(y[:window])
    variance=statistics.variance(y,mu_0)
    k=0
    m=0
    changes_k=[0]#while k<len(y)
    while k<len(y):#1000
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

def GLR_density(window,y,x):
    mu_0=statistics.mean(y[:window])
    variance=statistics.variance(y,mu_0)
    k=0
    m=0
    changes_k=[0]#while k<len(y)
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


def level(window,thresh,y,x,s,t):
    new_y,changes_k=GLR(window,thresh,y,x,s,t)
    amplist=[]
    maxkeylist=[]
    lengthlist=[]
    print(new_y)
    for i in range(0,len(changes_k)-1):
        amp=y[changes_k[i]]
        maxkey=changes_k[i]
        length=0
        if new_y[changes_k[i]+1]==5:
            length=x[changes_k[i+1]]-x[changes_k[i]]
            for j in range(changes_k[i],changes_k[i+1]):
                if y[j]>amp:
                    amp=y[j]
                    maxkey=j
            amplist.append(amp)
            maxkeylist.append(maxkey)
            lengthlist.append(length)

    return amplist,maxkeylist,lengthlist

def TheDerivatedSet(datafile,i):
    x=datafile[:,0]
    y=datafile[:,i]
    dy=[0]
    for i in range(len(y)-1):
        y_temp=(y[i+1]-y[i])/0.1
        dy.append(y_temp)
    return x,dy


if __name__ == "__main__":


    data_file=np.loadtxt('../data/aux6Table.txt', delimiter=' ')
    #data_file2=np.loadtxt('data-for-change-detection-S.txt', delimiter='\t',skiprows=1)
    x=data_file[:,0]
    y=data_file[:,1]
    #x2=data_file2[3000:4000,0]
    #y2=data_file2[3000:4000,9]

#####RUN GMA##########################################
    window=1000
    thresh=0.2
    alpha=0.3
    #s=5
    changetable=[]
    changes_k=GMA(window,thresh,alpha,x,y)

    for i in range(len(x)):        
        if i in changes_k:
            changetable.append([x[i],y[i]])
        else:
            changetable.append([x[i],0])
        
    saveTabl=np.array(changetable)
    np.savetxt("../data/aux6PointsGMA.txt",saveTabl)


    plt.plot(x,y)
    for k in changes_k:
        plt.plot(x[k],y[k],'*')
    plt.show()


#####RUN FMA##########################################
    """ window=20
    thresh=210
    alpha=0.2
    s=0
    new_y=FMA(window,thresh,alpha,x,y,s)

    plt.plot(x,y,'g')
    plt.plot(x,new_y,'r')
    plt.show()

    meanVal=statistics.mean(y)
    variance=statistics.variance(y,meanVal)
    print("variance",variance)"""

###BEST####
#####RUN GLR############################################
    """window=500
    thresh=2#This is the treshold for deciding a change.
    s=0 #starts with a relax
    t=12 #This is the threshold for deciding if a change is a jump or a relax.

    changetable=[]
    changes_k=GLR_mod(window,thresh,y,x,s)

    for i in range(len(x)):        
        if i in changes_k:
            changetable.append([x[i],y[i]])
        else:
            changetable.append([x[i],0])
        
    saveTabl=np.array(changetable)
    np.savetxt("aux6Points.txt",saveTabl)"""


    #plt.plot(x,y,'b')
    #for k in changes_k:
        #plt.plot(x[k],y[k],'*')
    #plt.show()

#####RUN LEVEL############################################
    #Parameters from GLR

    """amplist,maxkeylist,lengthlist=level(window,thresh,y2,x2,s,t)
    plt.plot(x2,y2,'g')
    print(amplist)
    for i in range(0,len(amplist)):
        plt.plot(x2[maxkeylist[i]],amplist[i],'o')
        plt.bar(x2[maxkeylist[i]],lengthlist[i],0.5)
    plt.show()"""


    """x,dy=TheDerivatedSet(data_file,9)
    plt.plot(x[800:1200],dy[800:1200],'c')
    plt.plot(x1,y1,'b')
    plt.show()"""







