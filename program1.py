def isValid(s):
    stack = [] 
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or bracket_pairs[char] != stack.pop():
                return False
        else:
            return False

    return not stack

print(isValid("()"))         
print(isValid("()[]{}"))     
print(isValid("(]"))          


  

