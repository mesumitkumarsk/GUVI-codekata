import string

def is_palindrome(s: str) -> bool:
    # Remove spaces, punctuation, and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage
input_string = input()
print(is_palindrome(input_string))
