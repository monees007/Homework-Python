def solution():
    '''
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
    '''


    year_ = input()
    population_ = input()
    max_of_the_field = input()

    f = open('WorldPopulation.csv', 'r')
    content = f.readlines()
    printed2 = 0
    for x in content:
        if x[0] == year_:
            print(x[1])  # answer to first question
        if x[1] > population_ and printed2 == 0:
            print(x[0])  # answer to second question
            printed2 = 1
    m = content[0].index(max_of_the_field)  # index_of_given_field
    max1 = 0
    for i in content:
        if max1 < i[m]:
            max1 = i[m]
    print(max1)  # answer to third question
