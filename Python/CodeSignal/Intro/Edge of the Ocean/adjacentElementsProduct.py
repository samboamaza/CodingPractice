'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
'''
def solution(inputArray):
    MaxSoFar = inputArray[0]*inputArray[1]
    for i in range(0, len(inputArray)-1):
        a = inputArray[i] * inputArray[i+1]
        if  (a > MaxSoFar):
            MaxSoFar = a
    return MaxSoFar
