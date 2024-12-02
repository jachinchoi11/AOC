with open("/Users/jachinchoi/AOC/AOC 2024/Day_1/input.txt") as input:
    data = input.readlines()
    
list1 = list()
list2 = list()

for line in data:
    line.strip()
    curr = line.split()
    list1.append(int(curr[0]))
    list2.append(int(curr[1]))

list1.sort()
list2.sort()
ans = 0

for value1, value2 in zip(list1, list2):
    ans += abs(value1 - value2)

print(ans)








    