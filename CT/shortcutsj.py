def last(p):
    lastV = []
    for q in p:
        lastV = q
    return(lastV)

def first(p):
    FirstV = []
    for q in p:
        FirstV = q
        return(FirstV)

def ListInList(p):
    i = 0
    Class = []
    for q in p:
        Student = [i,q]
        i= i + 1
        Class = Class + [Student]
        Student = []
    return(Class)

def invertList(p):
    list=[]
    for q in p:
        list = [q] + list
    return(list)

def assignGrade(SortedMarks,G):
    GradeA=[]
    GradeB=[]
    GradeC=[]
    i=1
    for p in SortedMarks:
        if i<=10:
            GradeA = GradeA+[p]
        if 10<i<=20:
            GradeB = GradeB+[p]
        if 20<i<=30:
            GradeC = GradeC+[p]
        i+=1
    if G == 'A':
        return(GradeA)
    if G == 'B':
        return(GradeB)
    if G == 'C':
        return(GradeC)

def InserstListinL(B,a):
    sortListinL = []
    inserted=1
    for b in B:
        if last(b) > last(a) and bool(inserted):
            sortListinL = sortListinL + [a]
            inserted=0
        sortListinL= sortListinL + [b]
    if bool(inserted):
        sortListinL = sortListinL+[a]
    return(sortListinL)

def sortListinL(list):
    sortedListinL = []
    for a in list:
        sortedListinL = InserstListinL(sortedListinL,a)
    return(sortedListinL)

