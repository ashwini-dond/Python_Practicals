a int(input("enter start limit"))
b int(input("enter end limit"))
for i in range(a,b+1):
n=i
s=0
while(n>0):
d=n%10
n=int(n/s)
s=s+(d*d*d)
print("armstrong number in interval")
if(s==i):
  print(i)
else
  break 
