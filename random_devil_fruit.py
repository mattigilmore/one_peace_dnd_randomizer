import random
import os

devil_fruit = {}
devil_fruit_file = open('devil_fruit.html')
#print(devil_fruit_file)

something=devil_fruit_file.read().lstrip('#### Chop-Chop Fruit')
x=something.split('####')

rand_devil_fruit = random.choice(x)
print(rand_devil_fruit)

