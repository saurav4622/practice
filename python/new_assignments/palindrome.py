def palindrome(n):
    sum_1 = 0
    copy = n
    while n > 0:
        a = n % 10
        sum_1 = sum_1 * 10 + a
        n = n // 10
    if sum_1 != copy:
        return "Non-Palindrome"
    else:
        return "Palindrome"
new = int(input("Enter a number: "))
print(palindrome(new))