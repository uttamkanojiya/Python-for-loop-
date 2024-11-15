#program for practicing the for else loop
height=(input('Enter the height in cms with space'))
list1=height.split()
count=0
for u in list1:
    count=count+1
    #print(count)
for i in range(0,count):
    list1[i]=(int)(list1[i])
    #print(list1)
total=0
for j in list1:
    total=total+j
else:
    print('Total of the given height is',total)
avg=total/count
print('The lenght of the list1 is',count)
print('The average of the all given height',avg)
print('Round of the avg is',round(avg))
