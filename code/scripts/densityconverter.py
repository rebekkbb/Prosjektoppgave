import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import statistics
import math
import plot


def densitygraph(star_file,window,save_file):
	star_table=np.loadtxt(star_file, delimiter=' ')
	starTranspose=star_table.transpose()
	newStar=np.append(starTranspose,[np.zeros(len(star_table))], axis=0)
	for k in range(len(star_table)):
		if newStar[1][k]!=0:
			newStar[2][k]=1
	newYlist=[]
	#print(starTranspose)
	starsum=sum(newStar[2][:window])
	for j in range(window):
		newYlist.append(starsum)
	for i in range(len(star_table)-window):
		starsum=sum(newStar[2][i:i+window])
		newYlist.append(starsum)
	saveTabl=np.column_stack((starTranspose[0],np.array(newYlist)))
	np.savetxt(save_file,saveTabl)
	plot.plotgraph(saveTabl.transpose()[0],saveTabl.transpose()[1],'b','Time(s)','Density','Density of changes')
	return


def meangraph(star_file,window,save_file):
	star_table=np.loadtxt(star_file, delimiter=' ')
	starTranspose=star_table.transpose()
	summean=0
	for j in range(window):
		if starTranspose[1][j]>=0:
			summean+=starTranspose[1][j]
	mean=summean/window
	newY=[mean]*window
	k=window
	while k<len(star_table):
		summean=0
		for i in range(window):
			if starTranspose[1][i]>=0:
				summean+=starTranspose[1][j]
		mean=summean/window
		newY.append(newY)
		k+=1
	saveTabl=np.column_stack((starTranspose[0],np.array(newY)))
	plot.plotgraph(saveTabl.transpose()[0],saveTabl.transpose()[1],'b','Time(s)','mean','mean of changes')
	return





