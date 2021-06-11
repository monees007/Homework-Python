def check_leap_year(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False

# Submission Successful! 4 out of 4 private test(s) passed.
