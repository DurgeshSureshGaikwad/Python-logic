# method 1
a=10
b=7
c=9
maxnumber=max(a,b,c)
print(f"max number is : {maxnumber}")

# method 2:
a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a third number: "))
print(max(a,b,c))

# method : 3
a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a third number: "))
if a>c and a>b:
    print("number first is grater ")
elif b>c and b>a:
    print("number second is grater ")
else:
    print("Number third is grater ")

# method 4
def maxnum(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return("number first is grater")
    elif num2 > num1 and num2 > num3:
        return("Number second is grater")
    else:
        return("Number third is grater")

a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a third number: "))
print(f"{maxnum(a,b,c)}")

# method 5
class max_num:
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    
    def maxnum(self):
        if self.num1 > self.num2 and self.num1 > self.num3:
            return("number first is grater")
        elif self.num2 > self.num1 and self.num2 > self.num3:
            return("Number second is grater")
        else:
            return("Number third is grater")
        
n1=int(input("Enter a first number: "))
n2=int(input("Enter a second number: "))
n3=int(input("Enter a third number: "))
m=max_num(n1,n2,n3)
print(f"first number {n1}, second number {n2}, third number {n3}: {m.maxnum()}")