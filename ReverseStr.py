"""
convert string to array 

concatenate string in while looping through 

"""



def reversestring(input) :
    arrString = list(input)
    length = len(arrString)
    arr = " ";
    for num in reversed(range(length)) :
        arr += arrString[num]
    return arr



print(reversestring('alter'))