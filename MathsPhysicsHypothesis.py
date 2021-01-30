mathsMarks = [68,62,57,42,87,71,81,84,74,63,64,97,52,65,89,76,87,62,72,56,93,78,62,97,44,87,74,81,74,72]
physicsMarks = [64,45,54,53,64,92,82,92,64,88,72,92,64,73,62,58,86,81,92,78,68,69,62,91,72,75,71,76,83,66]
chemMarks = [78,91,77,78,89,84,87,76,51,73,68,92,71,89,93,90,43,67,97,62,91,74,57,88,58,92,82,52,83,81]

from shortcutsj import *

MathLIL = ListInList(mathsMarks)
PhysicsLIL = ListInList(physicsMarks)
ChemLIL = ListInList(chemMarks)

# Sorting the marks in decending order

SortedMaths = invertList(sortListinL(MathLIL))
SortedPhysics = invertList(sortListinL(PhysicsLIL))

# Assigning the grades

MathsA=assignGrade(SortedMaths,'A')
MathsB=assignGrade(SortedMaths,'B')
MathsC=assignGrade(SortedMaths,'C')

PhysicsA=assignGrade(SortedPhysics,'A')
PhysicsB=assignGrade(SortedPhysics,'B')
PhysicsC=assignGrade(SortedPhysics,'C')

# If same or higher grade in physics as in Maths 
def CheckThesis():
    AGraders=[]
    BGraders=[]
    for p in MathsA:
        for q in PhysicsA:
            if first(p)==first(q):
                AGraders = AGraders + ['T']
             
    for p in MathsB:
        for q in PhysicsA+PhysicsB:
            if first(p)==first(q):
                BGraders = BGraders + ['t']
    print(AGraders)
    print(BGraders)
    print('Supporters')
    print(len(AGraders)+len(BGraders))
    print('over')
    print(30)
    print('It means')
    percent=len(AGraders)+len(BGraders)*100/30
    print(percent) 
  

# Returns
CheckThesis()
#print(assignGrade(SortedMaths))