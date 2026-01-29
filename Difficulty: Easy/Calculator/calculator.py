def utility(a, b, opr):
    #code here
    match opr:
        case 1:
            print(str(a + b), end="")
        case 2:
            print(str(a - b), end="")
        case 3:
            print(str(a * b), end="")
        case _:
            print("Invalid Input", end="")
        