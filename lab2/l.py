s=input()
def check_brackets(s):
    stack = []
    brackets = {'{', '(', '['}
    for char in s:
        if char in brackets:
            stack.append(char)
        elif not stack:
            return False
        else:
            top = stack.pop()
            if (top == '[' and char != ']') or \
                    (top =='(' and char != ')' ) or \
                    (top == '{' and char != '}'):
                return False
    return not stack
if(check_brackets(s)==True):
    print('Yes')
else:
    print('No')
    
