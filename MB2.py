import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.special as sp
from itertools import permutations 
import time 
import concurrent.futures
import math

from Hydrogen_Atom import radial_function

#Nowy commit

plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
})

def zeta(m, E_field):

    res=0

    for i in np.arange(-3,3):
        for j in np.arange(-3,3):
            res+=sp.jv(i-m,1/E_field)*sp.jv(j-m,1/E_field)

    return res

def gamma(E_field, N):
    res=1
    for i in np.arange(1,N):
        res=res*zeta(i, E_field)

    return res


# perm = permutations([1, 2, 3, 4, 5, 6, 7, 8]) 
 
# # Print the obtained permutations 
# for i in list(perm): 
#     print (i[0]) 

def MB(x, x_prime, E_field, N):  
    """ 
    MB function as an arguments takes positions 
    in which Wannier functions are localized and
    strenght of electric field.
    """
    Gamma=gamma(E_field, N)
    res=0
    perm = permutations([i for i in np.arange(1,N+1)]) 
    math.factorial(N-1)

    for i in np.arange(1,N):
        for n in np.arange(-3,3):
            for m in np.arange(-3,3):
                res+=sp.jv(-i+n,1/E_field)*sp.jv(-i+m,1/E_field)*radial_function(m+4,0,np.abs(x-m),0.75)*radial_function(n+4,0,np.abs(x_prime-n),0.75)/(zeta(i, E_field))

    return res*math.factorial(N-1)

def part(lp):
    """
    This function as an argument takes 
    list of partition of sample and as a result give
    us density function in this sample.
    """
    start=lp[0]
    stop=lp[1]
    list=np.arange(start,stop,0.15)
    listay=[]
    for i in list:
        listay.append([i,MB(1,4,i,10)])
    return listay


args=[[0.01,2.5],[2.5,5],[5,7.5],[7.5,10],[10,12.5],[12.5,15],[15,17.5],[17.5,20]]


def main():
    empty_list=[]
    with concurrent.futures.ProcessPoolExecutor() as executor:
            for number, prime in zip(args, executor.map(part, args)):
                #print(number, prime)
                empty_list.append(prime)
    return empty_list

print(args[0])

if __name__ == '__main__':
    list=np.array(main())
    print(len(list))
    X=[]
    Y=[]
    for i in np.arange(0,len(list)-1):
        for j in list[i]:
            X.append(j[0])
            Y.append(j[1])
    plt.plot(X,Y)
    plt.show()
# list=np.arange(0.01,10,0.25)
# listay=[]
# for i in list:
#     start=time.perf_counter()
#     listay.append(MB(1,4,i))
#     stop=time.perf_counter()
#     print('Czas = ', stop-start)

# for i in listay:
#     print(i)

# plt.plot(list,listay)
# plt.xlabel(r'$E$',fontsize=18)
# plt.ylabel(r'$\varrho$',fontsize=18)

# #plt.savefig("C:/Users/avoga/Documents/HKplusDC/density_function_x=_%.1f"%1+"xprim=_%1f"%6+".pdf")

# # plt.plot(list,radial_function(5,2,list+2,0.25))
# # plt.plot(list,radial_function(5,3,list+2,0.25))
# plt.show()
