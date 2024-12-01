
with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f];
    a,b =  map(list, zip(*[map(int, line.split()) for line in lines]))

    a.sort();
    b.sort();

    sums = [abs(x - y) for x, y in zip(a, b)]

c = {};

for n in b:
    if n not in c:
        c[n] = 1;
    else:
        c[n] += 1;

sum2 = 0

for n in a:
    if n in c: 
        sum2 += n * c[n]

print(sum2)