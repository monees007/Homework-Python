def solution():
    '''
    1. Process version_1.txt and version_2.txt
    2. Print the number lines in version_2.txt that are not in version_1.txt
    '''
    v1 = open('version_1.txt', 'r')
    v2 = open('version_2.txt', 'r')

    content1, content2 = [], []
    for i in v1.readlines():
        content1.append(i.strip())
    for i in v2.readlines():
        content2.append(i.strip())
    # print(content1)
    # print(content2)

    result = 0
    for i in content2:
        if 0 != content1.count(i):
            continue
        result += 1
        # print(i)
    print(result)
# Submission Successful! 4 out of 4 private test(s) passed.