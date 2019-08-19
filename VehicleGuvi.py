def auto():
  dist=150
  amt=dist*2
  print(name+'travelled a distance'+dist+'km and ur amt is '+amt+'.rs')

def taxi():
  dist=250
  amt=dist*5
  print(name+'travelled a distance'+dist+'km and ur amt is '+amt+'.rs')

def mini():
  dist=500
  amt=dist*20
  print(name+'travelled a distance'+dist+'km and ur amt is '+amt+'.rs')

def premium():
  dist=2500
  amt=dist*2
  print(name+'travelled a distance'+dist+'km and ur amt is '+amt+'.rs')

name=input("Enter ur name ")
src_place=input("Enter ur source place ")
dest_place=input("Enter ur destination place ")
print("The available vehicle are 1.Auto 2.Taxi 3.Mini 4.Premium ")
print("Select ur desired vehicle ")
select=int(input(""))
if select=='1':
  auto()
elif select=='2':
  taxi()
elif select=='3':
  mini()
elif select=='4':
  premium()
else:
  print("Enter valid option!!")
