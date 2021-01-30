mathsMarks = [68,62,57,42,87,71,81,84,74,63,64,97,52,65,89,76,87,62,72,56,93,78,62,97,44,87,74,81,74,72]
physicsMarks = [64,45,54,53,64,92,82,92,64,88,72,92,64,73,62,58,86,81,92,78,68,69,62,91,72,75,71,76,83,66]
chemMarks = [78,91,77,78,89,84,87,76,51,73,68,92,71,89,93,90,43,67,97,62,91,74,57,88,58,92,82,52,83,81]

from shortcutsj import last,first,ListInList

# Make List in List of marks with ID as [ ID , Mark ]

MathLIL = ListInList(mathsMarks)
PhysicsLIL = ListInList(physicsMarks)
ChemLIL = ListInList(chemMarks)

# Get the top third mark as cutoff

def topThreeMarks(a):
    FirstPlace = [1]
    SecondPlace = [1]
    ThirdPlace= [1]
    for b in a:
        if last(b) > last(FirstPlace):
            ThirdPlace = SecondPlace
            SecondPlace = FirstPlace
            FirstPlace = b
        if last(FirstPlace) > last(b) > last(SecondPlace):
            ThirdPlace = SecondPlace
            SecondPlace = b
        if last(SecondPlace) > last(b) > last(ThirdPlace):
            ThirdPlace = b
    return(ThirdPlace)

cutoffM = last(topThreeMarks(MathLIL))
cutoffP = last(topThreeMarks(PhysicsLIL))
cutoffC = last(topThreeMarks(ChemLIL))

# Students scoring more than cutoff

def topperS(Marksheet, cutoff):
    Toppers = []
    for p in Marksheet:
        if last(p) >= cutoff:
            Toppers = Toppers + [p]
    return(Toppers)

topperM = topperS(MathLIL,cutoffM)
topperP = topperS(PhysicsLIL,cutoffP)
topperC = topperS(ChemLIL,cutoffC)
print(topperM)
print(topperP)
print(topperC)
#these above are list of lists.

# compare two list for  same students

def topperAB(Sub1,Sub2):
    TopperAB = []
    for a in Sub1:
        for b in Sub2:
            p = first(a)
            q = first(b)
            if p == q:
                TopperAB = TopperAB + [b]
    return(TopperAB)

topperMP = topperAB(topperM,topperP)
topperMPC = topperAB(topperMP,topperC)

# This is overall Topper

print(topperMPC)
