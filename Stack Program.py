stack=[]
def push():
  element= input("Enter a element")
  stack.append(element)
  print(stack)
def pops():
  # element2=input("Enter a element")
  ele=stack.pop()
  print(ele,"is removed from the stack")
  print(stack)

while True:
  print("select the operation\n1.push\n2.pop\n3.quit")
  choice=int(input())
  if choice==1:
     push()
  elif choice==2:
       pops()
  elif choice==3:
       break
  else:
    print("enter the correct operation")
