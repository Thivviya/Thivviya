
def add(num1,num2):
  c=num1+num2
  print("The result for additon is "+c)

def sub(num1,num2):
  c=num1-num2
  print("The result for subtraction is "+c)

def mul(num1,num2):
  c=num1*num2
  print("The result for multiplication is "+c)

def div(num1,num2):
  c=num1/num2
  print("The result for division is "+c)

num1=int(input("Enter a frst no. "))
num2=int(input("Enter a sec no. "))
print("The operations are  1.Add 2.Sub 3.Mul 4.Div ..Now,choose ur option")
num3=int(input(" "))
if num3=='1':
  add(num1,num2)
elif num3=='2':
  sub(num1,num2)
elif num3=='3':
  mul(num1*num2)
elif num3=='4':
  div(num1/num2)
else:
  print("Enter a valid option!!")


