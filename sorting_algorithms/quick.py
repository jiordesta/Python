def quick(li):
    if len(li) <= 1:
        return li
    
    pivot = li[len(li)//2]
    left = [x for x in li if x < pivot]
    mid = [x for x in li if x == pivot]
    right = [x for x in li if x > pivot]

    return quick(left) + mid + quick(right)

print(quick([4,3,2,1,6,5]))