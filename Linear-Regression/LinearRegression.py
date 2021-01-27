import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class GradientDescent(object):
    def __init__(self, X, y, training_times=1000, LearningRate=0.0001):
        '''
        Initialize
        '''
        self.y = y
        self.training_times = training_times
        self.LearningRate = LearningRate
        self.shape = X.shape
        self.dimension = self.shape[1] + 1
        self.numberOfSamples = self.shape[0]
        self.onesbias = np.ones((self.numberOfSamples, 1))
        self.X = np.concatenate((X, self.onesbias), axis=1)
        self.theta = np.random.randn(self.dimension, 1)
        self.lossList = []

    def calculatingGradient(self):
        '''
        X^T * (X * theta - y)
        '''
        X_theta_minus_y = np.matmul(self.X, self.theta) - self.y
        return np.matmul((self.X).T, X_theta_minus_y)

    def descent(self):
        '''
        update theta
        '''
        for i in range(self.training_times):
            a = self.calculatingGradient()
            self.theta -= self.LearningRate * a
            if i % 50 == 0:
                print(self.loss())
            else:
                self.loss()
            return self.theta

    def loss(self):
        '''
        a向量的平方可以等价于a的转置乘a
        get loss between y and y_pred
        Loss = (X*theta-Y)^T * (X*theta-Y)
        '''
        X_theta_minus_y = np.matmul(self.X, self.theta) - self.y
        loss = np.matmul((X_theta_minus_y).T, X_theta_minus_y)
        self.lossList.append(int(loss))
        return loss


def createData():
    '''
    y=2x+1
    '''
    X = 10 * np.random.randn(200, 1)
    theta = np.array([[2]])
    y = np.matmul(X, theta) + 1
    salt = np.random.randn(200, 1)
    y = y.reshape((-1, 1)) + 3 * salt
    return X, y


def main():
    X, y=createData()
    print(X, y)
    plt.scatter(X, y)
    gradientDescent = GradientDescent(X, y)
    theta_ans = gradientDescent.descent()
    y_pred = np.matmul(gradientDescent.X, theta_ans)
    plt.plot(X, y_pred, color='r')
    plt.show()
    plt.close()
    loss = gradientDescent.lossList
    x = [i for i in range(1000)]
    plt.plot(x, loss)
    plt.show()

if __name__ == '__main__':
    main()
