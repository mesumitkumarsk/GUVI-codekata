import numpy as np

# Get the size of the list and its elements from the user
n = int(input())
arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

# Create a NumPy array from the given list
arr = np.array(arr, dtype=int)

# Print the shape of the array
print( arr.shape)

# Transpose the array
transposed_arr = np.transpose(arr)

# Print the transposed array
print( transposed_arr)

# Print the sum of the elements in each row
print( np.sum(arr, axis=1))

# Print the minimum element in the array
print(np.min(arr))