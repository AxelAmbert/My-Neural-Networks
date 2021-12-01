from NeuralNetwork.Layer import Layer


class NeuralNetwork:

    def connect_all_nodes(self, link_probability):
        if len(self.layers) <= 1:
            return
        top_layer = self.layers[-1]
        sub_layer = self.layers[-2]
        sub_layer.connect(top_layer, link_probability)

    def init_layers(self, shape, link_probability):
        for nb_of_node in shape:
            layer = Layer(nb_of_node)
            self.layers.append(layer)
            self.connect_all_nodes(link_probability)

    def __init__(self, shape: tuple, link_probability: float = 1):
        self.layers = []
        self.init_layers(shape, link_probability)
        self.shape = shape