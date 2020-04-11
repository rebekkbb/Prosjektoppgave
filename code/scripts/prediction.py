from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def  dynmodel(x,alpha):
	beta=0
	yi=0
	y=[]
	for i in range(len(x)):
		if i in ulist:
			u=1
			beta=beta+alpha
		else:
			u=0
		yi=yi+beta*u
		y.append(yi)
	return y

def kalman(x,y,alpha,U):
	#init params
	n_iter=len(y)
	sz=(n_iter,)
	z = y[:200001]
	beta=0

	Q=0.00001

	#allocated space
	xhat=np.zeros(sz)
	P=np.zeros(sz)
	xhatminus=np.zeros(sz)
	Pminus=np.zeros(sz)
	K=np.zeros(sz)

	R=0.1**2

	#Initial guesses
	xhat[0]=0.0
	P[0]=1.0

	for k in range(1,n_iter):
		beta=beta+alpha
		xhatminus[k]=xhat[k-1]+beta*U
		Pminus[k]=P[k-1]+Q

		#measurement update
		K[k]=Pminus[k]/(Pminus[k]+R)
		xhat[k]=xhatminus[k]+K[k]*(z[k]-xhatminus[k])
		P[k]=(1-K[k])*Pminus[k]
		if k>=200000:
			z=np.append(z,xhat[k])
	return xhat

"""data_file=np.loadtxt('../data/normalizedBreakingProbGMA.txt', delimiter=' ')
x=data_file[:,0]
y=data_file[:,1]

params, pcov = curve_fit(dynmodel,x,y)
xhat=kalman(x,y,params[0],params[1])
plt.plot(x,xhat,'b')
plt.plot(x,y,'g')
plt.show()"""

data_file=np.loadtxt('../data/normalizedBreakingProbGMA.txt', delimiter=' ')
x=data_file[:,0]
y=data_file[:,1]

ulist=[]
for i in range(len(y)-1):
	if y[i+1]!=y[i]:
		ulist.append(i)



params, pcov = curve_fit(dynmodel,x,y)
print(params)
plt.plot(x,dynmodel(x,params),'r')
plt.plot(x,y,'g')
plt.show()