#! /usr/bin/python
# -*- coding: utf-8 -*-


from dataHandler import DataHandler
from network import Network
import layer
import activationFunctions

if __name__ == '__main__':
    EPOCHS = 100
    ETA = 0.001
    PATH = "mnist_dataset"
    CKPT_DIR = "ckpt"
    MBS = 100 #mini_batch_size

    dataHandler = DataHandler(PATH)
    dataHandler.load_training()

    sizes = [784, 16,16,10]
    network = Network(sizes, dataHandler, EPOCHS/10.0, CKPT_DIR)
    network.SGD(dataHandler, EPOCHS, MBS, ETA, False)
