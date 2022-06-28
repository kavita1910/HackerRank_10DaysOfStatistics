n = int(input().strip())
data = sorted(list(map(int, input().rstrip().split())))

def get_median(data):
  mid = len(data) // 2
  if len(data) % 2 == 0:
    return (data[mid] + data[mid-1])/2
  else:
    return data[mid]

def quartiles(data):
  Q2 = int(get_median(data))
  n = len(data)
  mid = len(data) // 2
  # start = 0
  if n % 2 == 0:
    Q1 = int(get_median(data[0 : mid]))
    Q3 = int(get_median(data[mid : n]))
  else:
    Q1 = int(get_median(data[0 : mid]))
    Q3 = int(get_median(data[mid + 1 : n]))
  return Q1, Q2, Q3

print(quartiles(data))
