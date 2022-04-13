'''After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, 
but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or 
any of the rooms below any of the free rooms.
Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that 
are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).
'''

def solution(matrix):
    TotalSum = 0 #initiate a variable that tracks the number of suitable codebot rooms
    for j in range(len(matrix[0])): #looping through each column in the matrix
        for i in range(len(matrix)): # looping through each row in the matrix
            if (matrix[i][j] == 0): #exit loop if the element in the referenced matrix position equals 0
                break
            else: 
                TotalSum += matrix[i][j] #add the element to the totalsum variable
    return TotalSum
            
  
