# Inefficient Method
n = 4
name = "Luffy"
for i in range(n):
    print(name)


n1 = 7
Luffy = "King of Pirates"
for i in range(n1):
    print(Luffy)   


n2 = 3
crew = "Strawhats"
for i in range(n2):
    print(crew)



# Efficient Method

def fun(s,n):
    for i in range(n):
        print(s)
fun("Roronoa Zoro", 4)
fun(7,3)        
