li = [4,3,2,1,6,5]
n = len(li)

for i in range(1,n):
    key = li[i]
    j = i - 1
    while j >= 0 and key < li[j]:
        li[j + 1] = li[j]
        j -= 1
    li[j + 1] = key

print(li)