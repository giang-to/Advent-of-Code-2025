with open("input.txt", "r") as file:  # O(n)
    lines = file.readlines()
    rotations = [l.strip() for l in lines]
res = 0
curr_pos = 50
for r in rotations:
    dir = r[0]
    step = int(r[1:])
    if dir == 'R':
        res += (curr_pos + step) // 100
        curr_pos = (curr_pos + step) % 100
    else:
        if curr_pos==0:
            res+=step//100
        else:
            if step >= curr_pos:
                res += (step-curr_pos) // 100+1
        curr_pos = (curr_pos - step) % 100
print(res)  #6623
