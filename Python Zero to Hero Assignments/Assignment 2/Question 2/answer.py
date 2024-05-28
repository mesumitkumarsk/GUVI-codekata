def list_of_squares(n):
    return [i ** 2 for i in range(1, n + 1)]

n = int(input())
squares = list_of_squares(n)
print(", ".join(map(str, squares)))