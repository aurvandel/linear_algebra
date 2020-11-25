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
    print("You entered:\n {}".format(matrix))
    return matrix


def getEig(matrix):
    w, v = LA.eig(matrix)
    print("Eigen Values: {} '\n' Eigen Vectors:\n {}".format(w.real, v))
    return w.real, v


def predict(matrix, w, v):
    p = int(input("To predict enter number of years or 0 to exit: "))
    if p != 0:
        R = int(input("Enter the number of rows: "))
        print("Enter the entries of x0 in a single line (separated by space): ")
        # User input of entries in a
        # single line separated by space
        entries = list(map(float, input().split()))
        vector = np.array(entries).reshape(R, 1)
        print("You entered:\n {}".format(vector))
        aMatrix = np.concatenate((matrix, vector), 1)
        print("Your augmented matrix is:\n {} ".format(aMatrix))
        vector = np.flipud(vector)
        vRot = np.rot90(v)
        #matrix = np.rot90(matrix)
        # reshape v so that each vector is correct.
        a2Matrix = np.concatenate((vRot, vector),1)
        print(a2Matrix)
        x = LA.solve(vRot, vector)
        #print("Solves to: ".format(x))
        #x1 = v[0]
        #x2 = v[1]
        #print("The linear combination is: {} * ({}^{} * {}) + {}({}^{} + {}) + {}({}^{} + {}) ".format(x[0][0], w[0], p, vRot[2], x[1][0], w[1], p, vRot[1], x[2][0], w[2], p, vRot[0]))
        #prediction = x[0][0]*(pow(w[0], p) * vRot[1]) + x[1][0]*(pow(w[1], p) * vRot[0])
        #print("In {0} years there will be {1}".format(p, prediction))
        #s = 0
        #for i in range(len(prediction)):
        #    s += prediction[i]
        #print("Or {} total".format(s))
        print(x)       
        pred = []
        s = 0
        for i in range(R):
            print("{} * ({}^{} * {}".format(x[i][0], w[i], p, vRot[(R-1)-i]))
            part = x[i][0]*(pow(w[i], p) * vRot[(R-1)-i])
            pred.append(part)
            for j in range(len(part)):
                s += part[j]
        print("In {0} years there will be the sum of {1}, or {2} total".format(p, pred, s))

if __name__ == '__main__':
    matrix = getMatrix()
    w, v = getEig(matrix)
    predict(matrix, w, v)
