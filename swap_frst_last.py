num=int(input(" "))
frst=num
while(frst>=10):
    frst=frst//10
    
last=num%10
print("Before swap" ,frst,last)
frst,last=last,frst
print("After swap" , frst,last)
