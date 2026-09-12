from enforce_rules import is_valid
age: int = int(input("Enter your age: "))
if is_valid(age, {"min": 18}):
  print("You're an adult.")
else:
  print("You're a kid.")
