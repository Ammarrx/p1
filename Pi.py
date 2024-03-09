#Date:26/2/2024
#Author:Ammar Sayed Mansour Mohamed
#id:20230561
print("welcome")
while True:
 try:
  pi = 0
  sign = 1
  n = int(input("enter number of terms: "))
  if n<=0:
   raise ValueError
  for i in range(1, n * 2, 2):
   pi += sign * (1 / i)
  
   sign *= -1
  pi *= 4 
  result=pi

  print(f"the estimated value of Pi using {n} terms is: {result}")
 except ValueError:
  print("enter a positive integer number")
