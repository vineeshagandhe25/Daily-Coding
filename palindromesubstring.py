# Write a Python function that takes a string as input and returns the longest palindrome substring within that string.

def substring(s):
    res = ''
    for char in range(len(s)):
        for end in range(len(s), char, -1):
            if end - char <= len(res):
                break
            if s[char:end] == s[char:end][::-1] and end - char > len(res):
                res = s[char:end]
    return res

print(substring('i love my mom'))