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
        #if curr_pos=0, only count complete circle
        if curr_pos==0:
            res+=step//100
        else:
            #count complete circle + if end point is 0
            if step >= curr_pos:
                res += (step-curr_pos) // 100+1
        curr_pos = (curr_pos - step) % 100
print(res)  #answer: 6623
#Note: if step>=curr_pos, we goes back curr_pos steps ending at 0 (which gives 1 hit).
# Then from 0, we move back (step-curr_pos) steps.
# we count how many compelte circle , which is (step-curr_pos)//100