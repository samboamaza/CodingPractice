'''
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.
'''

#using the stack approach 
def solution(inputString):
    stack = [] #initiate an empty list for stack
    for i in range(len(inputString)): #loop through the length of inputarray
        if inputString[i] == "(": 
            stack.append(i) #keep track of the index whenever ( is encountered in the inputarray
        elif inputString[i] == ")":
            temp = inputString[stack[-1]:i+ 1] #reverse top string starting after  the last ')'                                                 is encountered
            inputString = inputString[:stack[-1]] + temp[::-1] + inputString[i+1:]
            del stack[-1]
        
    res = ''
    for i in range(len(inputString)): 
        if inputString[i]!= "(" and inputString[i] != ")": 
                res += inputString[i]
    return res
    
