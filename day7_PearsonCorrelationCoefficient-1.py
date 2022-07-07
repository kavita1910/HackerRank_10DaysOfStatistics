import statistics 

n = int(float(input()))
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

def pCorrelation(n, X, Y):
  mean_x = statistics.mean(X)
  mean_y = statistics.mean(Y)
  std_x = statistics.stdev(X)
  std_y = statistics.stdev(Y)
  num = 0
  for i in range(n):
      num += (X[i] - mean_x) * (Y[i] - mean_y)
  return num / (n * std_x * std_y)
  
print(round(pCorrelation(n, X, Y), 3))