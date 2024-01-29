import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
})

lista=[1.0,2.0,3.0,4.0,5.0]
fig, ax = plt.subplots(len(lista),sharex=True,figsize=(9, 6))
for i in np.arange(len(lista)):
    name='C:/Users/avoga/Documents/HKplusDC/dane/MBdensity_x=_ 1.0xprim=_%.1fN=_5.0.txt'%lista[i]
    
    X = np.loadtxt(name, delimiter=" ")[1:,0]
    Y = np.loadtxt(name, delimiter=" ")[1:,1]#+0.0001  

    ax[i].plot(X,Y) 
    ax[i].set_yscale("log")
    ax[i].set_xlabel(r'E', size=23)
    #ax[i].set_ylabel(r'$\rho$', size=23)
    ax[i].tick_params(axis='both', which='major', labelsize=14)
plt.subplots_adjust(hspace=0.07,left=0.14,right=0.98,top=0.95,bottom=0.117)
fig.supylabel(r'$\rho$', size=23)

plt.savefig("Correlation_logscale_N=5.pdf")
plt.show() 