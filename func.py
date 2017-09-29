import numpy as np 

def square(n):
    return n**2;

print(square(0));

def squareUpToN(n):
    result = [];
    for i in range(0, n):
        result.append(i**2);
    return result;

print(squareUpToN(3));