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



