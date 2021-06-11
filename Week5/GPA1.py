def perfect_number(num):
    divisors = []
    for i in range(num - 1, 0, -1):
        if num % i == 0:
            divisors.append(i)
    sumo = 0
    # print(divisors)
    for i in divisors:
        sumo += i
    if sumo == num:
        # print('T')
        return True
    else:
        # print('F')
        return False

# perfect_number(28)
#  Submission Successful! 4 out of 4 private test(s) passed.
