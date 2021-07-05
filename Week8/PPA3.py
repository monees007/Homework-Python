requests, count = {}, 0
log = {'O': 0, 'W': 0, 'C': 0, 'S': 0}
p = input()
while p != '':
    time_in_min = int(p[0:2]) * 60 + int(p[3:5])
    if time_in_min in requests:
        requests[time_in_min] = ''
    else:
        requests[time_in_min] = p
    p = input()

for time in requests:
    if 600 <= time <= 1020:
        for category in log:
            if category in requests[time]:
                booking = int(requests[time][requests[time].index(category) + 1:requests[time].index(category) + 4])
                if (count + booking) < 100:
                    log[category] += booking
                    count += booking
