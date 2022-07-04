means = list(map(float, input().split()))
mean_a = means[0]
mean_b = means[1]

print (round(160 + 40 * (mean_a + mean_a ** 2), 3))
print (round(128 + 40 * (mean_b + mean_b ** 2), 3))