with open("input.txt", "r") as file:
    ID=file.readline().split(',')

def sum_invalid_twice(a,b):
    """
    Return the sum of all numbers in range [a,b]
    which are made of some sequence of digits repeated TWICE.
    """
    n,m=len(str(a)),len(str(b))
    total=0
    if b<a:
        return 0
    if n==m:
        if n%2==0:
            d=n//2
            head1, tail1=str(a)[:d], str(a)[d:]
            head2, tail2=str(b)[:d], str(b)[d:]
            s=int(head1) if int(head1)>=int(tail1) else int(head1)+1
            e=int(head2) if int(head2)<=int(tail2) else int(head2)-1
            #sum all ss+....+ee
            return (10**d+1)*(s+e)*(e-s+1)//2
        #if n is odd, there is no twice-repeated pattern
        return 0
    elif n<m:
        return sum_invalid_twice(a,10**n-1)+sum_invalid_twice(10**n,b)
    return 0

p1=0
for item in ID:
    start, end=item.split('-')
    a,b = int(start), int(end)
    p1+=sum_invalid_twice(a,b)

print(p1)  #8576933996