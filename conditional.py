# ==========================
# Dictionary Exercise
# ==========================

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check if the dictionary has skills key and print the middle skill
if "skills" in person:
    skills = person["skills"]
    middle = len(skills) // 2
    print("Middle Skill:", skills[middle])

# 2. Check if the person has Python skill
if "skills" in person:
    if "Python" in person["skills"]:
        print("Person has Python skill.")
    else:
        print("Person does not have Python skill.")

# 3. Check the person's title
skills = person["skills"]

if "JavaScript" in skills and "React" in skills and len(skills) == 2:
    print("He is a front end developer")

elif "Node" in skills and "Python" in skills and "MongoDB" in skills:
    print("He is a backend developer")

elif "React" in skills and "Node" in skills and "MongoDB" in skills:
    print("He is a fullstack developer")

else:
    print("Unknown title")

# 4. Check marital status and country
if person["is_married"] and person["country"] == "Finland":
    print(
        person["first_name"],
        person["last_name"],
        "lives in",
        person["country"] + ".",
        "He is married."
    )
