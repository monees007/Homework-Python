mathsMarks = [68,62,57,42,87,71,81,84,74,63,64,97,52,65,89,76,87,62,72,56,93,78,62,97,44,87,74,81,74,72]
physicsMarks = [64,45,54,53,64,92,82,92,64,88,72,92,64,73,62,58,86,81,92,78,68,69,62,91,72,75,71,76,83,66]
chemMarks = [78,91,77,78,89,84,87,76,51,73,68,92,71,89,93,90,43,67,97,62,91,74,57,88,58,92,82,52,83,81]

def ListInList(p):
    i = 0
    Class = []
    for q in p:
        Student = [i,q]
        i= i + 1
        Class = Class + [Student]
        Student = []
    return(Class)

MathLIL = ListInList(mathsMarks)
PhysicsLIL = ListInList(physicsMarks)
ChemLIL = ListInList(chemMarks)
