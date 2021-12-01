from tkinter import *

from GraphicalInterface.MainGrid import MainGrid
from NeuralNetwork.NeuralNetwork import NeuralNetwork

neural_network = NeuralNetwork((25, ))
root = Tk()

def main():

    root.title("Emergent")

    root.resizable(0, 0)
    MainGrid(root, neural_network)

    root.mainloop()


main()

