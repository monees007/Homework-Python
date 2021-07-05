r = int(input())
c = int(input())
m = []
for i in range(r):
    m.append(input().split())

x = len(m) - 2
y = c - 2
for i in range(x):
    for j in range(y):
        m[1 + i][1 + j] = 0
st = ''
for i in range(r):
    for j in m[i]:
        st += str(j) + ' '
    print(st.strip())
    st = ''

# Submission Successful! 3 out of 3 private test(s) passed.
