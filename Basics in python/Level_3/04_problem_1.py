arr = [3, 2, 1, 5, 7, 8, 1, 4, 1, 2, 1, 4, 6]
count = 0
for i in arr:
    if i%3 == 0 and i %2 == 0:
        print(i)
        count = count + 1
print("The numbers divisible by 3 and 2 are:" + str( count))