import random
fibsum = 0
fibsum = int(fibsum)
fiblist = []
x = 1
print("Input a number between 0-9")
while x == 1:
  try: 
    user = input()
    int(user)
    print("This is your first number: ", user)
  except:
    print("This is not a number between 0-9")
  else: 
    x = 0
random = random.randint(1,20)
print("This is your random number ", random)
print("Beginning Fibbonaci Sequence:")
fib1 = int(user)
fib2 = int(random)

for i in range(10):
  fibsum = fib1 + fib2
  fiblist.append(fibsum)
  fib1 = int(fib2)
  fib2 = int(fibsum)
print(fiblist)
  
