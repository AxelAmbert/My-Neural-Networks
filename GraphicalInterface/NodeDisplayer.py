from tkinter import *

from NeuralNetwork.Node import Node


class NodeDisplayer(Frame):

    def __init__(self, master, root_size):
        super().__init__(master)
        self.canvas = Canvas(self, width= int(1920/ root_size), height=50,  bg="yellow")
        self.canvas.pack()
