import numpy as np
import scipy.linalg as LA

def getMatrix():
    R = int(input("Enter the number of rows: "))
    C = int(input("Enter the number of columns: "))

    print("Enter the entries in a single line (separated by space): ")

    # User input of entries in a
    # single line separated by space
    entries = list(map(float, input().split()))

    # For printing the matrix
    matrix = np.array(entries).reshape(R, C)
    print(matrix)
    return matrix


def getEig(matrix):
    w, v = LA.eig(matrix)
    print(w.real, '\n', v)
    return w.real, v


def predict(matrix, w, v):
    p = int(input("To predict enter number of years or 0 to exit: "))
    if p != 0:
        R = int(input("Enter the number of rows: "))
        print("Enter the entries in a single line (separated by space): ")
        # User input of entries in a
        # single line separated by space
        entries = list(map(float, input().split()))
        vector = np.array(entries).reshape(R, 1)
        print(vector)
        aMatrix = np.concatenate((matrix, vector), 1)
        print(aMatrix)
        v = np.rot90(v)
        #matrix = np.rot90(matrix)
        # reshape v so that each vector is correct.
        x = np.linalg.solve(matrix, vector)
        print(x)
        x1 = v[0]
        x2 = v[1]
        print(x1,x2)
        print("{} * ({}^{} * {})".format(x[0][0], w[0], p, v[1]))
        prediction = x[0][0]*(pow(w[0], p) * v[1]) + x[1][0]*(pow(w[1], p) * v[0])
        print("In {0} years there will be {1}".format(p, prediction))


if __name__ == '__main__':
    matrix = getMatrix()
    w, v = getEig(matrix)
    predict(matrix, w, v)
