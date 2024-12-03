import re

with open("input.txt") as f:
    text = f.read()

results = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|()", text)

total = 0
for result in results:
    a,b = map(int, result[4:-1].split(","))
    total += a * b

print(total)