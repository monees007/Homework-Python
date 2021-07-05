TEST_CASE = input()
numberOfStudents = int(input())
inde = list(input().split(","))
students = {}

for i in range(numberOfStudents):
    index_v = list(input().split(","))
    students[int(index_v[0])] = {}
    for j in range(1, len(inde)):
        students[int(index_v[0])][inde[j]] = int(index_v[j])

# Submission Successful! 2 out of 2 private test(s) passed.
