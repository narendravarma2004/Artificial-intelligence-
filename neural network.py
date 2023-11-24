import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases randomly
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.bias_hidden = np.random.rand(1, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_output = np.random.rand(1, self.output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, inputs):
        # Input to hidden layer
        hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        hidden_output = self.sigmoid(hidden_input)

        # Hidden to output layer
        output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
        predicted_output = self.sigmoid(output_input)

        return predicted_output

    def visualize_network(self):
        G = nx.DiGraph()

        # Add nodes
        G.add_nodes_from(range(1, self.input_size + self.hidden_size + self.output_size + 1))

        # Add edges - input to hidden layer
        for i in range(self.input_size):
            for j in range(self.hidden_size):
                G.add_edge(i + 1, self.input_size + j + 1)

        # Add edges - hidden to output layer
        for i in range(self.hidden_size):
            for j in range(self.output_size):
                G.add_edge(self.input_size + i + 1, self.input_size + self.hidden_size + j + 1)

        # Plot the graph
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold')
        plt.title('Neural Network Structure')
        plt.show()

# Example usage:
if __name__ == "__main__":
    # Define neural network parameters
    input_size = 3
    hidden_size = 4
    output_size = 2

    # Create a neural network
    neural_net = NeuralNetwork(input_size, hidden_size, output_size)

    # Visualize the network structure
    neural_net.visualize_network()
