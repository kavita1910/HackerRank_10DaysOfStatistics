N = int(input())
X = list(map(int, input().strip().split()))[:N]

def mean_func(N, X):
    return sum(X)/ N

def median_func(N, X):
  X.sort()  
  if N % 2 == 0:
      median1 = X[N//2]
      median2 = X[N//2 - 1]
      median = (median1 + median2)/2
  else:
      median = X[N//2]
  return median
        
def mode_func(N, X):
    matrx = []
    for i in set(X):
        lst_count = X.count(i)
        matrx.append([i, lst_count])

    mode_dict = dict(matrx)

    mode_lst = []
    for k, v in mode_dict.items():
        if v == max(list(mode_dict.values())):
          mode_lst.append(k)
          
    return min(mode_lst)

print(mean_func(N, X))
print(median_func(N, X))
print(mode_func(N, X))