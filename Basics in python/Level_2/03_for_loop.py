a = [4, "Xie lian", "Hua cheng/ San lang", 3000]
n = len(a)
for i in range(n):
    print(a[i])


# Single variable : ending -1
print(list(range(5)))

# 2 variables : first variable will be starting variable to ending variable-1
print(list(range(2,5)))

# 3 variables: 3rd variable is used to skip the values
print(list(range(2, 9, 3)))

# another example
for i in [1, 2, 3, 4]:
    print("One piece")
    print(i)
print("One piece is real!")