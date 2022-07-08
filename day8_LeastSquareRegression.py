X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

def mean(X):
  return sum(X) / len(X)

n = 5
mean_x = mean(X)
mean_y = mean(Y)
x_sq = sum([X[i]**2 for i in range(len(X))])
xy = sum([X[i] * Y[i] for i in range(len(X))])

b = (n * xy - sum(X) * sum(Y)) / (n * x_sq - (sum(X)**2))

a = mean_y - b * mean_x

print (round(a + 80 * b, 3))