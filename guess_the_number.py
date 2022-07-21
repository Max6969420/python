# n = 18
# number_of_guesses = 1
# print("Number of guesses is limited to 9 times:")
# # while(number_of_guesses<=9):
# while(True):
#     number=int(input("Guess the number:\n"))
#     if number<18:
#         print("Please guess a lesser number:\n")
#         # number=int(print())
#     if number>18:
#         print("Please guess a greater number:\n")
#     else:
#         print("You won!!!")
#         print(number_of_guesses( "Number of guesses you took :)" ))
#     break
#     print(9-number_of_guesses,"No. of guesses left")
#     number_of_guesses=number_of_guesses + 1
# import random
# from mimetypes import guess_type

# num = 22
# guess = None
# while guess !=num:
#     guess =input("Guess a number between 1-30: ")
#     # guess = int(input())
#     if guess<=num:
#         print("Higher it a bit")
#         input(guess)
#     if guess>=num:
#         print("Lower it a bit")
#     else:
#         print("Sorry you lost:(","Better luck next time")
# print("Made with love by Max")
run = True
while run:
    user_input = int(input('Enter a Number between 1 - 10: '))
    if user_input == 7:
        print('You won!')
        # run = False
        break
    # else:
    #     print('try again!')
    #     continue
    elif user_input<= 7:
        print('Higher it a bit')
    elif user_input>= 7:
        print('Lower it a bit')
