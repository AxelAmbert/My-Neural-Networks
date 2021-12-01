import random
from typing import List

from NeuralNetwork.Constants import Constants
from NeuralNetwork.Weight import Weight


class Node:

    def connect(self, other_node):
        random_weight = random.uniform(Constants.weight_probability_range[0], Constants.weight_probability_range[1])
        self.weights.append(Weight(other_node, random_weight))

    def __init__(self):
        self.value = 0
        self.weights = []
