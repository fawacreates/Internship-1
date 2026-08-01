# ==========================
# Dictionary Exercises
# ==========================

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age
dog["name"] = "Bruno"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 3

print("Dog Dictionary:")
print(dog)

# 3. Create a student dictionary
student = {
    "first_name": "Farwa",
    "last_name": "Abidi",
    "gender": "Female",
    "age": 21,
    "marital_status": "Single",
    "skills": ["Python", "HTML"],
    "country": "India",
    "city": "Mysore",
    "address": "Karnataka"
}

print("\nStudent Dictionary:")
print(student)

# 4. Get the length of the dictionary
print("\nLength of student dictionary:", len(student))

# 5. Get the value of skills and check its data type
print("\nSkills:", student["skills"])
print("Data type:", type(student["skills"]))

# 6. Modify skills by adding one or two skills
student["skills"].append("CSS")
student["skills"].append("JavaScript")

print("\nUpdated Skills:")
print(student["skills"])

# 7. Get dictionary keys as a list
print("\nKeys:")
print(list(student.keys()))

# 8. Get dictionary values as a list
print("\nValues:")
print(list(student.values()))

# 9. Change dictionary to a list of tuples
print("\nDictionary as List of Tuples:")
print(list(student.items()))

# 10. Delete one item from the dictionary
del student["address"]

print("\nAfter deleting address:")
print(student)

# 11. Delete the dictionary
del student
