z=int(input("enter a value"))
if z>1:
    for i in range(2,z):
        if(z%i)==0:
            print("number is not prime")
            break
        else:
            print("number is prime")

num1=int(input("enter the numebr"))
num2=int(input("enter the number"))
sum=num1+num2
print("the sum is",sum)

product=num1*num2
print("product is",product)

if sum>0:
    print("it is positive")

