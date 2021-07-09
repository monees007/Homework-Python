def solution():
    """
    0. Read the file.
    1. Accept input from the user as specified in the question.
    2. The input will be on three lines.
    3. For each of the three questions given in the problem statement,
       print your answer.

1. What is the population in the given year?
    The first line of input is a year. Print the population in this year.
2. When did the world population first exceed the given population?
    The second line of input is a positive number. Print the earliest year in which the world population exceeded the given number.
3. What is the maximum value of the given field?
    The third line of input is the name of a field in the header, print the maximum value in the given field.
    """

    given_year = input()
    given_population = input()
    given_field = input()
    printed2 = 0

    f = open('WorldPopulation.csv', 'r')
    # content should be nested list
    content = []
    for i in f.readlines():
        content = [list(i.strip().split(','))] + content  # content is reverted
    printed2 = 0
    for i in content[:-1]:
        if i[0] == given_year:
            print(i[1])  # first question answered

    for i in content[:-1]:
        if i[1] > given_population and printed2 == 0:
            print(i[0])  # second question answered
            printed2 = 1

    index = content[-1].index(given_field)
    max0 = 0
    for i in content[:-1]:
        if max0 < float(i[index]):
            max0 = float(i[index])
    print(max0)
# Submission Successful! 3 out of 3 private test(s) passed.
