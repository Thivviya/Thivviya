num=int(input(""))
num2=len(str(num))
sum=0
temp=num
while temp>0:
	digit = temp % 10
	sum += digit**num2
	temp //= 10
if(num==sum):
	print("Yes")
else:
	print("No")
