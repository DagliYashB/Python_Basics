# List
# List is a Muteble , Changeble
marks = [12.3, 23.4, 43.55, 24.2, 45.9]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])

student = ["yash", 20, "Amdvd"]
print(student[0])
student[0] = "Dagli"
print(student)
    
    
# List Slicing
marks = [1, 2, 3, 4, 5]
print(marks[1:4])
print(marks[:3])
print(marks[1:])
print(marks[-3:-1])

# List Methods
# Append
list = [3, 1, 2]
print(list)
list.append(4)
print(list)

# Sort  [ Assending Order ]
list = [3, 1, 2]
print(list.append(4))
print(list.sort())
print(list)

# Sort  [ Disending Order ]
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list.sort(reverse=True))
print(list)


list = ["banana", "litchi", "apple"]
print(list.sort())
print(list)

list = ['a', 'z', 'o', 'b', 'y']
print(list.sort())
print(list)

# List Revers
list = ['a', 'z', 'o', 'b', 'y']
list.reverse()
print(list)

# List Insert
list = [0, 1, 2, 3, 4, 5]
# print(list)
list.insert(1, 999)
print(list)


list = [0, 1, 2, 3, 4, 5]
print(list)
list.insert(1, "Start")
print(list)


# List Remove
list = [1, 2, 3]
list.remove(2)
print(list)

# List Pop
list = [1, 2, 3, 4, 5]
list.pop(2)
print(list)
