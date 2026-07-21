name=input("what is your name? ")
match name:
    case"Harry":
        print("Gryffindor")
    case"Hermoine":
        print("Gryffindor")
    case"Ron":
        print("Gryffindor")
    case"Draco":
        print("Slytherin")
    case _:
        print("Who? ")