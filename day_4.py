# 1. Concatenate strings
string = "Thirty" + " " + "Days" + " " + "Of" + " " + "Python"
print(string)

# 2. Concatenate strings
string2 = "Coding" + " " + "For" + " " + "All"
print(string2)

# 3. Declare company variable
company = "Coding For All"

# 4. Print company
print(company)

# 5. Print length
print(len(company))

# 6. Uppercase
print(company.upper())

# 7. Lowercase
print(company.lower())

# 8. capitalize(), title(), swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Slice out the first word
print(company[7:])        # For All

# 10. Check if company contains "Coding"
print(company.find("Coding"))
print(company.index("Coding"))

# 11. Replace Coding with Python
print(company.replace("Coding", "Python"))

# 12. Replace Everyone with All
sentence = "Python for Everyone"
print(sentence.replace("Everyone", "All"))

# 13. Split using space
print(company.split())

# 14. Split at comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))

# 15. Character at index 0
print(company[0])

# 16. Last index
print(len(company) - 1)

# 17. Character at index 10
print(company[10])

# 18. Acronym of Python For Everyone
pfe = "Python For Everyone"
print("".join(word[0] for word in pfe.split()))

# 19. Acronym of Coding For All
cfa = "Coding For All"
print("".join(word[0] for word in cfa.split()))

# 20. Position of first C
print(company.index("C"))

# 21. Position of first F
print(company.index("F"))

# 22. Last occurrence of l
text = "Coding For All People"
print(text.rfind("l"))

# 23. First occurrence of "because"
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

# 24. Last occurrence of "because"
print(sentence.rindex("because"))

# 25. Slice out "because because because"
start = sentence.find("because")
end = sentence.rindex("because") + len("because")
print(sentence[start:end])

# 26. First occurrence again
print(sentence.find("because"))

# 27. Slice again
print(sentence[start:end])

# 28. Starts with Coding?
print(company.startswith("Coding"))

# 29. Ends with coding?
print(company.endswith("coding"))

# 30. Remove spaces
text = "   Coding For All      "
print(text.strip())

# 31. isidentifier()
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 32. Join list with " # "
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libraries))

# 33. New line escape sequence
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Tab escape sequence
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35. String formatting
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.0f} meters square.")

# 36. String formatting methods
a = 8
b = 6

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")