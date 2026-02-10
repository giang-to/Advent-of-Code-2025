with open("input.txt", "r") as file: # O(n)
    lines=file.readlines()
    rotations=[l.strip() for l in lines]
res=0
curr_pos=50
for r in rotations:
    dir=r[0]
    step=int(r[1:])
    if dir=='R':
        curr_pos = (curr_pos + step) % 100
    else:
        curr_pos = (curr_pos - step) % 100
    if curr_pos==0:
        res+=1
print(res)   #correct answer: 1132
