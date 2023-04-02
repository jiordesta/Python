li = [4,3,2,1,6,5]

n = len(li)

for i in range(n):
    min_indx = i
    for j in range(i + 1,n):
        if li[j] < li[i]:
            min_indx = j
    li[i],li[min_indx] = li[min_indx],li[i]

print(li)