def Palindrome(str):
    if(len(str) <=1):
        return True
    
    return str[0] == str[-1] and Palindrome(str[1:-1])

print(Palindrome('Hello'))