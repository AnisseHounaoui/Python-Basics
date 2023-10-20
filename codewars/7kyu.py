#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    mumb = ""
    s = s.upper()
    i = 0
    for e in s:
        if i==0:
            mumb += e + "-" #first character doesnt have duplicate
        else:
            mumb += e + (e.lower())*i + "-" 
        i += 1
    return mumb[:-1] #remove last character "-"

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s)) #enumerate() is like a dictionarry we can get inexes and values

#Your task is to return the number of people who are still on the bus after the last bus stop (after the last array).

def number(bus_stops):
    inb = 0
    outb = 0
    for i in range(len(bus_stops)):
        inb += bus_stops[i][0]
        outb += bus_stops[i][1]
    return inb - outb

def number(bus_stops): #best
    return sum([stop[0] - stop[1] for stop in bus_stops])

#In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# example high_and_low("1 2 3 4 5")  # return "5 1"

def high_and_low(numbers):
    arr = numbers.split(" ")
    arr_int = list(map(int,arr))
    return str(max(arr_int)) + " " + str(min(arr_int))

def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])


#You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.
#The string has a length greater or equal to one and contains only letters from ato z.
#Examples:
#s="aaabbbbhaijjjm"
#printer_error(s) => "0/14"
#s="aaaxbbbbyyhwawiwjjjwwm"
#printer_error(s) => "8/22"

def printer_error(s):
    error = 0
    for e in s:
        if e not in "abcdefghijklm":
            error += 1
    return str(error) + "/" + str(len(s))

def printer_error(s): #good
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

from re import sub
def printer_error(s): #better
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))


#Take 2 strings s1 and s2 including only letters from a to z. 
#Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
#a = "xyaabbbccccdefww"
#b = "xxxxyyyyabklmopq"
#longest(a, b) -> "abcdefklmopqwxy"

def longest(a1, a2):
    a1 = sorted("".join(dict.fromkeys(a1)))
    a2 = sorted("".join(dict.fromkeys(a2)))

    long = ""
    for e in a1:
        if e not in long:
            long += e
    for e in a2:
        if e not in long:
            long += e 
    return ''.join(sorted(long))

def longest(a1, a2): #wow
    return "".join(sorted(set(a1 + a2)))


#Filter strings and keep int

def filter_list(l):
    return [e for e in l if not isinstance(e, str)]
