from collections import defaultdict

with open("/Users/jachinchoi/AOC/AOC 2024/Day_1/input.txt") as input:
    data = input.readlines()
list1 = []
list2 = list()
ans = 0
count = defaultdict(int)

for line in data:
    line.strip()
    values = line.split()
    list1.append(int(values[0]))
    list2.append(int(values[1]))

for value in list2:
    count[value] += 1

for curr in list1:
    ans += count[curr] * curr

print(ans)


