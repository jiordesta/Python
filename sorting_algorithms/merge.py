
def merge(li):
    if len(li) > 1:
        mid = len(li)//2
        left = li[:mid]
        right = li[mid:]

        merge(left)
        merge(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li[k] = left[i]
                i += 1
            else:
                li[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            li[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            li[k] = right[j]
            j += 1
            k += 1
    return li
print(merge([4,3,2,1,6,5]))