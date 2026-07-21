def main():
    x=int(input("what is x? "))
    if is_even(x):
        print("x is Even")
    else:
        print("x is Odd")

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

main()
