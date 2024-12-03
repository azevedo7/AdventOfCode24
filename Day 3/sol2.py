import re

with open("input.txt") as f:
    text = f.read()

results = re.findall(r"(mul\(\d{1,3},\d{1,3}\))|((do\(\)|don\'t\(\)))", text)
results = [match[0] or match[1] or match[2] for match in results]

total = 0
active = True 
for result in results:
    if result == "do()":
        active = True
        continue
    elif result == "don't()":
        active = False
        continue
    else:
        if(active):
            a,b = map(int, result[4:-1].split(","))
            total += a * b

print(total)