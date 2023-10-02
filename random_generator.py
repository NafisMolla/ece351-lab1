import math
import random


#this will generate randome variables with a exponential distribution
def generate(lamda:int):
    return - (1 / lamda) * math.log(1 - random.uniform(0, 1))




