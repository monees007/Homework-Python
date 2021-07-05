def trending(subject_topics):
    """
    :param subject_topics: list of list of topics in one subject
    :return: count_top_trending, count_least_trending
    """
    list0 = []
    db = []  # list of count, and topic
    for x in subject_topics:
        for y in list(set(x)):
            list0.append(y)
    set_of_topics = set(list0)
    for topic0 in set_of_topics:
        db.append([list0.count(topic0), topic0])
    highest_freq, lowest_freq = 0,9999999999999999
    for i in db:
        if highest_freq < i[0]:
            highest_freq = i[0]
        if lowest_freq > i[0]:
            lowest_freq = i[0]
    count_top_trending, count_least_trending = 0, 0
    for i in db:
        if i[0] == highest_freq:
            count_top_trending+=1
        if i[0] == lowest_freq:
            count_least_trending+=1
    return count_top_trending,count_least_trending
# Submission Successful! 2 out of 2 private test(s) passed.
