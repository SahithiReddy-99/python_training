class Mobiles:
    def __init__(self,name, model, price, count): 
        self.name = name
        self.model = model
        self.price = price
        self.count = count
        
    def __str__(self):
        return self.name+" "+self.model+" "+str(self.price)+"  "+str(self.count)


stock=[]
while 1:
    i = int(input("enter 1 to search\nenter 2 to add mobile\nenter 3 to display\nenter 4 to terminate"))
    if i == 1:
        name=input("Enter Mobile Brand")
        model=input("Enter Mobile Model")
        if stock:
            for i in stock:
                if i.name==name and i.model==model:
                    print(i.count)
        else:
            print("Your shop is FAKE")
        
    
        
    elif i == 2:
        name=input("Enter Mobile Brand")
        model=input("Enter Mobile Model")
        price = input("Enter Price")
        count=int(input("Enter count"))

        for i in stock:
            if i.name==name and i.model==model:
                i.count=i.count+count
        else:
            new_obj=Mobiles(name,model,price,count)
            stock.append(new_obj)

        for i in stock:
            print(i)
            
    elif i==4:
        break
    else:
        print("Enter a valid Input")
        
