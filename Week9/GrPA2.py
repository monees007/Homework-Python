def highest_grossing(yearFrom, yearUpto, genre):
    """
    Arguments:
    	yearFrom: int
    	yearUpto: int
    	genre: string
    Returns:
    	movie_name: string
    """
    f = open('IMDB_reviews.csv', 'r')
    content, worth = [], []
    for i in f.readlines():
        content.append(i.strip().split(','))

    for i in content[1:]:
        if yearFrom <= int(i[2]) <= yearUpto and i[4] == genre:
            worth.append(i)

    highest_grossing0, index = 0, 0
    for i in worth:
        print(i)
        if highest_grossing0 < float(i[-1].strip()):
            highest_grossing0 = float(i[-1].strip())
            index = i
    print(index[1])
