import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import statistics
import math

import GMA_real
import plot
import breakingProb
import densityconverter
import mic



if __name__ == "__main__":


	#Get data from a .wav file
    #sampling_rate=1000
    #mic.GetMicData('../../div/Mic-tracks/Aux/aux5.wav',"../data/test/aux5SoundWaves.txt",sampling_rate)"""

    #Step1: Run GLR to detect changes in mean, in order to analyze the soundwave further.
    data_file=np.loadtxt('../data/test/aux5SoundWaves.txt',delimiter=' ')
    x=data_file[:,0]
    y=data_file[:,1]

    """#GLR:
    window=1000
    thresh=3#This is the treshold for deciding a change.
    #start=520000(#GLR)
    #stop=520383(#GLR)

    
    changetable=[]
    changes_k=GLR_mod(window,thresh,y,x,start,stop)

    for i in range(start,stop):        
        if i in changes_k:
            changetable.append([x[i],y[i]])
        else:
            changetable.append([x[i],0])

    saveTabl=np.array(changetable)
    f = open("../data/aux6PointsGLR.txt", "a")
    np.savetxt(f,saveTabl,fmt='%1.6f')"""

    #GMA:
    alpha = 0.3
    thresh = 0.15
    window=1000

    changetable=[]
    changes_k=GMA_real.GMA(window,thresh,alpha,x,y)

    for i in range(len(x)):        
        if i in changes_k:
            changetable.append([x[i],y[i]])
        else:
            changetable.append([x[i],0])
    saveTabl=np.array(changetable)
    np.savetxt('../data/test/GMAaux5.txt',saveTabl,fmt='%1.6f')



    #Step2: plot a densitygraph from the detected changes/ plot a graph of the means in a shited window.
    window=30000# (30 seconds)

    #densityconverter.meangraph("../data/aux6pointsGLR.txt",window,"../data/aux6meanGLR.txt")
    densityconverter.densitygraph('../data/test/GMAaux5.txt',window,"../data/test/aux5density.txt")


    #Step3: Plot the breaking probability based by using the GLR again.
    density_tabel = np.loadtxt('../data/test/aux5density.txt', delimiter=' ')
    density = density_tabel.transpose()
    x = density[0]
    y = density[1]

    window = 500
    alpha = 0.3
    thresh = 0

    k_change = GMA_real.GLR_density3(window,y,x,thresh)
    ybreak,ulist = breakingProb.breakingProbGraph(k_change,density)
    saveTabl = np.column_stack((density[0],np.array(ybreak),ulist))
    np.savetxt("../data/test/aux5BreakingProb.txt",saveTabl,fmt='%1.6f')

    #Normaize the graph


