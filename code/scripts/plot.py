import numpy as np
import matplotlib.pyplot as plt

def plotgraph(x,y,color,xlabel,ylabel,title):
	font = {'fontname':'Arial'}
	fig = plt.figure()
	plt.plot(x,y,color)
	fig.suptitle(title,**font)
	plt.xlabel(xlabel,**font)
	plt.ylabel(ylabel,**font)
	plt.show()
	return

