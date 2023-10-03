import art
def add(n1,n2):
  return (n1+n2)
def sub(n1,n2):
  return(n1-n2)
def div(n1,n2):
  return(n1/n2)
def mul(n1,n2):
  return(n1*n2)
def calculator():
  ans=0
  dict_functions={"+":add,
                 "-":sub,
                 "/":div,
                 "*":mul
                 }
  print(art.logo)
  num1=float(input("Enter 1st number :"))
  for i in dict_functions:
    print(i)
  
  choice="yes"
  while choice=="yes":
    
    if choice=="no":
      break
    operator2=input("Enter the operation you wanna perform:")
    num2=float(input("Enter next number :"))
    function1=dict_functions[operator2]
    ans=function1(num1,num2)
    print(f"{num1} {operator2} {num2} = {ans}")
    
    choice=input("Do you wanna continue?:yes or no ?If you wanna start fresh then type fresh: ")
    choice=choice.lower()
    if choice=="yes":
      num1=ans
    if choice=="fresh":
      calculator()
calculator()    