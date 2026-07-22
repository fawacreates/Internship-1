# Week 1 Practice: Python Data Structures
# Complete the exercises below

"""
Part 1: Lists and List Comprehensions
"""

# Exercise 1.1: Create a list of numbers 1-10 using list comprehension
numbers = [i for i in range(1, 11)]
print("Numbers 1-10:", numbers)

# Exercise 1.2: Filter even numbers from the list
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)

# Exercise 1.3: Create a list of squares
squares = [n**2 for n in numbers]
print("Squares:", squares)

"""
Part 2: Dictionaries
"""

# Exercise 2.1: Create a dictionary of students and their grades
students = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 95
}

# Exercise 2.2: Find the student with the highest grade
top_student = max(students, key=students.get)
print(f"\nTop student: {top_student} with grade {students[top_student]}")

# Exercise 2.3: Create a new dict with grades in different scale (0-4.0)
def percent_to_gpa(percent):
    if percent >= 90: return 4.0
    elif percent >= 80: return 3.0
    elif percent >= 70: return 2.0
    else: return 1.0

gpa_dict = {name: percent_to_gpa(grade) for name, grade in students.items()}
print("GPA Dictionary:", gpa_dict)

"""
Part 3: Sets
"""

# Exercise 3.1: Create sets and perform operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union = set_a | set_b  # OR set_a.union(set_b)
intersection = set_a & set_b
difference = set_a - set_b

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference (A-B): {difference}")

"""
Part 4: Tuples and Unpacking
"""

# Exercise 4.1: Tuples (immutable sequences)
coordinates = (10.5, 20.3, 30.1)  # x, y, z
print(f"\nCoordinates: {coordinates}")

# Exercise 4.2: Unpacking
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")

# Exercise 4.3: Named tuples for clarity
from collections import namedtuple

Point3D = namedtuple('Point3D', ['x', 'y', 'z'])
point = Point3D(10.5, 20.3, 30.1)
print(f"Point: {point}")
print(f"Access by name: point.x={point.x}, point.y={point.y}")

"""
Challenge: Combine everything
"""

print("\n--- CHALLENGE ---")

# Create a list of flight data (altitude, speed, heading)
flight_data = [
    (1000, 25.5, 90),    # altitude(m), speed(m/s), heading(degrees)
    (1500, 28.2, 95),
    (2000, 30.1, 100),
    (2500, 32.5, 105),
]

print("Flight Data (altitude, speed, heading):")
for i, (alt, speed, heading) in enumerate(flight_data):
    print(f"  Measurement {i+1}: Alt={alt}m, Speed={speed}m/s, Heading={heading}°")

# Calculate average altitude and speed
avg_altitude = sum(alt for alt, _, _ in flight_data) / len(flight_data)
avg_speed = sum(speed for _, speed, _ in flight_data) / len(flight_data)

print(f"\nAverage Altitude: {avg_altitude:.1f}m")
print(f"Average Speed: {avg_speed:.1f}m/s")
