def remove_duplicates(lst: str) -> str:
    # Split the input string by commas to get the list of integers as strings
    elements = lst.split(',')
    
    # Use a set to keep track of seen elements and a list to store the result
    seen = set()
    result = []
    
    # Iterate over the elements and add to the result if not seen
    for element in elements:
        if element not in seen:
            seen.add(element)
            result.append(element)
    
    # Join the result list into a comma-separated string
    return ','.join(result)

# Example usage
input_string = input()
print(remove_duplicates(input_string))
