import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class GradientDescent(object):
    def __init__(self, X, y, training_times = 10000, learningRate = 0.00001):
        '''
        初始化数据
        '''
        self.training_times = training_times
        self.learningRate = learningRate
        self.y = y
        self.shape = X.shape
        self.dimension = self.shape[1] + 1
        self.numberOfSamples = self.shape[0]
        self.onesbias = np.ones((self.numberOfSamples, 1))
        self.X = np.concatenate((X, self.onesbias), axis=1)
        self.theta = np.random.randn(self.dimension, 1)
        self.lossList = []

    def calculatingGradient(self):
        '''
        计算梯度
        '''
        a = np.matmul(self.X, self.theta) - self.y
        gradient = np.matmul((self.X).T, a)
        return gradient

    def descent(self):
        '''
        梯度下降
        更新theta
        '''
        for i in range(self.training_times):
            X_theta_minus_y = self.calculatingGradient()
            self.theta -= X_theta_minus_y * self.learningRate
            if i % 50 == 0:
                print(self.loss())
            else:
                self.loss()
        return self.theta

    def loss(self):
        a = np.matmul(self.X, self.theta) - self.y
        loss = np.matmul(a.T, a)
        self.lossList.append(int(loss))
        return loss


def createData():
    '''
    y = 2x+1
    '''
    X = 10 * np.random.rand(200, 1)
    theta = np.array([[2]])
    y = np.matmul(X, theta) + 1
    '''
    增加扰动
    '''
    salt = np.random.randn(200, 1)
    y = y.reshape((-1, 1)) + salt * 3
    return X, y

def main():
    X, y = createData()
    gradientDescent = GradientDescent(X, y)
    plt.scatter(X, y)
    theta_min = gradientDescent.descent()
    y_pred = np.matmul(gradientDescent.X, theta_min)
    plt.plot(X, y_pred, color='r')
    plt.show()
    plt.close()
    loss = gradientDescent.lossList
    # for i in range(1000):
    #     plt.plot(i, loss)
    x = [i for i in range(10000)]
    plt.plot(x, loss)
    plt.show()

if __name__ == '__main__':
    main()




