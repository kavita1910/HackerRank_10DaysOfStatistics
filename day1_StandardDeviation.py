import math 

n = int(input().strip())
vals = list(map(int, input().rstrip().split()))

def stdDev(vals):
  mean_vals = sum(vals) / n
  for i in range(len(vals)):
    vals[i] = (vals[i] - mean_vals)**2
  sqr_val = math.sqrt(sum(vals)/n)
  return round(sqr_val, 1)

print(stdDev(vals))