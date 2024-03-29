#!/usr/bin/env python3

import numpy as np
import scipy.linalg as LA

def getMatrix():
    """
    Gets the specified matrix
    :return matrix, size:
    """
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
    """
    Calculates the eigen values/vectors of a matrix
    :param matrix:
    :return: eigen values, eigen vectors
    """
    w, v = LA.eig(matrix)
    v = np.real_if_close(v, tol=1)
    print("Eigen Values: {} '\n' Eigen Vectors:\n {}".format(w.real, v))
    return w.real, v

def getX0(R):
    """
    Allows user to input a vector of sie R
    :param R:
    :return: inputted vector
    """
    print("Enter the entries of x0 in a single line ({} values separated by spaces) : ".format(R))
    # User input of entries in a
    # single line separated by space
    entries = list(map(float, input().split()))
    vector = np.array(entries).reshape(R, 1)
    print("You entered:\n {}".format(vector))
    return vector

def multPred(matrix, R):
    """
    Multiply a matrix with vector to predict a population for a specified time period
    :param matrix:
    :param R: size of matrix
    :return: x: distribution vector
    """
    years = int(input("Number of years to predict: "))
    x = getX0(R)
    for i in range(years):
        x = np.matmul(matrix, x)

    s = 0
    for i in range(len(x)):
        s += x[i]

    print("The population at {} years is the sum of \n {} \n or {}.".format(years, x, s))
    return x

def predict(matrix, w, v, R):
    """
    Uses the linear combo of eigen values/vectors to predict long term behavior of a population
    :param matrix:
    :param w: eigenvalues
    :param v: eigenvectors
    :param R: matrix size
    :return:
    """
    p = int(input("To predict enter number of years or 0 to exit: "))
    if p != 0:
        vector = getX0(R)
        aMatrix = np.concatenate((matrix, vector), 1)
        print("Your augmented matrix is:\n {} ".format(aMatrix))
        vector = np.flipud(vector)
        vRot = np.rot90(v)
        x = LA.solve(v, vector)
        pred = []
        s = 0
        for i in range(R):
            part = x[i][0]*(pow(w[i], p) * vRot[(R-1)-i])
            pred.append(part)
            for j in range(len(part)):
                s += part[j]
        print("In {0} years there will be the sum of\n{1}\nor {2} total".format(p, pred, s))

def solve(matrix, R):
    """
    Solves a matrix by returning the null space of Ax=
    :param matrix:
    :param R: size
    :return:
    """
    print(LA.null_space(matrix))

def raiseP(A):
    """
    Raises a matrix to the specified power
    :param A: matrix
    :return:
    """
    n = int(input("Enter the number to raise A to: "))
    print(np.linalg.matrix_power(A, n))

def raiseMult(A, R):
    """
    Raises the matrix to the specified power, then multiplies with a vector to predict future behavior
    :param A: matrix
    :param R: size
    :return: distribution vector
    """
    n = int(input("Enter the number to raise A to: "))
    x = getX0(R)
    A = np.linalg.matrix_power(A, n)
    result = np.matmul(A,x)
    print(result)
    return result

def divByMax(A):
    """
    Divides a vector by it's largest element. Used for obtaining the dominant eigenvalue using the power method
    :param A: vector
    :return: vector
    """
    newA = []
    maxA = np.amax(A)
    print("Max: {} ".format(maxA))
    for i in A:
        newA.append(i/maxA)
    x = np.vstack(newA)
    print(x)
    return x

def divBySum(A):
    """
    Divides a vector by the sum of the elements. Useful reformatting a steady state distribution vector.
    :param A: vector
    :return: vector
    """
    newA = []
    sumA = np.sum(A)
    print("Sum: {}".format(sumA))
    for i in A:
        newA.append(i/sumA)
    x = np.vstack(newA)
    print(newA)
    print(x)
    return x

def estimateDE(A, x):
    """
    Calculates the Rayleigh quotient for the dominant eigen value using the power method
    :param A: matrix
    :param x: vector
    :return:
    """
    Ax = np.matmul(A,x)
    Ax = np.squeeze(np.array(Ax))
    x = np.squeeze(np.array(x))
    AxDx = np.dot(Ax, x)
    xDx = np.dot(x, x)
    print("Estimated eigenvalue: {}".format(AxDx/xDx))

def menu():
    """
    Menu interface to drive the UI
    :return: choice
    """
    print("Please make a selection from the menu below", "\n", 
    "[e] Get eigen values and vectors", "\n",  
    "[p] Predict using linear comb of eigen vals/vects", "\n", 
    "[m] Predict using matrix multiplication", "\n", 
    "[s] Get the homogeneous solution", "\n",
    "[r] Raise matrix to the power of n\n",
    "[a] Raise matrix then multiply\n",
    "[v] Estimate the dominant eigen value\n",
    "[n] Convert to distribution vector\n",
    "[b] Markov mouse projections"
    "[q] Quit\n")
    validChoices = ['r','e', 'p', 'm', 'q', 's', 'v', 'a', 'n', 'b']
    while True:
        choice = input("Enter your choice: ")
        choice = choice.lower()
        if choice in validChoices:
            return choice
        else:
            print("Choose a valid option.")


if __name__ == '__main__':
    np.set_printoptions(suppress=True, formatter={'float_kind':'{:.3f}'.format})
    matrixChoices = ['r', 'e', 'p', 'm', 's', 'v', 'a', 'b']
    gotM = False
    while True:
        choice = menu()
        if choice in matrixChoices:
            if not gotM:
                matrix, r = getMatrix()
                gotM = True

            if choice == 'e':
                w, v = getEig(matrix)
            elif choice == 'p':
                w, v = getEig(matrix)
                predict(matrix, w, v, r)
            elif choice == 'm':
                multPred(matrix, r)
            elif choice == 's':
                solve(matrix, r)
            elif choice == 'r':
                raiseP(matrix)
            elif choice == 'a':
                x = raiseMult(matrix, r)
            elif choice == 'v':
                x = raiseMult(matrix, r)
                x = divByMax(x)
                estimateDE(matrix, x)
            elif choice == 'b':
                x = multPred(matrix, r)
                divBySum(x)

        elif choice == 'n':
            R = int(input("Enter size of vector: "))
            x = getX0(R)
            divBySum(x)
        else:
            print("Good bye")
            break
