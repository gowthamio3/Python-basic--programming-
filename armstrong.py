num=int(intput("Enter a number:"))
temp=num
sum=0
digits=len(str(num))
while temp>0:
  digits = temp%10
  sum+=digit**digits
  temp=temp//10
if sum==num:
  print(num,"is an armstrong numners")
else:
  print(num"is not an armstrong number")
