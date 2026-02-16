n=int(input("Enter the numbers:"))
a=0
b=1
print("Fabonacci Series:")

for i in range(n):
  print(a,end=" ")
  c=a+b
  a=b
  b=c
