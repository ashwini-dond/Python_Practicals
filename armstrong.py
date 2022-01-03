num=int(input("enter the number"))
 sum=0
num1=num
while(num1>0):
d=num1%10
num1=int(num/10)
sum=sum+d*d*d
if(num==sum):
  print("number is armstrong")
else:
  print("number is not armstrong")
