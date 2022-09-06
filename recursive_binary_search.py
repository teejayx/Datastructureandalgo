def recursive_binanry_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binanry_search(list[midpoint+1:], target)
            else:
                return recursive_binanry_search(list[midpoint], target)