a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))

if (a>=b and a>=c):
    print ("First Number is Largest ",a)
elif (b>=c):
    print ("Second Number is Largest ",b)
else:
    print ("Third  is Largest ",c)


# Multiple Of 5
x = int(input("Enter  Number :"))
    
if (x % 5 == 0):
    print("Multiple Of 5")
else:
    print("Not a Multiple Of 5")