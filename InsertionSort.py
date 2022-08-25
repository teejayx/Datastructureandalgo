# peusdocode 
# A = {5,2,4,6,1,3}
# for j = 2 to A.Length 
# key = A[j]
# //insert a[j] into the sorted sequence A[A... j-1]
# i = j - 1
# while i > 0 and A[i] > key 
# A[i + 1] = A[i]
#i = i - 1 
#A[i + 1] = key 
#Big O (n2)

def insertionSort(arrr): 
    for j in range(1, len(arrr)):
        key = arrr[j]
        i = j - 1
        while i >= 0 and arrr[i] > key :
            arrr[i + 1] = arrr[i]
            i -=  1
            arrr[i + 1] = key
 
    return arrr
      
     
print(insertionSort([5,2,4,6,1,3]))