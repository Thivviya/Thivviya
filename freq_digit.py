num=int(input(""))
digit=int(input(""))
count=0
while num>0:
    rem=num%10
    if rem==digit:
        count=count+1
    num=num//10
print(count)
