from replit import clear
import art
print(art.logo)
repeat = True
def add(a,b):
  return a + b
def subtract(c, d):
  return c-d
def multiply(e, f):
  return e * f
def divide(h, i):
  return h/i

while repeat == True:
  num1 = int(input("What is the first number?:\n"))
  op= input(''' *\n /\n +\n -\n Pick an operation \n''')
  num2 = int(input("What is the second number?:\n"))
  
  if op == "+":
    answer = add(num1,num2)
    print(f"{num1} {op} {num2} = {answer} ")
  elif op == "-":
    answer = subtract(num1,num2)
    print(f"{num1} {op} {num2} = {answer} ")
  elif op == "*":
    answer = multiply(num1,num2)
    print(f"{num1} {op} {num2} = {answer} ")
  elif op == "/":
    answer = divide(num1,num2)
    print(f"{num1} {op} {num2} = {answer} ")
    
  decide = (input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation and 'x' to cancel.\n")).lower()
  
  if decide == 'y':
    num1 = answer
    op= input(''' *\n /\n +\n -\n Pick an operation \n''')
    num2 = int(input("What is the second number?:\n"))
    if op == "+":
      answer = add(num1,num2)
      print(f"{num1} {op} {num2} = {answer} ")
    elif op == "-":
      answer = subtract(num1,num2)
      print(f"{num1} {op} {num2} = {answer} ")
    elif op == "*":
      answer = multiply(num1,num2)
      print(f"{num1} {op} {num2} = {answer} ")
    elif op == "/":
      answer = divide(num1,num2)
      print(f"{num1} {op} {num2} = {answer} ")
    print("Thank you, Goodbye!")
    break
  elif decide == 'n':
    repeat = True
    clear()
  else:
    break
