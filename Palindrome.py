num1=int(input(""))
temp=num1
rev = 0
while num1 > 0 :
    rem = num1 %10
    rev = (rev *10) + rem
    num1 = num1 //10

if temp==rev :
	print("Yes")
else:
	print("No")
