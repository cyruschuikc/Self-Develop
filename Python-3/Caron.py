def _init_():
  lang = "python-3.**"
  name = "Caron.py"
  version = "1.0.0"
  return lang+":/>"+name+":/>Ver`"+version
prog_shell = _init_()
print(prog_shell)

print("/*Presented by 'cyruschui1@replit.com'*/")
print("\nHello, user. Welcome to use Py3Calc (V1)!")
print("I'm Caron, the guide elf inside the program.")
print("I'll help you to calculate a formula.\n")

def get_formula():
  print("Please tell me your formula that need me to calculate.")
  formula = str(input(">>> "))
  return formula
fx = get_formula()

def calculation():
  global fx
  if "/0" in fx:
    return "Math Error: Division by zero."
  else:
    return eval(fx)
print("The answer is:", calculation())

contin_to_use = str(input("Continue?(Y/N)"))
while contin_to_use != "N":
  fx = get_formula()
  answer = calculation()
  print("The answer is:", answer)
  contin_to_use = str(input("Continue?(Y/N)"))
else:
  print("Okay, bye!\nThank-you for your using!")
  exit()
