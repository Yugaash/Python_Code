def Add(val1, val2):
    return val1 + val2


def Subtract(val1, val2):
    return val1 - val2


def Multiply(val1, val2):
    return val1 * val2


def Divide(val1, val2):
    return val1 / val2


print("Select:")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

proceed = input("Select Choice a, b, c, d: ")

Val1 = float(input("Num1: "))
Val2 = float(input("Num2: "))

if proceed == 'a':
    print(Val1, "+", Val2, "=", Add(Val1, Val2))

elif proceed == 'b':
    print(Val1, "-", Val2, "=", Subtract(Val1, Val2))

elif proceed == 'c':
    print(Val1, "*", Val2, "=", Multiply(Val1, Val2))

elif proceed == 'd':
    print(Val1, "/", Val2, "=", Divide(Val1, Val2))

else:
    print("retry")
