"""
Design a calculator that shows answers for some particular calculations wrong.
 45 * 3 = 555, 56 + 9 = 77, 56/6 = 4
Your program should take operator & the 2 nos. as input from the user & then return the result
"""

print("Welcome to F_calculator")
# faulty_calculator={"45 * 3 = 555, 56 + 9 = 77, 56/6 = 4"}
# calculation_type=input()
# print("Enter the number")
#  eyn=("num1")
# A=int(input())
#
#  print("Enter your operation")
# eyn=("operation")
#  operation=(input())
#
# print("Enter the second number")
#  eyn=("num2")
print("Enter the 1st number")
A=int(input())
print("Enter the 2nd number")
B=int(input())
print("Your choice?"'*,+,/')
C=input()




"""
SETTING UP THE FAULTY PART

"""
if A ==45 and B ==3 and C =='*':
    print("555")
elif A ==56 and B ==9 and C =='+':
    print("77")
elif A ==56 and B ==6 and C =='/':
    print("4")
elif  C =='*':
    mult =  A * B
    print(mult)
elif C =='+':
    add = A + B
    print(add)
elif C =='/':
    div =  A / B
    print(div)

# print("Enter the operation")
# operation=input()
# string=num1+operation+num276

# if num1== 45 and num2== 3:
#     print("Multiple is 555")
#
# if num1== 55 and num2== 9:
#     print("Addition is 77")
#
# if num1== 56 and num2== 6:
#     print("Division is 555")
# else:
#     print("The multiple is", int(num1)*int(num2))
#     print("The addition is", int(num1)+int(num2))
#     print("The division is", int(num1)/int(num2))
