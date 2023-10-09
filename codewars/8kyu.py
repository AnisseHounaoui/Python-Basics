#Complete the solution so that it reverses the string passed into it.

def solution(string):
    return string[::-1] 
  
def solution(string):
    l = []
    for c in string:
        l.insert(0,c) #add element c in position 0
    return ''.join([c for c in l]) #join different element of the list by '' to form a string

def solution(string):
    reverse =''
    for x in string:
        reverse = x + reverse
    return reverse


