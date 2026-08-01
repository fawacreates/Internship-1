# Day 2: 30 Days of Python Programming

# Variables
first_name = "Stalin"
last_name = "Anthony"
full_name = first_name + " " + last_name
country = "India"
city = "Mysore"
age = 21
year = 2026

# Check data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))

# Length of first name
print("Length of first name:", len(first_name))

# Compare lengths
print("Length of first name:", len(first_name))
print("Length of last name:", len(last_name))

if len(first_name) > len(last_name):
    print("First name is longer.")
elif len(first_name) < len(last_name):
    print("Last name is longer.")
else:
    print("Both names have the same length.")

# Number variables
num_one = 5
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Print results
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

# Circle calculations
pi = 3.14
radius = 30

area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)

# User input for radius
radius = float(input("Enter the radius of the circle: "))
area = pi * radius ** 2
print("Area of the circle:", area)

# User input for personal details
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

# Display Python keywords
help("keywords")