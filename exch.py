def char_exchange(str1):
    anil=input('Enter a string:')
    return str1[-1:]+str1[1:-1]+str1[:1] 
print(char_exchange('anil'))