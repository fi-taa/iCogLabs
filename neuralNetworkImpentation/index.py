import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

input_layer_neurons = 3  # Number of features in the input data
hidden_layer_neurons = 4  # Number of neurons in the hidden layer
output_neurons = 1  # Number of output neurons

# Weight and bias initialization
np.random.seed(42)
weights_input_hidden = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
bias_hidden = np.random.uniform(size=(1, hidden_layer_neurons))
bias_output = np.random.uniform(size=(1, output_neurons))

def forward_propagation(inputs):
    hidden_layer_input = np.dot(inputs, weights_input_hidden) + bias_hidden
    hidden_layer_activation = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_activation, weights_hidden_output) + bias_output
    output = sigmoid(output_layer_input)
    
    return hidden_layer_activation, output

def backward_propagation(inputs, hidden_layer_activation, output, expected_output):
    global weights_hidden_output, weights_input_hidden, bias_hidden, bias_output

    output_error = expected_output - output
    output_delta = output_error * sigmoid_derivative(output)
    
    hidden_layer_error = output_delta.dot(weights_hidden_output.T)
    hidden_layer_delta = hidden_layer_error * sigmoid_derivative(hidden_layer_activation)
    
    # Update weights and biases
    weights_hidden_output += hidden_layer_activation.T.dot(output_delta)
    weights_input_hidden += inputs.T.dot(hidden_layer_delta)
    bias_hidden += np.sum(hidden_layer_delta, axis=0, keepdims=True)
    bias_output += np.sum(output_delta, axis=0, keepdims=True)

def train(inputs, expected_output, epochs):
    for epoch in range(epochs):
        hidden_layer_activation, output = forward_propagation(inputs)
        backward_propagation(inputs, hidden_layer_activation, output, expected_output)

# Example training data
inputs = np.array([[0, 0, 1], 
                   [0, 1, 1], 
                   [1, 0, 1], 
                   [1, 1, 1]])
expected_output = np.array([[0], 
                            [1], 
                            [1], 
                            [0]])

# Training the neural network
train(inputs, expected_output, epochs=10000)

def predict(inputs):
    _, output = forward_propagation(inputs)
    return output

# Example test data
test_inputs = np.array([[0, 0, 1], 
                        [0, 1, 1], 
                        [1, 0, 1], 
                        [1, 1, 1]])
print(predict(test_inputs))
