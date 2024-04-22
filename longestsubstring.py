# Problem: Given a string s, find the length of the longest substring without repeating characters.

def longestsubstring(string):
    if not string :
        return 0
    
    max_length=0
    start=0
    char_index={}

    for end in range(len(string)):   # Time Complexity --- O(n) 
        # if current char is already in map then we update start 
        if string[end] in char_index:
            start=max(start,char_index[string[end]]+1)
        char_index[string[end]]=end
        max_length=max(max_length,end-start+1)

    return max_length

s='abcdabababab'
print(longestsubstring(s))        

# * Time Complexity --- O(n) where n is the length of string
# * Space Complexity --- O(1)