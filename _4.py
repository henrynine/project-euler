def is_palindrome(string):
    for n in range(int(len(string)/2)):
        if string[n]!=string[-(n+1)]:
            return False
    return True

largest_palindrome = 1
for factor1 in range(100, 999):
    for factor2 in range(100, 999):
        product = factor1*factor2
        if is_palindrome(str(product)) and product > largest_palindrome:
            largest_palindrome = product
print(largest_palindrome)
