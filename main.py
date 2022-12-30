import random

print("Welcome to python casino")
pc_choice = random.randint(0,50)
playing = True
while playing:
    user_choice = int(input("Choose number"))
    if user_choice == pc_choice:
        print("You win")
        playing = False
    elif user_choice > pc_choice:
        print("Lower")
    elif user_choice < pc_choice:
        print("Higher")






# distance = 0
# while distance < 20:
#     print("i'm running" , distance ,"km")
#     distance = distance + 1