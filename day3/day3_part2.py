with open("input.txt", "r") as file:
    lines = file.readlines()
    data = [line.strip() for line in lines]


def max_n_digits(s,n):
    """
    Return the string of the maximum n-digit number formed by digits of
    a string s in order
    """
    if n > len(s):
        return ''
    elif n == len(s):
        return s
    # if len(s)>n
    res = ''
    while n > 0:
        # the first digit of the result=maximum digit among the first len(s)-n+1 digits of s
        ind, max_digit = max(enumerate(s[: len(s)-n+1]), key=lambda x: int(x[1]))
        res += max_digit
        # after the first digit is determined, the problem becomes finding the maximum (n-1)-digit number
        # formed by digits of s from the index ind+1
        s = s[ind+1:]
        n = n-1
    return res


p2=0
for text in data:
    p2+=int(max_n_digits(text,12))
print(p2)
# Note: this function also work for part 1 with n=2