import math
from tkinter import *

from GraphicalInterface.NodeDisplayer import NodeDisplayer
from NeuralNetwork.NeuralNetwork import NeuralNetwork


class MainGrid(Frame):


    def add_a_grid_layer(self, size):
        size_root = math.floor(math.sqrt(size))

        for i in range(0, size):
            print(" {} - {} ".format(i/5, i % 5))
            tmp = NodeDisplayer(self, size)
            tmp.grid(column=i % size_root, row=int(i / size_root))

    def add_grid_layers(self):
        for size in self.neural_network.shape:
            self.add_a_grid_layer(size)

    def __init__(self, root, neural_network: NeuralNetwork, **kw):
        super().__init__(root, **kw)
        self.root = root
        self.neural_network = neural_network
        self.add_grid_layers()

        self.pack()
