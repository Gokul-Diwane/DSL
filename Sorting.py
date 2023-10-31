n=int(input("Enter total number of students in the class : "))
marks=[]
for i in range (n):
    m=float(input("Enter the marks of student out off 100 : "))
    marks.append(m)
print ("Marks of students ",n,"students are : ",marks)

def selection(m1):
    for i in range (len(m1)-1):
        min=i
        for j in range (i+1,len(m1)):
            if m1[min] > m1[j]:
                min=j
        m1[i],m1[min]=m1[min],m1[i]
    print ("Marks of students after applying selection sort : ",m1)


def bubble(m2):
    for i in range (len(m2)):
        for j in range (0,len(m2)-i-1):
            if m2[j] > m2[j+1]:
                m2[j],m2[j+1]=m2[j+1],m2[j]
    print ("Marks of students after applying bubble sort : ",m2)


def top_five(m3):
    for i in range (len(m3)-1,len(m3)-6,-1):
        print (m3[i],end=" ")


flag=1
while (flag):
    print ("\n ***********************MENU***********************")
    print ("1.Sort marks of students using selection sort")
    print ("2.Sort marks of students using bubble sort")
    print ("3.Display top five marks")
    print ("4.Exit")
    ch=int(input("Enter your choice : "))
    if ch==1:
        selection(marks)
    elif ch==2:
        bubble(marks)
    elif ch==3:
        print ("Top five scores in the class are : ",end=" ")
        top_five(marks)
    elif ch==4:
        flag=0
    else:
        print ("Enter valid choice !!!")
    
