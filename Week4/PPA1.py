units = int(input())
bill = 0
if units <= 100:
    bill += 0
elif 100 < units <= 200:
    units -= 100
    bill += units * 5
elif 200 < units <= 500:
    units -= 200
    bill += 500
    bill += units * 8
else:
    units -= 500
    bill += (500 + 2400)
    bill += 10 * units
print(bill)
# Submission Successful! 4 out of 4 private test(s) passed.
