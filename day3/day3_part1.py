with open("input.txt", "r") as file:
    lines = file.readlines()
    data = [line.strip() for line in lines]


def max_two_digits(s):
    """
    Return the maximum 2-digit number formed by digits of
    a string s in order
    """
    # extract the 2 largest digits of s and their indices
    # a=largest, b=second largest
    a, b = sorted(enumerate(s), key=lambda x: int(x[1]), reverse=True)[:2]
    # if the largest digit is not the last one
    if a[0] < len(s)-1:
        # the maximum number=largest digit+largest digit among digits after the largest digit's index
        second_digit = max(s[a[0] + 1:], key=int)
        return int(a[1] + second_digit)
    # if the largest digit of s is the last one
    else:
        # the maximum number=second largest + largest digit
        return int(b[1] + a[1])


total = 0
for text in data:
    total += max_two_digits(text)
print(total)
