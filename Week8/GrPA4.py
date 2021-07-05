def add_movie_to_boxoffice(db,n_movie):
    db[n_movie[0]]=list(n_movie[1:])
    return db
def total_collection(db):
    sum0,count0=0,0
    for i in db:
        sum0+=db[i][0]
        count0+=1
    return sum0
def average_collection(db):
    sum0,count0=0,0
    for i in db:
        sum0+=db[i][0]
        count0+=1
    return round(sum0/count0,2)
def num_of_movies_above_average_movies(db):
    sum0,count0=0,0
    for i in db:
        sum0+=db[i][0]
        count0+=1
    average0=sum0/count0
    count1=0
    for i in db:
        if db[i][0] > average0:
            count1+=1
    return count1
def highest_grossing_movie_year(db):
    max0,year=0,0
    for i in db:
        if db[i][0] > max0:
            max0 = db[i][0]
            year=db[i][2]
    return year