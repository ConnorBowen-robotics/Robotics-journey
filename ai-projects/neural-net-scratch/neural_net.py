import math 
import random

class NeuralNetwork:
    # initializing all of the random variables
    def __init__(self):
        #the rate of which it learns
        self.learning_rate = 0.1
        #how many times it goes through the learning proccess 
        self.iterations = 50000
        #these are the weights that i use
        #hidden layer
        self.w1 = [[random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)], [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]]
        #output layer
        self.w2 = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]
        #these are the biases that i use
        #hidden layer
        self.b1 = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]
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
        hidden = [0, 0, 0, 0]
        hidden[0] = self.sigmoid(input[0] * self.w1[0][0] + input[1] * self.w1[1][0] + self.b1[0])
        hidden[1] = self.sigmoid(input[0] * self.w1[0][1] + input[1] * self.w1[1][1] + self.b1[1])
        hidden[2] = self.sigmoid(input[0] * self.w1[0][2] + input[1] * self.w1[1][2] + self.b1[2])
        hidden[3] = self.sigmoid(input[0] * self.w1[0][3] + input[1] * self.w1[1][3] + self.b1[3])
        output = self.sigmoid(hidden[0] * self.w2[0] + hidden[1] * self.w2[1] + hidden[2] * self.w2[2] + hidden[3] * self.w2[3] + self.b2)
        return hidden ,output
    
    # this is the training function
    def train(self, inputs, target):
        hidden, output = self.forward(inputs)
        #this is the error calculator
        error = target - output
        #this is the outputdelta calculator
        outputdelta = error * self.sigmoid_derivative(output)
        #hidden error calc
        hidden_error = [0, 0, 0, 0]
        hidden_error[0] = outputdelta * self.w2[0]
        hidden_error[1] = outputdelta * self.w2[1]
        hidden_error[2] = outputdelta * self.w2[2]
        hidden_error[3] = outputdelta * self.w2[3]
        #hidden delta calc
        hidden_delta = [0, 0, 0, 0]
        hidden_delta[0] = hidden_error[0] * self.sigmoid_derivative(hidden[0])
        hidden_delta[1] = hidden_error[1] * self.sigmoid_derivative(hidden[1])
        hidden_delta[2] = hidden_error[2] * self.sigmoid_derivative(hidden[2])
        hidden_delta[3] = hidden_error[3] * self.sigmoid_derivative(hidden[3])
        #updating w2 and b2
        self.w2[0] += hidden[0] * outputdelta * self.learning_rate
        self.w2[1] += hidden[1] * outputdelta * self.learning_rate
        #second set up weights
        self.w2[2] += hidden[2] * outputdelta * self.learning_rate
        self.w2[3] += hidden[3] * outputdelta * self.learning_rate
        #b2 updates
        self.b2 += outputdelta * self.learning_rate

        #updating w1 and b1
        self.w1[0][0] += inputs[0] * hidden_delta[0] * self.learning_rate
        self.w1[0][1] += inputs[0] * hidden_delta[1] * self.learning_rate
        self.w1[1][0] += inputs[1] * hidden_delta[0] * self.learning_rate
        self.w1[1][1] += inputs[1] * hidden_delta[1] * self.learning_rate
        #second set of weights update 
        self.w1[0][2] += inputs[0] * hidden_delta[2] * self.learning_rate
        self.w1[0][3] += inputs[0] * hidden_delta[3] * self.learning_rate
        self.w1[1][2] += inputs[1] * hidden_delta[2] * self.learning_rate
        self.w1[1][3] += inputs[1] * hidden_delta[3] * self.learning_rate
        #updating b1
        self.b1[0] += hidden_delta[0] * self.learning_rate
        self.b1[1] += hidden_delta[1] * self.learning_rate
        #updating second set of b1 weights
        self.b1[2] += hidden_delta[2] * self.learning_rate
        self.b1[3] += hidden_delta[3] * self.learning_rate

        return error
# temporary tests - delete later
training_data = [
    ([0,0], 0),
    ([0,1], 1),
    ([1,0], 1),
    ([1,1], 0)
]

nn = NeuralNetwork()

nn.load()

for i in range(nn.iterations):
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

nn.save()