import numpy as np
import matplotlib.pyplot as plt
import breakingProb

def normalized(unormlist):
	normlist=[]
	numpunormlist=np.array(unormlist)
	print(max(unormlist))
	print(min(unormlist))
	d=max(unormlist)-min(unormlist)
	for i in range(len(unormlist)):
		normlist.append(((unormlist[i]-min(unormlist))*100)/d)
	return normlist

def plotgraph(x,y,color,xlabel,ylabel,title):
	font = {'fontname':'Arial'}
	fig = plt.figure()
	plt.plot(x,y,color)
	fig.suptitle(title,**font)
	plt.xlabel(xlabel,**font)
	plt.ylabel(ylabel,**font)
	plt.show()
	return


"""data_file=np.loadtxt('../data/aux6BreakingProbGLR.txt', delimiter=' ')
d=data_file.transpose()
plt.plot(d[0],d[1].transpose(),'g')
star_file=np.loadtxt('../data/aux6PointsGLR.txt', delimiter=' ')
x=star_file.transpose()[0]
y=star_file.transpose()[1]
for i in range(len(x)):
	if y[i]!=0:
		plt.plot(x[i],y[i],'*')
plt.show()"""
"""
data_file=np.loadtxt('../data/aux6BreakingProbGMA.txt', delimiter=' ')
d=data_file.transpose()
newY=normalized(d[1])
#plotgraph(d[0],np.array(newY),'b','t(s)',"Breaking Probability","Breaking dynamics")
saveTabl = np.column_stack((d[0],np.array(newY)))
np.savetxt("normalizedBreakingProbGMA.txt",saveTabl,fmt='%1.6f')
"""