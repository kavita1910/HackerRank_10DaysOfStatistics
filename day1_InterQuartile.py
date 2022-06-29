n = int(input().strip())
val = list(map(int, input().rstrip().split()))
freq = list(map(int, input().rstrip().split()))


def get_median(S):
  mid = len(S) // 2
  if len(S) % 2 == 0:
    return (S[mid] + S[mid-1])/2
  else:
    return S[mid]

def interQuartiles(val, freq):
  S = []
  for f,v in zip(freq, val):
    for i in range(f):
      S.append(v)
  S.sort()
  # Q2 = int(get_median(data))
  n = len(S)
  mid = len(S) // 2
  # start = 0
  if n % 2 == 0:
    Q1 = int(get_median(S[0 : mid]))
    Q3 = int(get_median(S[mid : n]))
  else:
    Q1 = int(get_median(S[0 : mid]))
    Q3 = int(get_median(S[mid + 1 : n]))
  diff = Q3 - Q1
  return float(diff)

print(interQuartiles(val, freq))