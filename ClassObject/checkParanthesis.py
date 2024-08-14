class validstr:
    def accept(self):
        self.s=input("etner string with paranthesis :")

    def disp(self):
        l=len(self.s)
        # print(l)
        if(l%2==0):
            for i in range(0,l):
                # print((self.s).pop())
                
                if(self.s[i] == self.s[i+1]):
                    print("true")
                elif(i!=l+1):
                    print("")

                                 
                   

ob=validstr()
ob.accept()
ob.disp()        