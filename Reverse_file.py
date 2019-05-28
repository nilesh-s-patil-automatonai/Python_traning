import io
file_name=input("enter file name")
fd=open(file_name)
line= fd.readline()
while line != '':
    for line in reversed(line):
        print(line,end=" ")
    line=fd.readline()
