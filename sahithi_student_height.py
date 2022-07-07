class Student:
    def __init__(self,name,heigth,weigth,age):
        self.name=name
        self.heigth=heigth
        self.weigth=weigth
        self.age=age
    def __str__(self) :
        return "name = "+self.name+" "+ "heigth in cm= "+str(self.heigth)
    def __lt__(self,other):
        return self.heigth<other.heigth
    def __gt__(self,other):
        return self.heigth<other.heigth



record=[]

istrue=True
while(istrue):
    print(" enter 1 add a student \n two view heigth of a student \n 3  change the heigth of a student \n 4  view entire student list")
    print (" 5 to exit")
    x=input()
    if x=='1':
        print("enter the name,heigth,weigth and age in seperate lines")
        name=input()
        heigth=float(input())
        weigth=float(input())
        age=int(input())
        student=Student(name,heigth,weigth,age)
        record.append(student)
        print(student, end=" ")
        print(" is added to list")
    if (x=='2'):
        print(" enter name of student to view heigth")
        isinrecord=False
        name=input()
        for ele in record:
            if(ele.name==name):
                isinrecord=True
                print(ele)
        if(isinrecord==False):
            print("there is no such student with name"+str(name))
    if (x=='3'):
        print(" enter name of student and  heigth of student to change heigth")
        name=input()
        heigth=float(input())
        isinrecord=False

        for ele in sorted(record):
            if(ele.name==name):
                isinrecord=True
                print("the heigth of student is changed from "+str(ele.heigth)+" to "+str(heigth))
                ele.heigth=heigth
        if(isinrecord==False):
            print("there is no such student with name"+str(name))
    if(x=='4'):
        for ele in record:
            print(ele)
    if(x=='5'):
        isture=False
