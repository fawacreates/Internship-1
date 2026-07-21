def main():
    x = int(input("what is x? "))
    print("x cubed is", cube(x))
def cube(n):
    return pow(n, 3)
main()