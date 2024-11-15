#program for practice
numbers=(input("Enter the number with space"))
list1=numbers.split()
count=0
for i in list1:
    count=count+1
else:
    print('The lenght of the given number list is',count)
for j in range(0,count):
    list1[j]=int(list1[j])
else:
    print('The given list is ',list1)
maximumnumber=list1[0]
for u in list1:
    if u>maximumnumber:
        maximumnumber=u
else:
    print('The maximum number form the given list is ',maximumnumber)
