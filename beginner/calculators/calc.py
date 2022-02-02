
def calculate(first, second, operator):
    """
    Takes the first and second numbers, and maths it with the given operator.
    :param first: the first number to calculate
    :param second: the second number to calculate
    :param operator: the operator to use ( + - * / )
    :return: string
    """
    if operator == "+":
        return print(f"{first} {operator} {second} = {first + second}")
    elif operator == "-":
        return print(f"{first} {operator} {second} = {first - second}")
    elif operator == "*":
        return print(f"{first} {operator} {second} = {first * second}")
    elif operator == "/":
        return print(f"{first} {operator} {second} = {first / second}")
    else:
        return None


if __name__ == "__main__":
    num1 = int(input("What is your first number?: "))
    operation = input("Pick an operation ( + - * / ): ")
    num2 = int(input("What is your second number?: "))

    calculate(num1, num2, operation)