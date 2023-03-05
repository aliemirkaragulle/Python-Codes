#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 08:17:49 2021

@author: aliemirkaragulle
"""
#Simple Neural Network/ Perceptron Learning Algorithm
import numpy as np

class Perceptron:
    
    def __init__(self, n): 
        self.n = n 
        self.w = [np.random.randn() for i in range(n)] #gaussian distributed n random numbers as weights 
        self.b = 0 #bias
        
    def predict(self, x): #x = input/ data point
        assert self.n == len(x)
        
        c = 0
        for i in range(self.n):
            c += self.w[i] * x[i]
        return np.sign(c + self.b) #add bias and return the sign
    
    def __call__(self, x): #w/ __call__ you can have your class behave as a function
        return self.predict(x)    
    
    def one_iter(self, X, y): #one iteration of the training over the data set/ one epoch
        num_samples = len(y)
        err = 0 #error
        for a in range(num_samples):
            yhat = self.predict(X[a])
            if yhat * y[a] < 0: #wrong prediction/ I have to update each weight
                err += 1 #update the error
                for i in range(self.n):
                    self.w[i] = self.w[i] + y[a] * X[a][i] #learning rule
                self.b = self.b + y[a] #update the bias
        
        return err
  
    def train(self, X, y, num_iters = 100): 
        for t in range(num_iters):
            err = self.one_iter(X,y) #collect the error
            print(f"Iter: {t}, Error: {err}")
            if err == 0:
                break
            
            

def generate_data(n, num_samples, model = None):
    """ Generate x and y data """
    X = [[np.random.randn() for i in range(n)] for i in range(num_samples)]
    if model is None:
        y = [np.random.choice([-1,+1]) for a in range(num_samples)]
    else:
         y = [model(X[a]) for a in range(num_samples)]  
    return  X,y

def accuracy(model, X, y):
    """
    Training Accuracy 
    Checks if model.predict(X[0]) == y[0], for all sample
    """
    num_samples = len(y)
    acc = 0
    for a in range(num_samples):
        #yhat = model.predict(X[a])
        yhat = model(X[a]) #let's say that you want to use model as a function/ can do this w/ __call__
        if yhat * y[a] > 0: #means they have the same sign
            acc += 1 
    return acc / num_samples
    
#################################################

np.random.seed(17) #same random numbers   
n = 200 #dimension of the data point 
num_samples = 350 #more the samples, harder to fit / you can fit at most 2 * n (prediction)

#create the model
teacher = Perceptron(n) #the perceptron that generates the labels/ generalizing geneerate_data()
model = Perceptron(n)

#generate the data
X, y = generate_data(n, num_samples, model = teacher)
Xtest, ytest = generate_data(n, num_samples, model = teacher)

#print(f"Train Accuracy: {accuracy(model, X, y)}")

#train the model
model.train(X,y, num_iters = 200)

print(f"Train Accuracy: {accuracy(model, X, y)}")
print(f"Test Accuracy: {accuracy(model, Xtest, ytest)}")

