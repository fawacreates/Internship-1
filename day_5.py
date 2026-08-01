# ==========================
# Exercise Level 1
# ==========================

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Kiwi"]

# 3. Find the length of the list
print(len(fruits))

# 4. Get the first, middle and last item
print("First:", fruits[0])
print("Middle:", fruits[len(fruits)//2])
print("Last:", fruits[-1])

# 5. Declare mixed_data_types list
mixed_data_types = ["Farwa", 21, 5.4, "Single", "India"]
print(mixed_data_types)

# 6. Declare it_companies list
it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

# 7. Print the list
print(it_companies)

# 8. Print number of companies
print(len(it_companies))

# 9. Print first, middle and last company
print("First:", it_companies[0])
print("Middle:", it_companies[len(it_companies)//2])
print("Last:", it_companies[-1])

# 10. Modify one company
it_companies[2] = "Netflix"
print(it_companies)

# 11. Add an IT company
it_companies.append("Intel")
print(it_companies)

# 12. Insert a company in the middle
middle = len(it_companies)//2
it_companies.insert(middle, "Adobe")
print(it_companies)

# 13. Change one company to uppercase (except IBM)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14. Join using "#; "
print("#; ".join(it_companies))

# 15. Check if a company exists
print("Google" in it_companies)

# 16. Sort list
it_companies.sort()
print(it_companies)

# 17. Reverse list
it_companies.reverse()
print(it_companies)

# 18. Slice first 3 companies
print(it_companies[:3])

# 19. Slice last 3 companies
print(it_companies[-3:])

# 20. Slice middle company
middle = len(it_companies)//2
if len(it_companies) % 2 == 0:
    print(it_companies[middle-1:middle+1])
else:
    print(it_companies[middle])

# 21. Remove first company
it_companies.pop(0)
print(it_companies)

# 22. Remove middle company
middle = len(it_companies)//2
it_companies.pop(middle)
print(it_companies)

# 23. Remove last company
it_companies.pop()
print(it_companies)

# 24. Remove all companies
it_companies.clear()
print(it_companies)

# 25. Destroy list
del it_companies

# 26. Join front_end and back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

joined = front_end + back_end
print(joined)

# 27. Copy and insert Python and SQL
full_stack = joined.copy()

index = full_stack.index("Redux") + 1
full_stack.insert(index, "Python")
full_stack.insert(index + 1, "SQL")

print(full_stack)

# ==========================
# Exercise Level 2
# ==========================

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort, min and max
ages.sort()
print("Sorted:", ages)
print("Min:", min(ages))
print("Max:", max(ages))

# 2. Add min and max again
ages.append(min(ages))
ages.append(max(ages))
print(ages)

# 3. Median
ages.sort()

if len(ages) % 2 == 0:
    median = (ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2
else:
    median = ages[len(ages)//2]

print("Median:", median)

# 4. Average
average = sum(ages) / len(ages)
print("Average:", average)

# 5. Range
age_range = max(ages) - min(ages)
print("Range:", age_range)

# 6. Compare distances
print(abs(min(ages) - average))
print(abs(max(ages) - average))

# 7. Countries list
countries = [
    "China",
    "Russia",
    "USA",
    "Finland",
    "Sweden",
    "Norway",
    "Denmark"
]

middle = len(countries)//2

if len(countries) % 2 == 0:
    print(countries[middle-1:middle+1])
else:
    print(countries[middle])

# 8. Divide into two halves
if len(countries) % 2 == 0:
    first_half = countries[:middle]
    second_half = countries[middle:]
else:
    first_half = countries[:middle+1]
    second_half = countries[middle+1:]

print("First Half:", first_half)
print("Second Half:", second_half)

# 9. Unpack countries
first, second, third, *scandic_countries = countries

print(first)
print(second)
print(third)
print(scandic_countries)