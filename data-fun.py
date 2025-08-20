# Let's create data about students in a class
import pandas as pd  # This helps us work with data

# Creating a table of student information
students_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [10, 11, 10, 12, 11],
    'Favorite_Subject': ['Math', 'Science', 'Art', 'English', 'Math'],
    'Pet': ['Dog', 'Cat', 'Fish', 'Dog', 'Hamster'],
    'Hours_Sleep': [9, 8, 10, 9, 8]
}

# Turn this into a data table (called a DataFrame)
students_table = pd.DataFrame(students_data)
print("Our student data:")
print(students_table)

# Let's ask questions about our data!
print("\nHow many students love Math?")
math_lovers = students_table[students_table['Favorite_Subject'] == 'Math']
print(math_lovers)

print("\nWhat's the average age?")
average_age = students_table['Age'].mean()
print("Average age is:", average_age)
