### Creator: CHUI, Ka Chun (HK)
import random as RD
print("Welcome to use p3-NumPicker@CyrusChui1!")
def _init_():
  temp1 = int(input("Minimum number:"))
  temp2 = int(input("Maximum number:"))
  array1, array2 = [0]*temp2, [0]*(temp2-temp1)
  for i in range (0,temp2):
    array1[i] = i+1
  return temp1, temp2, array1, array2
min, max, NumBox, MS = _init_()
# 'MS' refer to 'memeories'
temp = -1
print("No. in NumBox:\n",NumBox)
LN = RD.choice(NumBox) # Lucky Number
def check():
  global LN, temp
  while LN in MS:
    LN = RD.choice(NumBox)    
  if LN not in MS:
    temp = temp+1
    MS[temp] = LN
  else:
    MS.append(LN) 
check()
print("The lucky number is:",LN)
Continue = input("Press ‘Enter’ to continue extraction or ‘0’ to exit. ")
while Continue != "0":
  LN = RD.choice(NumBox)
  check()
  print("The lucky number is:",LN)
  Continue = input("Press ‘Enter’ to continue extraction or ‘0’ to exit. ")
else:
  print("Thx for your using.")
  exit()
