from sklearn import linear_model

m,n = input().split()
inputs = []
for i in range(int(n)):
    inputs.append([float(j) for j in input().split()])
    
y = [x.pop() for x in inputs]
f = input() 
x = []
for k in range(f): 
    x.append([float(l) for l in input().split()])

lm = linear_model.LinearRegression()
lm.fit(inputs, y)
a = lm.intercept_
b = lm.coef_

for m in range(0, len(x)):
    out = a + x[m][0] * b[0] + x[m][1] * b[1]
    print(out)