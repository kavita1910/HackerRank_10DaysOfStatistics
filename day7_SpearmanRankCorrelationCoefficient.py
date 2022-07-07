n = int(input())
X = [float(x) for x in input().split()]
Y = [float(x) for x in input().split()]


def rank(X):
    lst = []
    for i in X:
        lst.append(sorted(X).index(i) + 1)
    return lst


def spearman(X, Y, rank_x, rank_y, n):
    diffs = []
    for x, y in zip(rank_x, rank_y):
        diffs.append((x - y)**2)
        coeff = 1 - (6 * sum(diffs)) / (n**3 - n)
    return coeff


rank_x = rank(X)
rank_y = rank(Y)
spearman_rank = spearman(X, Y, rank_x, rank_y, n)
print(round(spearman_rank, 3))
