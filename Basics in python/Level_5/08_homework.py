# Adding 1 to 7 to the give number
def func(n):
    for i in range(1, 8):
        print(f"{n} + {i} = {n+i}")

func(4)
func(7)        




# Even

def even(n):
    for i in range(1, 11):
        if i%2 == 0:
            print(f"{n}+{i} = {n+i}")

even(2)
even(8)





# even or odd

def num(n):
    if n%2 == 0:
        print("Even")
    else:
        print("Odd")    

num(4)




# table with 2 parameters
def table(n1,n2):
    for i in range(1, n2+1):
        print(f"{n1}*{i} = {n1*i}")

table(4, 8)
table(3, 7)        


