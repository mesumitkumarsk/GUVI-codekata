def sort_names(names):
    # Sort the list of names using Python's built-in sorted() function
    return sorted(names)

# Read number of names
n = int(input())

# Read names into a list
names = [input().strip() for _ in range(n)]

# Sort the names
sorted_names = sort_names(names)

# Print sorted names
for name in sorted_names:
    print(name)
