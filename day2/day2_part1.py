with open("input.txt", "r") as file: # O(n)
    lines=file.readlines()
    rotations=[l.strip() for l in lines]