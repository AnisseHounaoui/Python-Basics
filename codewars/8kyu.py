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


#Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!

def are_you_playing_banjo(name):
    return name + " plays banjo" if name[0] == "r" or name[0] == "R" else name + " does not play banjo"


#Your task is to create a function that does four basic mathematical operations.
#The function should take three arguments - operation(string/char), value1(number), value2(number).
#The function should return result of numbers after applying the chosen operation.

def basic_op(operator, value1, value2): #vulnerable to code injection
    return eval(str(value1) + operator + str(value2))

def basic_op(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2

def basic_op(operator, value1, value2): #using placeholders
    return eval("{}{}{}".format(value1, operator, value2))


#Check to see if a string has the same amount of 'x's and 'o's. 
#The method must return a boolean and be case insensitive. The string can contain any char.

def xo(s):
    x=0
    o=0
    for c in s:
        if c.lower() == "x":
            x += 1
        elif c.lower() == "o":
            o += 1
    if x == o:
        return True
    return False

def xo(s):
    s = s.lower()
    if s.count('x') == s.count('o') or (('x' and 'o') not in s):
        return True
    return False

def xo(s): #best
    s = s.lower()
    return s.count('x') == s.count('o')


#Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
#Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n*m

def paperwork(n, m): #best
    return max(n, 0) * max(m, 0)


#Complete the square sum function so that it squares each number passed into it and then sums the results together.
#For example, for [1, 2, 2] it should return 9

def square_sum(numbers):
    return sum(num**2 for num in numbers)









