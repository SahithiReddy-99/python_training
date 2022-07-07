class Student:
    def __init__(self,name,height,weigth,age):
        self.name=name
        self.height=height
        self.weigth=weigth
        self.age=age
    def __str__(self) :
        return "name = "+self.name+" "+ "height in cm= "+str(self.height)
    def __lt__(self,other):
        return self.height<other.height
    def __gt__(self,other):
        return self.height<other.height

record=[]

while(True):
    print(" enter 1 add a student \n two view height of a student \n 3  change the height of a student \n 4  view entire student list")
    print (" 5 to exit")
    x=input()
    if x=='1':
        print("enter the name,height,weigth and age in seperate lines")
        name=input()
        height=float(input())
        weigth=float(input())
        age=int(input())
        student=Student(name,height,weigth,age)
        record.append(student)
        print(student, end=" ")
        print(" is added to list")
    if (x=='2'):
        print(" enter name of student to view height")
        isinrecord=False
        name=input()
        for ele in record:
            if(ele.name==name):
                isinrecord=True
                print(ele)
        if(isinrecord==False):
            print("there is no such student with name"+str(name))
    if (x=='3'):
        print(" enter name of student and  height of student to change height")
        name=input()
        height=float(input())
        isinrecord=False

        for ele in sorted(record):
            if(ele.name==name):
                isinrecord=True
                print("the height of student is changed from "+str(ele.height)+" to "+str(height))
                ele.height=height
        if(isinrecord==False):
            print("there is no such student with name"+str(name))
    if(x=='4'):
        for ele in record:
            print(ele)
    if(x=='5'):
        break
