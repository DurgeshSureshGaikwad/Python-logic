# # method 1:
# n1=21
# if n1%2==0:
#     print("number is even")
# else:
#     print("Number is odd")

# # Method 2:
# num1=int(input("Enter a Number : "))
# if num1%2==0:
#     print("Number is even")
# else:
#     print("Number is odd")

# #method 3: by using function
# def evenodd(num):
#     if num%2==0:
#         return "number is even"
#     else:
#         return "Number is odd"

# num=int(input("Enter a number"))
# print(f"Enter {evenodd(num)} ")

class evenodd:
    def __init__(self,num):
        self.num=num

    def check(self):
        if self.num%2==0:
            return("Number is Even ")
        else:
            return("Number is odd ")

n1=int(input("Enter Number: "))
n=evenodd(n1)
print(f"{n.check()}")