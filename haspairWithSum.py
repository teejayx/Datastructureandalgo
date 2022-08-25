

#Brute/Naive solution - 2 loops BigO(n*2)
def HasPairWithSum(arr, sum): 
    length = len(arr)
    for i in range(0, length):
        for j in range(1, length): 
            if(arr[i] + arr[j] == sum):
                print("Pairs [%d, %d] 's sum is %d " % (arr[i], arr[j], sum))
                return True

    print("no Pairs found")
    return False

def HasPairWithSumOptimized(arr, sum): 
    tempset = []
    length = len(arr)
    for i in range(0, length):
        if arr[i] in tempset.values() :
            return  print("Pairs [%d, %d] 's sum is %d " % (arr[i], tempset[i], sum))
                
        tempset[arr[i]] = sum - arr[i]
    return print("no Pairs found")


HasPairWithSum([1,2,4,3], 5)
HasPairWithSumOptimized([1,2,4,3], 5)


#OptimizeSolution single loop BigO(n)




