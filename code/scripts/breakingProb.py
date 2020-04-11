import plot
import numpy as np
import GMA_real

def normalized(unormlist):
	normlist=[]
	numpunormlist=np.array(unormlist)
	d=max(unormlist)-min(unormlist)
	for i in range(len(unormlist)):
		normlist.append((unormlist[i]-min(unormlist)*100)/d)
	return normlist


def breakingProbGraph(k_change,density):
	k_change.append([len(density[0]),0])
	knumpy_change=np.array(k_change)
	kTransposed=knumpy_change.transpose()
	y=[]
	ulist=[]
	curr_levl=0
	for i in range(len(kTransposed[0])-1):
		u=1
		for j in range(int(kTransposed[0][i]),int(kTransposed[0][i+1])):
			ulist.append(u)
			y.append(curr_levl)#currlevel
			u=0
		curr_levl+=kTransposed[1][i]

	#normalizedY = normalized(y)
	#plot.plotgraph(density[0],y,'g','Tme(s)','Breaking probability','Breaking dynamics')
	return y,ulist






