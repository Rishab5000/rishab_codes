z=int(input("enter a value"))
if z>1:
    for i in range(2,z):
        if(z%i)==0:
            print("number is not prime")
            break
        else:
            print("number is prime")
