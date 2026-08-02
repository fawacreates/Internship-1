# 1. Unpack siblings and parents from family_members
family_members = (
    "Ali", "Sara", "Ahmed", "Fatima",   # siblings
    "Father", "Mother"                  # parents
)

*siblings, father, mother = family_members

print("Siblings:", siblings)
print("Father:", father)
print("Mother:", mother)

# 2. Create tuples
fruits = ("Apple", "Banana", "Mango")
vegetables = ("Carrot", "Potato", "Tomato")
animal_products = ("Milk", "Egg", "Cheese")

# Join tuples
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Convert tuple to list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Slice out the middle item(s)
middle = len(food_stuff_lt) // 2

if len(food_stuff_lt) % 2 == 0:
    print(food_stuff_lt[middle-1:middle+1])
else:
    print(food_stuff_lt[middle])

# 5. Slice first three and last three items
print("First three:", food_stuff_lt[:3])
print("Last three:", food_stuff_lt[-3:])

# 6. Delete the tuple
del food_stuff_tp

# 7. Check if an item exists in tuple
nordic_countries = (
    "Denmark",
    "Finland",
    "Iceland",
    "Norway",
    "Sweden",
    "Estonia"
)

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)