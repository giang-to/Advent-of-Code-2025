with open("input.txt", "r") as file:
    ID=file.readline().split(',')

import math

# Möbius function μ(n) for n = 1..10
MU = {1: 1, 2: -1, 3: -1, 4: 0,5: -1,
      6: 1, 7: -1, 8: 0, 9: 0, 10: 1}

# Divisors for n = 1..10
DIVS = {
    1:  [1],
    2:  [1, 2],
    3:  [1, 3],
    4:  [1, 2, 4],
    5:  [1, 5],
    6:  [1, 2, 3, 6],
    7:  [1, 7],
    8:  [1, 2, 4, 8],
    9:  [1, 3, 9],
    10: [1, 2, 5, 10]}

def arith_sum(m, M):
    """
    Return sum of numbers from m to M
    """
    if m > M:
        return 0
    return (M + m) * (M - m + 1) // 2


def invalid_sum_mobius(a, b):
    """
    Return the sum of all numbers in range [a,b]
    which are made of some sequence of digits repeated AT LEAST TWICE.
    See https://giangto.com/2026/02/23/advent-of-code-2025-day-2-mobius-inversion-formula/
    for the theory explanation
    """
    n, m = len(str(a)), len(str(b))
    total = 0
    if b < a:
        print("Empty range!")
        return 0

    if n == m:
        Fn = 0
        # compute Fn
        for d in DIVS[n]:
            k = n // d
            R = (10 ** n - 1) // (10 ** k - 1)
            low = max(math.ceil(a / R), 10 ** (k - 1))
            high = min(math.floor(b / R), 10 ** k - 1)
            Gk = R * arith_sum(low, high)
            Fn += MU[d] * Gk
        return arith_sum(a, b) - Fn
    elif n < m:
        return invalid_sum_mobius(a, 10 ** n - 1) + invalid_sum_mobius(10 ** n, b)
    return total

p2=0
for item in ID:
    start, end=item.split('-')
    a,b = int(start), int(end)
    p2+=invalid_sum_mobius(a,b)

print(p2)  #25663320831


# Another solution without using Möbius inversion

def sum_invalid(a,b):
    """
    Return the sum of all numbers in range [a,b]
    which are made of some sequence of digits repeated AT LEAST TWICE.
    """
    D={4:[2], 6:[2,3],  8:[2,4], 9:[3], 10:[2,5]}
    ans=set()
    R=0
    start,end=str(a),str(b)
    x,y=int(start[0]),int(end[0])
    d=len(start)
    if len(start)==len(end) and len(start)>1:
        #Case 1: consider the pattern xxx..xx where all digits are the same
        for i in range(x,y+1):
            num=int(str(i)*d)
            if a<=num<=b and not (num in ans):
                R+=num
                ans.add(num)
        #Case 2: if d is not prime, there are other repeated patterns
        if d in D.keys():
            for p in D[d]:
                s=d//p
                u=int(start[:s])
                v=int(end[:s])
                for i in range(u,v+1):
                    num=int(str(i)*p)
                    if a<=num<=b and not (num in ans):
                        R+=num
                        ans.add(num)
        return R
    elif len(start)<len(end):
        return sum_invalid(a,10**len(start)-1)+sum_invalid(10**len(start),b)
    return 0

q2=0
for item in ID:
    start, end=item.split('-')
    a,b = int(start), int(end)
    q2+=sum_invalid(a,b)

print(q2)  #25663320831