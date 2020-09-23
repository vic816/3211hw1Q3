import pandas as pd
import numpy
import random

path = 'D:\\UST lesson materials\\Year 3\\COMP 3211\\Assignment 1\\gp-training-set.csv'

data = pd.read_csv(path) 

w1 = w2 = w3 = w4 = w5 = w6 = w7 = w8 = w9 = 0 
weight = [w1,w2,w3,w4,w5,w6,w7,w8,w9]
sum_result_array = [0]*100
learning_rate = 1
fitness_score = 0

i = j = k = generation = 0
sum_result = 0
middle_index = 0
temp_weight = weight     

for generation in range(100):
    print(generation)
    middle_index = random.randint(0,9)
    if(generation != 0):
        weight = weight[:middle_index] + temp_weight[middle_index:]
    for i in range(100):
        temp = 0                # Check if summation is +ve or -ve
        for j in range(9):
            sum_result += weight[j] * data.iloc[i,j]        
        sum_result_array[i] = sum_result    
        if(sum_result_array[i] > 0): # positive number
            temp = 1 
            
        if(temp == data.iloc[i,9]):
            fitness_score += 1
        else:
            for k in range(9):
                weight[k] = learning_rate*(temp-data.iloc[i,9])*data.iloc[i,j] + random.random()
    temp_weight = weight      
index = 0
for index in range(9):
    print(weight[index])

correct = incorrect = 0
for i in range(100):
        temp = 0                # Check if summation is +ve or -ve
        for j in range(9):
            sum_result = weight[j] * data.iloc[i,j]
        if(sum_result > 0):
            temp = 1
        if(temp == data.iloc[i,9]):
            correct += 1
        else:
            incorrect += 1
print(correct)
print(incorrect)