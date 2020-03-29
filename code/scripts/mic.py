import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np
import csv
import librosa

data,SR=librosa.load('../Mic-tracks/Aux/aux6.wav',sr=1000)
print(len(data))
print(data)
#rate,data=scipy.io.wavfile.read('../Mic-tracks/Aux/aux6.wav')
plt.plot(data)
plt.show()

xsek=np.arange(0,len(data)/SR,1/SR)
print(len(xsek))
saveTabl=np.column_stack((xsek,data))
np.savetxt("aux6Table.txt",saveTabl)
#saveTabl=np.column_stack((xsek,data))
#np.savetxt("aux6Table.txt",saveTabl)
"""#22000:340000
newdata=data.flatten('F')[:len(data)]
print(saveTabl)
# write it
#table=saveTabl.tolist()
#with open('aux6Table.csv', 'w') as csvfile:
   # writer = csv.writer(csvfile)
    #[writer.writerow(r) for r in table]
np.savetxt("aux6Table.txt",saveTabl)"""
#plt.plot(xsek,newdata)
#plt.show()