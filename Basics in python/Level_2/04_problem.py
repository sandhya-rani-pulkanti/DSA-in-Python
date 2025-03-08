li = [1, 3, 2, 4, 7, 9, 4, 1, 1, 5, 3, 1]
count = 0
for i in li:
    if i == 1:
        count =count + 1
        
print(count)


# Another method
a = [1, 2, 3, 4, 1, 2, 7, 8, 1, 3]
n = len(a)
c = 0 
for i in range(n):
    if a[i] == 1:
        c = c+1
print(c)        


lis = [1, 2, 3, 4]
print(lis[1])
# list index out of range error
# print[lis[4]]
