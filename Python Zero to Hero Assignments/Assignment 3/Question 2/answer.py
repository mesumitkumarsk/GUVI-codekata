def divide(dividend, divisor):
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        return "Cannot divide by zero"
    return result

dividend, divisor = map(int, input().split())
print(divide(dividend, divisor))