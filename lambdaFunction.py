# addition =lambda a,b,c:a+b+c
# s=addition(10,20,30)
# print(s)

# ----------------------------------------------
# ans=lambda no1 : print(no1*no1)
# print(type(ans(3)))
# ----------------------------------------------

def myfunction(n):
  return lambda n:n*3

ans=myfunction(3)
# print(ans)<---------------
# why (ans) veriables not content return value;

# here why it must to pass value to (ans) veriable at the time of print, like function 
# but here (ans) is only veriable
print(ans)
print(ans(11))



add=lambda a1,b1: print(a1>b1)

print(add(10,29))










