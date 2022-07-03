# A random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.
e = 2.71828
mean = 2.5
k = 5

def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n

result = ((mean**k) * (e**-mean)) / factorial(k)
print(round(result, 3))