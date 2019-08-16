num1=int(input(""))
num2=int(input(""))
for i in range(num1+1,num2-1):
	sum=0
	temp=i
	while temp>0:
		digit = temp % 10
		sum += digit**3
		temp //= 10
	if(i==sum):
		print("",i)
