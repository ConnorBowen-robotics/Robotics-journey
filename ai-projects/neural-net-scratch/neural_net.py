import math 
import random
from math_function import functions 
class NeuralNetwork:
    # initializing all of the random variables
    def __init__(self):

        #the rate of which it learns
        self.learning_rate = 0.0001

        #how many times it goes through the learning proccess 
        self.iterations = 200000

        #these are the weights that are used for training
        #hidden layer
        self.w1 = [[random.uniform(-0.5, 0.5) for _ in range(16)] for _ in range(3)]
        #output layer
        self.w2 = [random.uniform(-0.5, 0.5) for _ in range(16)]

        #these are the biases that are used for training 
        #hidden layer
        self.b1 = [random.uniform(-0.5, 0.5) for _ in range (16)]
        #output layer
        self.b2 = random.uniform(-0.5, 0.5)

    #this saves the output of the weights to a txt file
    def save(self, filename = "weights.txt"):
        self.fout = open(filename, "w")
        self.fout.write(str(self.w1) + "\n")
        self.fout.write(str(self.w2) + "\n")
        self.fout.write(str(self.b1) + "\n")
        self.fout.write(str(self.b2) + "\n")
        self.fout.close()
                
    #this loads the weights from the weights.txt file or what ever file i feed it 
    def load(self, filename = "weights.txt"):
        try:
            self.fout = open(filename, "r")
            weights = self.fout.readlines()
            self.w1 = eval(weights[0])
            self.w2 = eval(weights[1])
            self.b1 = eval(weights[2])
            self.b2 = eval(weights[3])
            self.fout.close()
        except:
            print("No saved weights found making a new file.")

    #the activation for learning
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
    
    #what is used to actually back propagate the ai for learning 
    def sigmoid_derivative(self, x):
        return x * (1-x)
    
    # this is what passes date through the network 
    #this is the hidden layer
    def forward(self, input):
        hidden = [0] *  16
        for i in range(16):
            hidden[i] = self.sigmoid(input[0] * self.w1[0][i] + input[1] * self.w1[1][i] + self.b1[i] + input[2] * self.w1[2][i])
        output = sum(hidden[i] * self.w2[i] for i in range(16)) + self.b2
        return hidden ,output
    
    # this is the training function
    def train(self, inputs, target):
        hidden, output = self.forward(inputs)

        #this is the error calculator
        error = target - output

        #this is the outputdelta calculator
        outputdelta = error

        #hidden error calc
        hidden_error = [0] * 16
        for i in range(16):
            hidden_error[i] = outputdelta * self.w2[i]

        #hidden delta calc
        hidden_delta = [0] * 16
        for i in range(16):
            hidden_delta[i] = hidden_error[i] * self.sigmoid_derivative(hidden[i])

        #updating w2 and b2
        for i in range(16):
            self.w2[i] += hidden[i] * outputdelta * self.learning_rate

        #b2 updates
        self.b2 += outputdelta * self.learning_rate

        #updating w1 and b1
        for i in range(16):
            self.w1[0][i] += inputs[0] * hidden_delta[i] * self.learning_rate
            self.w1[1][i] += inputs[1] * hidden_delta[i] * self.learning_rate
            self.w1[2][i] += inputs[2] * hidden_delta[i] * self.learning_rate

        #updating b1
        for i in range(16):
            self.b1[i] += hidden_delta[i] * self.learning_rate

        return error
# temporary tests - delete later
training_data = functions().generate()

nn = NeuralNetwork()

nn.load()

for i in range(nn.iterations):
    total_error = 0
    for inputs, target in training_data:
        error = nn.train(inputs, target)
        total_error += abs(error)
    if i % 100 == 0:
        print(f"Iteration {i} Error: {total_error:.4f}")

#math testing
print("\nTesting addition:")
print(f"0.3 + 0.5 = {nn.forward([0.3, 0.5, 0])[1]:.4f} (expected 0.8)")
print(f"0.5 - 0.2 = {nn.forward([0.5, 0.2, 1])[1]:.4f} (expected 0.3)")
print(f"0.5 * 0.5 = {nn.forward([0.5, 0.5, 2])[1]:.4f} (expected 0.25)")
print(f"0.5 / 0.25 = {nn.forward([0.5, 0.25, 3])[1]:.4f} (expected 2)")

nn.save()