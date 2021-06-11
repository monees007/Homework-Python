import math, statistics


def avg(x):
    s = 0
    for i in x:
        s += i
    return s / len(x)


def sd(x):
    sum = 0
    for i in x:
        sum += ((i - avg(x)) ** 2)
    return (sum ** (1 / 2))


def pearson_correlation(x, y):
    x_ = avg(x)
    y_ = avg(y)
    sd_x = sd(x)
    sd_y = sd(y)
    sum = 0
    for i in range(len(x)):
        sum += ((x[i] - x_) * (y[i] - y_))

    r = sum / (sd_x * sd_y)

    if len(x) != len(y):
        return 0.0
    else:
        return round(r, 1)
# Submission Successful! 9 out of 9 private test(s) passed.
