

def calculate(operator, *numbers):
    if not numbers:
        return "No numbers provided"

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
        else:
            return "Invalid operator"

    return result

print(calculate('+', 2, 3, 4))     # 2 + 3 + 4 = 9
print(calculate('*', 2, 3, 4))     # 2 * 3 * 4 = 24
print(calculate('-', 10, 3, 2))    # 10 - 3 - 2 = 5
print(calculate('/', 100, 2, 5))   # 100 / 2 / 5 = 10
