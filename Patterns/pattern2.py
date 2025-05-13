'''
*****
****
***
**
*
'''

#using while loop
def pattern(r1):
    i=r1
    while i>1:
        print("*" * (i-1))
        i -= 1
pattern(6)

#using for loop
num=7
for i in range(num):
    print("*" * (num-1))
    num-=1

# nested for loop
def pattern(r1):
    for i in range(r1,0,-1):
        for j in range(i):
            print("*",end="")
        print()
pattern(6)

#by using function
def pattern(r1):
    for i in range(r1):
        print("*" * (r1-1))
        r1 -= 1
pattern(5)

#accept the value from user
def pattern(r1):
    for i in range(r1):
        print("*" * (r1-1))
        r1 -= 1
num=eval(input("Enter a number: "))
pattern(num)

# by using range function
def pattern(r1):
    for i in range(r1-1,0,-1):
        print("*" * i)
pattern(7)