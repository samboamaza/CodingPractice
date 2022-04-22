'''Given two strings, find the number of common characters between them'''
def solution(s1,s2):
    result = 0
    string1 = str(''.join(sorted(s1)))
    string2 = str(''.join(sorted(s2)))
    for i in string1: 
        if i in string2: 
            string2 = string2.replace(i,'',1)
            result = result + 1
    return result

