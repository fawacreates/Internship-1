# 1. Declare your age as integer variable
age = 21

# 2. Declare your height as a float variable
height = 5.4

# 3. Declare a variable that stores a complex number
complex_num = 3 + 4j

# 4. Area of a triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height
print("The area of the triangle is", area)

# 5. Perimeter of a triangle
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))

perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter)

# 6. Area and perimeter of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)

print("Area of rectangle:", rectangle_area)
print("Perimeter of rectangle:", rectangle_perimeter)

# 7. Area and circumference of a circle
pi = 3.14
radius = float(input("Enter radius: "))

circle_area = pi * radius * radius
circumference = 2 * pi * radius

print("Area of circle:", circle_area)
print("Circumference of circle:", circumference)

# 8. Slope, x-intercept and y-intercept of y = 2x - 2
slope = 2

# x-intercept (set y = 0)
x_intercept = 1

# y-intercept (set x = 0)
y_intercept = -2

print("Slope:", slope)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)

# 9. Slope and Euclidean distance between (2,2) and (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10

point_slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Slope between points:", point_slope)
print("Distance:", distance)

# 10. Compare the slopes
print("Are the slopes equal?", slope == point_slope)

# 11. Find x where y = x² + 6x + 9 = 0
for x in range(-5, 6):
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")

print("y becomes 0 when x = -3")

# 12. Compare lengths of 'python' and 'dragon'
print(len("python") != len("dragon"))

# 13. Check if 'on' is found in both words
print("on" in "python" and "on" in "dragon")

# 14. Check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)

# 15. Check if 'on' is not in both words
print("on" not in "python" and "on" not in "dragon")

# 16. Find the length of 'python' and convert to float then string
length = len("python")
print(length)

length_float = float(length)
print(length_float)

length_string = str(length_float)
print(length_string)

# 17. Check if a number is even
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# 18. Check floor division
print(7 // 3 == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print(type("10") == type(10))

# 20. Check if int('9.8') is equal to 10
# (Using float first because int('9.8') raises an error)
print(int(float("9.8")) == 10)

# 21. Weekly earning
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

weekly_earning = hours * rate
print("Your weekly earning is", weekly_earning)

# 22. Seconds lived
years = int(input("Enter number of years you have lived: "))

seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

# 23. Display the table
print("\nTable:")
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)