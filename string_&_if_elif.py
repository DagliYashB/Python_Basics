print(str)

# concatenation
str1 = 5
str2 = 10
print(str1+str2)

str = "hello"
str1 = "world"
final_str = str+str1
print(final_str)

# Nesting
age = 90
if (age >= 18):  # 0-1
    if(age >= 80):   # 1-1
        print("You can't drive")  # 1-1
    else:
        print("You can drive")   # 0-1
else:
    print("cannot drive")