print(list(range(3)))
for i in range(3):
    print (i)

# a methode to compare 1st element with last , 2nd with last second and so on 
n = 3
mul = n * 2
for i in range(n):
    print(i, mul-1-i)    

# palindrome problem

s = "abaaba"    
n = 3
mul = n * 2
for i in range(n):
    l = s[i]
    r = s[mul-1-i]  
    print(l, r)    

# solving palindrome problem
    
s = "abaaaba"    
n = len(s)//2
mul = len(s)
valid = True
for i in range(n):
    l = s[i]
    r = s[mul-1-i]  
    if l != r:
        valid = False
    print(l, r)      

if valid: 
    print("Yes")
else:
    print("No")   
    


# WE WILL GET THE ERROR IN THE BELOW CODE CASUE 4/2 GIVES 2.0 WHICH IS A FLOAT BUT RANGE CONSIDERS ONLY INTER=GERS
# n = 4/2
# for i in range(n):
#     print(i)    

# THE ABOVE CODE CAN BE WRITTEN AS BELOW

n = 4//2 # here we will get 2 not 2.0
for i in range(n):
    print(i)

    # OR

n = 4/2
for i in range(int(n)):
    print(i)    

# OPTIMISED CODE FOR PALINDROME PROBLEM USING "break"    
s = "abaaadba"    
n = len(s)//2
mul = len(s)
valid = True
for i in range(n):
    l = s[i]
    r = s[mul-1-i]  
    if l != r:
        valid = False
        break
    print(l, r)      

if valid: 
    print("Yes")
else:
    print("No")