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

