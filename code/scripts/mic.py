import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np
import csv
import librosa
import plot

def GetMicData(inn_file,save_file,sampling_r):
	data,SR=librosa.load(inn_file,sr=sampling_r)
	xsek=np.arange(0,len(data)/SR,1/SR)
	saveTabl=np.column_stack((xsek,data))
	np.savetxt(save_file,saveTabl,fmt='%1.6f')
	return


