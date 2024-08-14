
def myfunction(n):
  return lambda n:n+10
  
ans=myfunction(3)

# print(ans)<---------------
# why (ans) veriables not content return value;

# here why it must to pass value to (ans) veriable at the time of print, like function 
# but here (ans) is only veriable
print(ans(11))
