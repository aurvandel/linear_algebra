import numpy as np
import scipy.linalg as LA

def getMatrix():
    R = int(input("Enter the number of rows\columns of a square matrix: "))

    print("Enter the entries in a single line (separated by space): ")

    # User input of entries in a
    # single line separated by space
    entries = list(map(float, input().split()))

    # For printing the matrix
    matrix = np.array(entries).reshape(R, R)
    print("You entered:\n {}".format(matrix))
    return matrix, R


def getEig(matrix):
    w, v = LA.eig(matrix)
    print("Eigen Values: {} '\n' Eigen Vectors:\n {}".format(w.real, v))
    return w.real, v

def getX0(R):
    print("Enter the entries of x0 in a single line ({} values separated by spaces) : ".format(R))
    # User input of entries in a
    # single line separated by space
    entries = list(map(float, input().split()))
    vector = np.array(entries).reshape(R, 1)
    print("You entered:\n {}".format(vector))
    return vector

def multPred(matrix, R):
    years = int(input("Number of years to predict: "))
    x = getX0(R)
    for i in range(years):
        x = np.matmul(matrix, x)
    print("The population at {} years is {}.".format(years, x))

def predict(matrix, w, v, R):
    p = int(input("To predict enter number of years or 0 to exit: "))
    if p != 0:
        vector = getX0(R)
        aMatrix = np.concatenate((matrix, vector), 1)
        print("Your augmented matrix is:\n {} ".format(aMatrix))
        vector = np.flipud(vector)
        vRot = np.rot90(v)
        #matrix = np.rot90(matrix)
        # reshape v so that each vector is correct.
        #a2Matrix = np.concatenate((vRot, vector),1)
        #print(a2Matrix)
        x = LA.solve(v, vector)
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
        #print(x)       
        pred = []
        s = 0
        for i in range(R):
            #print("{} * ({}^{} * {}".format(x[i][0], w[i], p, vRot[(R-1)-i]))
            part = x[i][0]*(pow(w[i], p) * vRot[(R-1)-i])
            pred.append(part)
            for j in range(len(part)):
                s += part[j]
        print("In {0} years there will be the sum of {1}, or {2} total".format(p, pred, s))

def menu():
    print("Please make a selection from the menu below", "\n", 
    "[e] Get eigen values and vectors", "\n",  
    "[p] Predict using linear comb of eigen vals/vects", "\n", 
    "[m] Predict using matrix multiplication", "\n", 
    "[q] Quit\n")
    validChoices = ['e', 'p', 'm', 'q']
    while True:
        choice = input("Enter your choice: ")
        choice = choice.lower()
        if choice in validChoices:
            return choice
        else:
            print("Choose a valid option.")


if __name__ == '__main__':
    matrix, r = getMatrix()
    while True:
        choice = menu()
        if choice == 'e':
            w, v = getEig(matrix)
        elif choice == 'p':
            w, v = getEig(matrix)
            predict(matrix, w, v, r)
        elif choice == 'm':
            multPred(matrix, r)
        else:
            print("Good bye")
            break
