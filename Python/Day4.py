# 무작위화 및 파이썬 리스트

# Random 모듈
# import random
# import my_module

# random_interger = random.randint(1, 10);
# print(random_interger);

# print(my_module.pi);

# 0.000000000 ~ 0.9999999999
# random_float = random.random();
# print(random_float);

# 0.00000000 ~ 4.9999999999
# print(random_float * 5);

# Quiz Coin
# import random

# random_side = random.randint(0, 1);
# if random_side == 1:
#     print("Heads");
# else:
#     print("Tails");    

# 오프셋 이해 및 리스트에 항목 추가

# states_of_america = ["Delaware", "Pennsylvania"];
# print(states_of_america[0]);

# states_of_america[1] = "Pencilvania"
# print(states_of_america[1]);

# states_of_america.append("RTE");
# print(states_of_america[2]);

# 금융가 룰렛
# Import the random module here
# import random

# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# randomint = random.randint(0, 4);
# print(f"{names[randomint]} is going to buy the meal today!");

#Write your code below this line 👇

# IndexError 및 중첩 리스트 활용
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"];
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen =[fruits, vegetables];
# print(dirty_dozen);

# Quiz 보물 지도
# 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# first = int(position[0]) - 1;
# second = int(position[1]) - 1;

# if first >= 0 and first <= 2:
#     if second >= 0 and second <= 2:        
#         map[second][first] = "X";

# Write your code above this row 👆31

# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

# Quiz 가위바위보
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_image = [rock,paper, scissors];

user_choice = int(input("What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"));
if user_choice >= 3 or user_choice < 0:
    print("You typedan invalid number,you lose!");

print(game_image[user_choice]);

computer_choice= random.randint(0, 2);
print(game_image[computer_choice]);