n = int(input("Enter any number: "))

def func():
    for i in range(11):
        print(f"{n} * {i} = {n*i}")
        i = i+1

func()        


# Similar method

def table(n):
    for i in range(1, 11):
        # print(n, "*", i, "=" , n*i)
        # print(str(n)+ "*" +str(i)+ "=" + str(n*i))
        print(f"{n} * {i} = {n*i}")

table(4) # passing parameter