'''
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. 
Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous 
one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
'''

def solution(statues):
    max_value = max(statues)
    min_value = min(statues)
    array_len = len(statues)
    
    count = max_value - min_value + 1
    
    return count - array_len
