li = [4,3,2,1,6,5]

for x in range(len(li)):
    for y in range(len(li)):
        if li[x] < li[y]:
            tmp = li[x]
            li[x] = li[y]
            li[y] = tmp
print(li)