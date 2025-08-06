
import math

def calculate(operator, *numbers):
    if not numbers:
        return "No numbers provided"

    if operator == "sqrt":
        if len(numbers) != 1:
            return "Square root needs exactly one number"
        if numbers[0] < 0:
            return "Cannot take square root of negative number"
        return math.sqrt(numbers[0])

    result = numbers[0]

    for num in numbers[1:]:
        if operator == '+':
            result += num
        elif operator == '-':
            result -= num
        elif operator == '*':
            result *= num
        elif operator == '/':
            if num == 0:
                return "Cannot divide by zero"
            result /= num
        elif operator == '^':
            result **= num
        else:
            return "Invalid operator"

    return result

print(calculate('+', 2, 3, 4))     # 2 + 3 + 4 = 9
print(calculate('-', 10, 3, 2))    # 10 - 3 - 2 = 5
print(calculate('^', 2, 3))        # 2 ^ 3 = 8
print(calculate('sqrt', 16))       # sqrt(16) = 4.0
