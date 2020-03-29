import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import statistics
import math
import plot

def densityconverter(star_file,window,save_file):
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

def densityconverter2(star_file,save_file):
	star_table=np.loadtxt(star_file, delimiter=' ')
	starTranspose=star_table.transpose()
	newStar=np.append(starTranspose,[np.zeros(len(star_table))], axis=0)
	for k in range(len(star_table)):
		if newStar[1][k]!=0:
			newStar[2][k]=1
	newYlist=[]
	starsum=0
	for i in range(0,len(star_table)):
		starsum+=newStar[2][i]
		newYlist.append(1-(starsum/(i+1)))
	saveTabl=np.column_stack((starTranspose[0],np.array(newYlist)))
	plot.plotgraph(saveTabl.transpose()[0],saveTabl.transpose()[1],'b','Time(s)','Density','Density of changes')
	return

if __name__ == "__main__":
	###########Run densityconverter##################
	densityconverter("../data/aux6pointsGMA2.txt",20000,"../data/aux6density1.txt")
	#densityconverter2("../data/aux6pointsGMA.txt","../data/aux6density2.txt")




