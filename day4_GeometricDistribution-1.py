# The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect occurs the 5th item produced?
probability = list(map(int, input().split()))
p = probability[0] / probability[1]
q = 1 - p
n = int(input())

result = q ** (n - 1) * p
print(round(result, 3))