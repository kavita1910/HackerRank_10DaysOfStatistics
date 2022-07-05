import math

n = float(input())
mean = float(input())
std = float(input())
percent = float(input())
z = float(input())

result = z * (std / math.sqrt(n))

print(round(mean - result, 2))
print(round(mean + result, 2))