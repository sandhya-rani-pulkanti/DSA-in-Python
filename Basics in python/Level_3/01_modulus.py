print(6%3)
print(7%3)
print(7%8)
print(8%5)

# Problem

li = [1, 3, 6, 8, 9, 33, 39, 81, 75, 24]
count = 0
print("The numbers divisible by 3 are :")
for i in li:
    if i%3 == 0:
        print(i)
        count = count + 1
print('The count is: ' + str(count))        