x,y=input(),input()
for i in x:
    for j in y:
        if i == j:
            y=y[:y.index(i)]+y[y.index(i+1):]
print(y)