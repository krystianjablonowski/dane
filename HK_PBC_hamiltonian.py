import numpy as np

from scipy.linalg import eigh


def HK_nonPBC_hamiltonian_2particle(delta,t,U):

    
    matrix = np.zeros((6,6))
    matrix[0][0]=delta
    matrix[0][1]=-2*t
    matrix[1][0]=-2*t
    matrix[1][1]=-U/2+delta
    matrix[2][1]=-delta
    matrix[1][2]=-delta
    matrix[2][2]=-U/2+delta
    matrix[3][3]=-U+delta
    matrix[4][4]=-U+delta
    matrix[5][5]=-U+delta
    return eigh(matrix)[1][:,1]

def HK_nonPBC_hamiltonian_1particle(delta,t,U):
    matrix = np.zeros((4,4))
    matrix[0][0]=-t-U/2+delta/2
    matrix[0][2]=-delta/2
    matrix[2][0]=-delta/2
    matrix[1][1]=-t-U/2+delta/2
    matrix[3][1]=-delta/2
    matrix[1][3]=-delta/2
    matrix[2][2]=t-U/2+delta/2
    matrix[3][3]=t-U/2+delta/2

    return eigh(matrix)


if __name__ == '__main__':

    print(HK_nonPBC_hamiltonian_2particle(1,2,3))

    print(HK_nonPBC_hamiltonian_1particle(1,2,3))





