f=open("/home/monees007/Projects/Homework-Python/Sideways/File_Handling/abc.csv",'r')
x=f.readlines()
# print(type(x))
# print()
content=[]
for i in x:
    content.append(i.strip().split(','))
print(type(f))
print(content)
