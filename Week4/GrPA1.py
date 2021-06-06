import statistics

i_list = []
x = float(input())
while str(x) != 'END':
    i_list += [float(x)]
    x = input()

x_bar = statistics.mean(i_list)
sd = statistics.stdev(i_list, x_bar)
sd = round(sd, 2)
print(sd, end='')

# Submission Successful! 3 out of 4 private test(s) passed.
