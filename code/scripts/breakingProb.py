import plot
import numpy as np
import GMA_real

def normalize(unormlist):
	normlist=[]
	numpunormlist=np.array(unormlist)
	d=max(unormlist)-min(unormlist)
	for i in range(len(unormlist)):
		normlist.append((unormlist[i]-min(unormlist)*100)/d)
	return normlist


def breakingProb(density_file,window):
	density_tabel=np.loadtxt(density_file, delimiter=' ')
	density=density_tabel.transpose()
	current_k=window
	k_change=[]
	print(len(density_tabel))
	for k in range(window+1,len(density_tabel)):
		if density[1][k]<density[1][current_k]:
			k_change.append(k)
			current_k=k
	return k_change,density

def breakingProbGraph(k_change,density):
	k_change.append([len(density[0]),0])
	knumpy_change=np.array(k_change)
	kTransposed=knumpy_change.transpose()
	print("LenK:,{}".format(len(k_change)))
	if len(k_change)==0:
		return
	numSteps=len(k_change)
	a=100/numSteps
	y=[]
	curr_levl=0
	print(len(k_change))
	for i in range(len(kTransposed[0])-1):
		for j in range(int(kTransposed[0][i]),int(kTransposed[0][i+1])):
			y.append(curr_levl)
		curr_levl+=kTransposed[1][i]
	normalizedY = normalize(y)
	plot.plotgraph(density[0],normalizedY,'g','Tme(s)','Breaking probability','Breaking dynamics')
	return

window=20000
density_tabel=np.loadtxt('../data/aux6density1.txt', delimiter=' ')
density=density_tabel.transpose()
x=density[0]
y=density[1]
alpha=0.1
thresh=0.5
k_change=GMA_real.GLR_density(window,y,x)
#breakingProb('../data/aux6density1.txt',20000)
breakingProbGraph(k_change,density)






