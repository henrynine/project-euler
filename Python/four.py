def is_palindrome(string):
    for n in range(int((len(string)-1)/2)):
        if string[n]!=string[-(n+1)]:
            return False
    return True
