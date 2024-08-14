class color:
    def accept(self,c1,c2):
        self.c1=c1
        self.c2=c2
    def disp(self):
        print("color one :",self.c1)
        print("color two :",self.c2)

ob=color()
c1=input("enter first color ")
c2=input("enter secound color ")
ob.accept(c1,c2)
ob.disp()            