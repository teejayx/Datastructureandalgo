""""
Quick sort algo is sorthing algo which is faster than selection sort and is frequently used in reall life for exmaple the stand c libairy  which has a function called qsort
Quicksort uses D and C which is dived and conquer 

pick a pivot 
partition the array into two sub arrays: elements less than the pivot and elements greater than pivot 
call quicksort recursively on the two sub arrays 



"""



from os import PRIO_USER


def qucicksort(array): 
    if len(array) < 2 :
        return array         #base case: arrays wit 0 or 1 eleent 
    else:
        pivot = array[0]  #recursive case 
        less = [i for i in array[1:] if i <= pivot] # sub array of all elements less than pivot 

        greater = [i for i in array[1:] if i > pivot] # sub array of elements greater than pivot 

        return qucicksort(less) + [pivot] + qucicksort(greater)



print(qucicksort([10, 4, 12, 15, 35]))
