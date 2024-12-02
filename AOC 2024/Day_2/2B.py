with open("/Users/jachinchoi/AOC/AOC 2024/Day_2/input.txt") as file:
    data = file.readlines()
res = 0

for line in data:
    line.strip()
    curr = line.split()
    i = 0
    addOne = False
    while i < len(curr):
        currValue = curr.pop(i)
        valid = True
        print(curr)
        change = int(curr[1]) - int(curr[0])
        if abs(change) >= 1 and abs(change) <= 3:
            if change > 0:
                for index in range(2,len(curr)):
                    pos = int(curr[index]) - int(curr[index - 1])
                    if pos < 1 or pos > 3:
                        valid = False
            else:
                for index in range(2, len(curr)):
                    neg = int(curr[index - 1]) - int(curr[index])
                    if neg < 1 or neg > 3:
                        valid = False
            if valid:
                addOne = True
        curr.insert(i, currValue)
        i += 1
    if addOne:
        res += 1
print(res)