with open("/Users/jachinchoi/AOC/AOC 2024/Day_2/input.txt") as file:
    data = file.readlines()
    file.close()
res = 0

for line in data:
    valid = True
    line.strip()
    curr = line.split()
    change = int(curr[1]) - int(curr[0])
    if abs(change) < 1 or abs(change) > 3:
        continue
    else:
        if change > 0:
            for index in range(2,len(curr)):
                pos = int(curr[index]) - int(curr[index - 1])
                if pos < 1 or pos > 3:
                    valid = False
                    break
        else:
            for index in range(2, len(curr)):
                neg = int(curr[index - 1]) - int(curr[index])
                if neg < 1 or neg > 3:
                    valid = False
        if valid:
            res += 1
print(res)