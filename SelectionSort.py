""""
selection is a neat alogrithim but is not very fasrt BigO(n^2)
"""

def findsmallest(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallestIndex = i
    return smallestIndex




def SelectionSort(arr): 
    newArr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(SelectionSort([5, 3, 6, 2, 10]))

