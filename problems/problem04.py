
def is_palindrome(n):
    string = str(n)
    if string[::-1] == string:
        return True
    else:
        return False

palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i*j) and i*j > palindrome:
            palindrome = i*j
        j += 1
    i += 1

print(palindrome)