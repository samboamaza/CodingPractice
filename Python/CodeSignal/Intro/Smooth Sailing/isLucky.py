'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to 
the sum of the second half.

Given a ticket number n, determine if it's lucky or not.
'''

def solution(n):
    n_string = str(n)
    first_sum = 0 
    second_sum = 0
    for i in range(0,len(n_string)):
        if i < len(n_string)/2:
            first_sum += int(n_string[i])
        else: 
            second_sum += int(n_string[i])
    return first_sum == second_sum
