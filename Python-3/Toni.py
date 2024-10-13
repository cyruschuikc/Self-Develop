### Toni.py (Number Picker)
## Shell: ~/Toni$
## presented by cyruschui1@replit.com
## Partner/Support: cyruschikc@GitHub

import random as fx_RD
def init(lan,name,ver):
  path = lan+":>/"+name+":>/Ver:"+ver
  return path
PB = init("Python-3. **","Toni.py", "1.1.0")

print(PB,"\nWelcome to use Toni.py (Number Picker)!\n")
print("I'm Toni, the guide elf inside the program.")
print("I'll help you to pick a number from a range of numbers.")

lucky_num = 0
temp1 = int(input("How many numbers you want to pick from? "))

nums = [0]*temp1
history = [0]*(temp1-1)

for i in range(0,len(nums)):
  nums[i] = i +1
print("Numbers in NumBox:")
print(nums)

pick_num = str(input("Pick a number? (Y/N)"))
if pick_num == "Y":
  lucky_num = fx_RD.choice(nums)
  temp2 = 0
  while lucky_num in history:
    lucky_num = fx_RD.choice(nums)
  if temp2 == 0:
    history[0] = lucky_num
    temp2 = temp2 + 1
    print("\nThe lucky number is:",lucky_num)
    print("\nHistory of numbers:")
    print(history)
  else:
    history[temp2] = lucky_num
    temp2 = temp2 + 1
    print("\nThe lucky number is:",lucky_num)
    print("\nHistory of numbers:")
    print(history)
else:
  print("Okay, bye!\nThank-you for your using!")
  exit()

contin_to_use = str(input("Continue?(Y/N)"))
while contin_to_use != "N":
  pick_num = str(input("Pick a number? (Y/N)"))
  if pick_num == "Y":
    lucky_num = fx_RD.choice(nums)
    while lucky_num in history:
      lucky_num = fx_RD.choice(nums)
    history[temp2] = lucky_num
    temp2 = temp2 + 1
    print("\nThe lucky number is:",lucky_num)
    print("\nHistory of numbers:")
    print(history)
    contin_to_use = str(input("Continue?(Y/N)"))
else:
  print("Okay, bye!\nThank-you for your using!")
  exit()
