'''
This function takes two lists as parameters.
list eq1 = [a1 , b1, c1]
list eq2 = [a2 , b2, c2]
'''
def solve(eq1,eq2):
    a1,b1,c1=eq1[:]
    a2,b2,c2=eq2[:]
    x=(c1*b2-c2*b1)/(a2*b1-a1*b2)
    y=-(a1*x/b1)-c1/b1
    return int(x),int(y)

# Submission Successful! 2 out of 2 private test(s) passed.