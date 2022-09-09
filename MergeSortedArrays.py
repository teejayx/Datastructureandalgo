"""
Merge sorted arrays 

"""





def mergeSortedArrays(arr1, arr2):
    firstItem = arr1[0];
    secondItem = arr2[0];
    mergedArra = []

    while firstItem < secondItem:
        