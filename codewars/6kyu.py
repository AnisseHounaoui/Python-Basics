#Given an array of integers, find the one that appears an odd number of times.
#There will always be only one integer that appears an odd number of times.
#[1,1,2] should return 2, because it occurs 1 time (which is odd).
#[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).

def find_it(seq):
    for e in seq:
        if seq.count(e) % 2 != 0:
            return e

def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]


#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements 
#with the same value next to each other and preserving the original order of elements.
#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']

def unique_in_order(sequence):
    unique_list = []
    for item in sequence:
        if not unique_list or item != unique_list[-1]:
            unique_list.append(item)
    return unique_list
