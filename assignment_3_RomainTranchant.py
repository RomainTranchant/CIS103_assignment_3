# Romain Tranchant
# CIS103
# 9/19/2024
# Homework Assignment 3: Python
# Collections (Basic Level)
# Due Date: 09/20/2024
# Instructor: MD Ali
# Objective:
# This homework will introduce you to the basics of Python collections: lists, tuples, sets, and
# dictionaries. You will practice working with each collection type, understanding how to store
# and manipulate data, and write Python code to perform basic operations.

# 1. Working with Lists
# Write a Python program that does the following:
# - Create an empty list called `fruits`.
# - Add the following fruits to the list: `"apple"`, `"banana"`, `"orange"`, `"grape"`.
# - Print the list of fruits.
# - Remove `"banana"` from the list and print the updated list.
# - Add `"strawberry"` to the list and print the final list.
# Expected Output:
# ['apple', 'banana', 'orange', 'grape']
# ['apple', 'orange', 'grape']
# ['apple', 'orange', 'grape', 'strawberry']


# Create an empty list named fruits
fruits = []

# Add apple, banana, orange and grape to the list
fruits.append("apple")
fruits.append("banana")
fruits.append("orange")
fruits.append("grape")

# Print the updated list
print(fruits)

# Remove banana from the list and print the updated list
fruits.remove("banana")
print(fruits)

# Add strawberry to the list and print the updated list
fruits.append("strawberry")
print(fruits)

# 2. Using tuples
# Write a Python program that:
# - Creates a tuple called `colors` with the following values: `"red"`, `"green"`, `"blue"`, `"yellow"`.
# - Print the entire tuple.
# - Access and print the first and last elements of the tuple.
# - Try to change the second element of the tuple (you should see an error—explain why this
# happens in your comments).

# Create a tuple with the elements red, green, blue and yellow and print the tuple
colors = ("red", "green", "blue", "yellow")
print(colors)

# Print the first element of the tuple, at index 0
print(colors[0])

# Print the fourth element of the tuple, at index 3
print(colors[3])

# Attempt to change the value of the second element, at index 1
# Using the try and except blocks to handles errors, assign the error type
# as the variable t, and print the result using an f-string
# An error happens because tuple can not be changed, they are immutables
try:
    colors[1] = "purple"
except TypeError as t:
    print(f"Error!, {t}")

# 3. Working with Sets
# Write a Python program that:
# - Creates a set called `student_names` with the following names: `"John"`, `"Emma"`, `"Sophia"`,
# `"James"`.
# - Add `"Oliver"` to the set.
# - Remove `"Sophia"` from the set.
# - Print the set after each operation.
# - Try to add `"John"` again and observe what happens (explain why in your comments).
# Expected Output:
# {'John', 'Emma', 'Sophia', 'James'}
# {'John', 'Emma', 'Sophia', 'James', 'Oliver'}
# {'John', 'Emma', 'James', 'Oliver'

# Create a set name student_names and print the result
student_names = {"John", "Emma", "Sophia", "James"}
print(student_names)

# Add Oliver to the set and print the updated set
student_names.add("Oliver")
print(student_names)

# Remove Sophia from the set and print the updated set
student_names.remove("Sophia")
print(student_names)

# John can not be added because sets prevent duplicates, John can only appear once
student_names.add("John")

# Print the student_names set
print(student_names)

# 4. Using Dictionaries
# Write a Python program that:
# - Creates a dictionary called `student_scores` with the following key-value pairs:
# `"John"`: 85, `"Emma"`: 92, `"Sophia"`: 78, `"James"`: 89.
# - Print the dictionary.
# - Access and print Emma's score.
# - Add a new student `"Oliver"` with a score of 95.
# - Update Sophia’s score to 82.
# - Print the updated dictionary.

# Create a student_scores dictionary with key-values pairs and print the dictionary
student_scores = {"john": 85, "Emma": 92, "Sophia": 78, "James": 89}
print(student_scores)

# Print Emma's score using an f-string
print(f"Emma's score is: {student_scores["Emma"]}")

# Add a new student, Oliver, to the dictionary and assign him a score of 95
student_scores["oliver"] = 95

# Update the Sophia's score to 82
student_scores["Sophia"] = 82

# Print the updated dictionary
print(student_scores)


