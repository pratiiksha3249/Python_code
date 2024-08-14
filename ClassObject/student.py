class studet:
    def accept(self):
        self.rno=input("enter rno :")
        self.name=input("enter name :")
        self.per=input("enter per :")
    def disp(self):
        print("rno:",self.rno)
        print("name",self.name)
        print("per",self.per)    
ob=studet()
ob.accept()
ob.disp()        