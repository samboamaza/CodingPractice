# Given an array of strings, return another array containing all of its longest strings.

def solution(inputArray):
    result= []
    max_len = max(len(x) for x in inputArray)
    for i in inputArray: 
        if len(i) == max_len: 
            result.append(i)
    return result
    
        

