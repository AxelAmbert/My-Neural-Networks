from typing import List

from random import random

from NeuralNetwork.Node import Node


class Layer:

    def init_nodes(self) -> None:
        for i in range(0, self.size):
            self.nodes.append(Node())

    def connect(self, layer, link_probability) -> None:
        for self_node in self.nodes:
            for other_node in layer.nodes:
                if random() < link_probability:
                    self_node.connect(other_node)

    def __init__(self, size):
        self.nodes = []
        self.size = size
        self.init_nodes()
