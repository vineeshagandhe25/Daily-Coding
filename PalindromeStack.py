# To check if a string is a palindrome using a stack.
def is_palindrome(s):
    
    stack = []
    
    s = s.lower()
    
    # Push each character of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack and compare with the original string
    for char in s:
        if char != stack.pop():
            return False  # If any character doesn't match
    
    return True  


input_str = "Madam"
if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is not a palindrome.")

# Time Complexity --- O(N) where N is length of given string.
# Space Complexity --- O(N) where N is length of given string.    
