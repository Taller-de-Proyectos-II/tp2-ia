#!/usr/bin/python

import numpy as np
import csv


def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))


def sigmoid_der(x):
    return x * (1.0 - x)


class MultiLayerAlert:

    def __init__(self, input):
        
        self.input = input
        self.l = len(self.input)
        self.li = len(self.input[0])
        self.wi = []
        self.wh = []
        with open('weights_wi_alert.csv', newline='') as File:
            rows = csv.reader(File)
            for row in rows:
                self.wi.append([float(x) for x in row])

        with open('weights_wh_alert.csv', newline='') as File:
            rows = csv.reader(File)
            for row in rows:
                self.wh.append([float(x) for x in row])

        #self.wi = np.random.random((self.li, self.l))
        #self.wh = np.random.random((self.l, 1))
        
    def response(self, input):
        s1 = sigmoid(np.dot(input, self.wi))
        s2 = sigmoid(np.dot(s1, self.wh))
        return s2

    def training(self, input, outputs, iterations=100000, error=0.00001):
        learn = False
        iter = 0
        average = 0

        while not learn:
            l0 = input
            l1 = sigmoid(np.dot(l0, self.wi))
            l2 = sigmoid(np.dot(l1, self.wh))

            l2_err = outputs - l2
            l2_delta = np.multiply(l2_err, sigmoid_der(l2))
            l1_err = np.dot(l2_delta, self.wh.T)
            l1_delta = np.multiply(l1_err, sigmoid_der(l1))

            self.wh += np.dot(l1.T, l2_delta)
            self.wi += np.dot(l0.T, l1_delta)
            iter += 1
            average = np.mean(abs(l2_err))
            print(iter)
            if error >= average or iter >= iterations:

                with open('weights_wh_alert.csv', 'w', newline='') as File:
                    writer = csv.writer(File)
                    writer.writerows(self.wh)

                with open('weights_wi_alert.csv', 'w', newline='') as File:
                    writer = csv.writer(File)
                    writer.writerows(self.wi)

                print("iterations {}".format(iter))
                print("Error average {}".format(average))

                learn = True
