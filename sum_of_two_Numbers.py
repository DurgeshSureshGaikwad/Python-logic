"""sum of two numbers"""
#method 1:
a=7
b=9
print(a+b)

#method 2:
num1=int(input("Enter a First Number: "))
num2=int(input("Enter a Second Number: "))
sum=num1+num2
print(sum)

# sum of two numbers by using function
#method 3: 
def result(num1, num2):
    return num1 + num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The sum is:", result(num1, num2))

# sum of two numbers by using class
#method 4:
class sum:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def result(self):
        return (self.num1+self.num2)
    
n1=int(input("Enter a First number: "))
n2=int(input("Enter a Second Number:"))
s=sum(n1,n2)
print(f"sum of {n1} and {n2} is :{s.result()}")