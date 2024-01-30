import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)
plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
})

# plt.rcParams['text.usetex'] = True
cmap=cm.get_cmap('viridis')


shift=1e-4
dist=np.arange(1,8)
max=0
for xp in dist:
    file_name="/home/krystian/Dokumenty/WannierStark/Wannier-Stark-ladder/dane/MBdensity_x=_4.0xprim=_%.1fN=_8.0.txt"%xp
    data=np.loadtxt(file_name)
    plt.plot(data[:,0],np.abs(data[:,1])+shift, label=r'$x^\prime-x$'+"=%i"%(int(xp-1)),color=cmap(xp/5))
    temp_max=np.amax(data[:,1])+shift
    if(temp_max>max):
        max= temp_max
    plt.xlim([np.amin(data[:,0]),np.amax(data[:,0])])
plt.yscale("log")
#plt.xscale('log')
#plt.ylim([shift,max+0.01])
plt.xlabel(r'$E_{field}$',fontsize=15)
plt.ylabel(r'$|\rho(x,x^\prime)|$',fontsize=15)
plt.title(r'$x=4$')
plt.legend(fontsize=15)
plt.tight_layout()
plt.savefig("/home/krystian/Dokumenty/WannierStark/Wannier-Stark-ladder/dane/density_plot_N=8_with_x=4.pdf")
plt.show()