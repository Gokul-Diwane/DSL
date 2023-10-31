n=int(input("Enter total no of students in class : "))
total=[]
for i in range (n):
    name=str(input("Enter the name of student : "))
    total.append(name)
print ("The students in class are ",total)

cricket=[]
n_cric=int(input("Enter the number of students who play cricket : "))
for i in range (n_cric):
    cric_name=str(input("Enter the name of student who play cricket : "))
    cricket.append(cric_name)
print ("Students who play cricket are ",cricket)

badminton=[]
n_bad=int(input("Enter the number of students who play badminton : "))
for i in range (n_bad):
    bad_name=str(input("Enter the name of student who play badminton : "))
    badminton.append(bad_name)
print ("Students who play badminton are ",badminton)

football=[]
n_ft=int(input("Enter the number of students who play football : "))
for i in range (n_ft):
    c_ft=str(input("Enter the name of student who play football : "))
    football.append(c_ft)
print ("Students who play football are ",football)

def cric_and_bad(l1,l2,l3):
    l4=[]
    for i in l1:
        if i in l2 and i in l3:
            l4.append(i)
    print ("Stduents who play both cricket and badminton are ",l4)


def cric_or_bad(l1,l2,l3):
    l4=[]
    for i in l1:
        if i in l3 and i not in l2:
            l4.append(i)
    for i in l2:
        if i in l3 and i not in l1:
            l4.append(i)
    print ("Students who either play cricket or badminton are ",l4)


def nor_cric_bad(l1,l2,l3):
    l4=[]
    for i in l3:
        if i not in l1 and i not in l2:
            l4.append(i)
    print ("Number of students who neither play cricket nor badminton is ",len(l4))
 

def cric_and_ft_not_bad(l1,l2,l3,l4):
    l5=[]
    for i in l4:
        if i in l1 and i in l3 and i not in l2:
            l5.append(i)
    print ("Number of students who play cricket and football but not badminton is ",len(l5))


flag=1
while (flag):
    print ("\n####################MENU####################")
    print ("1.Display stduents who play both cricket and badminton")
    print ("2.Display students who either play cricket or badminton")
    print ("3.Display number of students who neither play cricket nor badminton ")
    print ("4.Display number of students who play cricket and football but not badminton")
    print ("5.Exit")
    ch=int(input("Enter yur choice : "))
    if ch==1:
        cric_and_bad(cricket,badminton,total)
    elif ch==2:
        cric_or_bad(cricket,badminton,total)
    elif ch==3:
        nor_cric_bad(cricket,badminton,total)
    elif ch==4:
        cric_and_ft_not_bad(cricket,badminton,football,total)
    elif ch==5:
        flag=0
    else:
        print ("Enter valid choice !!!")
