
'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in 
a non-descending order without moving the trees. People can be very tall!
'''

def solution(a):
    a_sorted = sorted([i for i in a if i != -1])
    j = 0     
    for i in range(len(a)):
        if a[i] == -1: 
            pass
        else: 
            a[i] = a_sorted[j]
            j += 1
    return a
