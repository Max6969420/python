print('This is the 1st number')
num1 = input()
print('This is the 2nd number')
num2 = input()
try:
    print("The sum is:",
      int(num1) + int(num2))

except Exception as a:
    print(a)