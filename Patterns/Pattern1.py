"""
*
**
***
****
*****
"""

# by using function and accept the number from user
def pattern(r1):
    for i in range(r1):
        print("*" * (i+1))
num=eval(input("Enter a Number: "))
pattern(num)

# by using function
def pattern(r1):
    for i in range(r1):
        print ("*" * (i+1))
pattern(5)

# without useing function
for i in range(1,9,1):
    print("*" * (i+1))

# Using nested loops
def pattern(r1):
    for i in range(r1):
        for j in range(i + 1):
            print("*", end="")
        print()
pattern(5)

# using a while loop
def pattern(r1):
    i=0
    while i < r1:
        print("*" *(i + 1))
        i += 1
pattern(5)

# using sttr.jion() and list comprehension
def pattern(r1):
    for i in range(1, r1 + 1):
        print("".join(["*" for _ in range(i)]))
pattern(5)

# Recursive approach
def pattern(r1, current=1):
    if current > r1:
        return
    print("*" * current)
    pattern(r1,current + 1)
pattern(5)