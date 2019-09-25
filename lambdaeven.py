from array import*
arr=array('i',[])
n=int(input(" "))
for i in range(n):
	num=int(input(" "))
	arr.append(num)
evens=list(filter(lambda n1:n1%2==0,arr))
print(evens)
