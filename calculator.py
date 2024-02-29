first_number=int(input("Enter your first Number:"))
second_number=int(input("Enter your second Number:"))
o=input("Enter your operator:")
if(o=='+'):
  print("Sum of two number is:",first_number + second_number)
elif(o=='-'):
  print("Subtraction of two number is:",first_number - second_number)
elif(o=='*'):
  print("Multiplication of two number is:",first_number * second_number)
elif(o=='/'):
  print("Division of two number is:",first_number / second_number)
else:
  print("Invalid operator")