import math 
import random

class NeuralNetwork:
    # initializing all of the random variables
    def __init__(self):
        #the rate of which it learns
        self.learning_rate = 0.5
        #how many times it goes through the learning proccess 
        self.iterations = 10000
        #these are the weights that i use
        #hidden layer
        self.w1 = [[random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)], [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]]
        #output layer
        self.w2 = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]
        #these are the biases that i use
        #hidden layer
        self.b1 = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]
        #output layer
        self.b2 = random.uniform(-0.5, 0.5)

    #the activation for learning
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
    
    #what is used to actually back propagate the ai for learning 
    def sigmoid_derivative(self, x):
        return x * (1-x)
    
    # this is what passes date through the network 
    #this is the hidden layer
    def forward(self, input):
        hidden = [0, 0]
        hidden[0] = self.sigmoid(input[0] * self.w1[0][0] + input[1] * self.w1[1][0] + self.b1[0])
        hidden[1] = self.sigmoid(input[0] * self.w1[0][1] + input[1] * self.w1[1][1] + self.b1[1])
        output = self.sigmoid(hidden[0] * self.w2[0] + hidden[1] * self.w2[1] + self.b2)
        return hidden ,output
    
    # this is the training function
    def train(self, inputs, target):
        hidden, output = self.forward(inputs)
        #this is the error calculator
        error = target - output
        #this is the outputdelta calculator
        outputdelta = error * self.sigmoid_derivative(output)
        #hidden error calc
        hidden_error = [0, 0]
        hidden_error[0] = outputdelta * self.w2[0]
        hidden_error[1] = outputdelta * self.w2[1]
        #hidden delta calc
        hidden_delta = [0, 0]
        hidden_delta[0] = hidden_error[0] * self.sigmoid_derivative(hidden[0])
        hidden_delta[1] = hidden_error[1] * self.sigmoid_derivative(hidden[1])
        #updating w2 and b2
        self.w2[0] += hidden[0] * outputdelta * self.learning_rate
        self.w2[1] += hidden[1] * outputdelta * self.learning_rate
        self.b2 += outputdelta * self.learning_rate
        #updating w1 and b1
        self.w1[0][0] += inputs[0] * hidden_delta[0] * self.learning_rate
        self.w1[0][1] += inputs[0] * hidden_delta[1] * self.learning_rate
        self.w1[1][0] += inputs[1] * hidden_delta[0] * self.learning_rate
        self.w1[1][1] += inputs[1] * hidden_delta[1] * self.learning_rate
        self.b1[0] += hidden_delta[0] * self.learning_rate
        self.b1[1] += hidden_delta[1] * self.learning_rate

        return error
# temporary tests - delete later
training_data = [
    ([0,0], 0),
    ([0,1], 1),
    ([1,0], 1),
    ([1,1], 0)
]

nn = NeuralNetwork()

for i in range(10000):
    total_error = 0
    for inputs, target in training_data:
        error = nn.train(inputs, target)
        total_error += abs(error)
    if i % 1000 == 0:
        print(f"Iteration {i} Error: {total_error:.4f}")

print("\nTesting:")
print(f"[0,0] -> {nn.forward([0,0])[1]:.4f}")
print(f"[0,1] -> {nn.forward([0,1])[1]:.4f}")
print(f"[1,0] -> {nn.forward([1,0])[1]:.4f}")
print(f"[1,1] -> {nn.forward([1,1])[1]:.4f}")