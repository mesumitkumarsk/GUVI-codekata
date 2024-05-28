def sum_of_list(int_list):
    try:
        return sum(int_list)
    except TypeError:
        return "TypeError: List contains non-integer values"

# Reading input from the user
input_list = input().split()

# Convert the input list to integers
try:
    int_list = [int(x) for x in input_list]
    print(sum_of_list(int_list))
except ValueError:
    print("TypeError: List contains non-integer values")
