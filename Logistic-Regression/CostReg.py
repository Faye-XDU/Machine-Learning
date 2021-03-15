import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def costReg(X, y, theta, learningRate):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)

    first = np.multiply(-y, np.log(sigmoid(X*theta.T)))
    second = np.multiply(-(1 - y), np.log(1 - sigmoid(X*theta.T)))
    reg = (learningRate / (2 * len(X))) *
    np.sum(np.power(theta[:, 1, theta.shape[1]], 2))

    return np.sum(first + second) / len(X) + reg
