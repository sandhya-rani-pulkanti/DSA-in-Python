# Strings
s = "one piece"
print(s[4])
l = len(s)
print(l)

# for loop range
print(list(range(0, 5, 1)))

# The above range can also be writen as range(0,5) or  range(5)
# 0 --> starting point (including 0)
# 5 --> ending point (excluding 5)
# 1 --> increment

# reversing
print(list(range(5, 0, -1)))

# REVERSING A STRING
# Inefficient method
s = "luffy"
print(s[4]+s[3]+s[2]+s[1]+s[0])
print(list(range(4, -1, -1)))
ans = ""
ans = ans + s[4] # y
ans = ans + s[3] # f
ans = ans + s[2] # f
ans = ans + s[1] # u
ans = ans + s[0] # l
print(ans)

# Efficient method using "for loop"
print("REVERSING A STRING")
n = "One Piece"
answer = ""
l = len(n)
print(l)
for i in range(l-1, -1, -1):
    answer = answer + n[i]
    print(answer)
print(answer)    


# OR
n = "One Piece"
answer = ""
for i in range(8, -1, -1):
    answer = answer + n[i]
print(answer)






