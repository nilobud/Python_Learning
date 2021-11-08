num_1 = num_2 = res = 0
op = ""
while True:

  print("What is the first number?")
  num_1 = float(input())
  #print(num_1)

  print("What is the operation?")
  op = input()
  #print(op)

  print("What is the second number?")
  num_2 = float(input())

  if op == "+": 
    res = num_1 + num_2
    print("The result is ", res)
  elif op == "-":
    res = num_1 - num_2
    print("The result is ", res)
  elif op == "x" or op == "*":
    res = num_1 * num_2
    print("The result is ", res)
  elif op == "/":
    if num_2 == 0:
      print("Number 2 can't be 0, LOL")
    else:
      res = num_1 / num_2
      print("The result is ", res)
  else: 
    print("Operation is not defined")

  print("continue? q for quit.")
  q = input()
  if q == "q":
    break
  










