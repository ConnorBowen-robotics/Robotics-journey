import math
import random 

class addition:
    def generate(self):
        training_data = []
        for problem in range(0, 1001, 1):
            num1 = random.randint(0, 100) / 100
            num2 = random.randint(0, 100) / 100
            operation = 0
            answer = num1 + num2
            training_data.append(([num1, num2, operation], answer))
        return training_data

class subtraction:
    def generate(self):
        training_data = []
        for problem in range(0, 1001, 1):
            num1 = random.randint(0, 100) / 100
            num2 = random.randint(0, 100) / 100
            operation = 1
            answer = num1 - num2
            training_data.append(([num1, num2, operation], answer))
        return training_data
    
class multiplication:
    def generate(self):
        training_data = []
        for problem in range(0, 1001, 1):
            num1 = random.randint(0, 100) / 100
            num2 = random.randint(0, 100) / 100
            operation = 2
            answer = num1 * num2
            training_data.append(([num1, num2, operation], answer))
        return training_data

class division:
    def generate(self):
        training_data = []
        for problem in range(0, 1001, 1):
            num1 = random.randint(0, 100) / 100
            num2 = random.randint(1, 100) / 100
            operation = 3
            answer = num1 / num2
            training_data.append(([num1, num2, operation], answer))
        return training_data

class functions:
    def generate(self):
        all_data = addition().generate() + subtraction().generate() + multiplication().generate() + division().generate()
        random.shuffle(all_data)
        return all_data 