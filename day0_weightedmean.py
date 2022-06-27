def weightedMean(X, W):
    # Write your code here
    product_list = []
    for i in range(len(X)):
        product = X[i] * W[i]
        product_list.append(product)
    sum_plist = sum(product_list)
    sum_w = sum(W)
    w_mean = sum_plist / sum_w
    return round(w_mean, 1)

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    print(weightedMean(vals, weights))