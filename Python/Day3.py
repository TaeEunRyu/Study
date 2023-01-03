# 흐름 제어와 논리 연산자

# if / else 및 조건 연산자를 통한 흐름 제어

# print("Welcom to the rollercoaster!");
# height = input("What is your height in cm? ");

# if height >= 120:
#     print("You Can ride the rollercoaster!")
# else:
#     print("Sorry, you have to frow taller before you can ride.")    
    
# Quiz 홀수 또는 짝수 모듈
# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# if number % 2 == 1:
#     print("This is an odd number.");
# else:
#     print("This is an even number.");

# Write your code below this line 👇

# 중첩 if 문과 elif 문
# print("Welcom to the rollercoaster!");
# height = input("What is your height in cm? ");

# if height >= 120:
#     print("You Can ride the rollercoaster!")
#     age = int(input("What is your age? "));
#     if age < 12:
#         print("Please pay $5");
#     elif age <= 18:    
#         print("Please pay $7");
#     else:
#         print("Please pay $12");        
# else:
#     print("Sorry, you have to frow taller before you can ride.")    
        
# Quiz BMI 2.0
# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# height = float(height);
# weight = float(weight);

# bmi = round(weight / height ** 2);

# if bmi >= 35:
#     print(f"Your BMI is {int(bmi)}, you are clinically obese.");
# elif bmi > 30:
#     print(f"Your BMI is {int(bmi)}, you are obese.");
# elif bmi > 25:
#     print(f"Your BMI is {int(bmi)}, you are slightly overweight.");
# elif bmi > 18.5:
#     print(f"Your BMI is {int(bmi)}, you have a normal weight.");
# else:
#     print(f"Your BMI is {int(bmi)}, you are underweight.");

# Write your code below this line 👇

# Quiz 윤년
# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# if year % 4 == 0: # 조건을 만족하면 윤년
#     if year % 100 == 0: # 조건을 만족하면 윤년이 아님    
#         if year % 400 == 0: # 조건을 만족하면 윤년
#             print("Leap year.");
#         else:
#             print("Not leap year.");
#     else:
#         print("Leap year.");
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print("Leap year.");                     
#     else:
#         print("Not leap year.");
# elif year % 400 == 0:
#     print("Leap year.");
# else:
#     print("Not leap year.");

#Write your code below this line 👇

# 다중 연속 if문
# print("Welcom to the rollercoaster!");
# height = input("What is your height in cm? ");

# bill = 0;

# if height >= 120:
#     print("You Can ride the rollercoaster!")
#     age = int(input("What is your age? "));
#     if age < 12:
#         bill = 5;
#         print("Please pay $5");
#     elif age <= 18:    
#         bill = 7;
#         print("Please pay $7");
#     else:
#         bill = 12;
#         print("Please pay $12");        
        
#     wants_photo = input("Do you want a photo taken? Y or N");
#     if wants_photo == "Y":
#         #Add $3 to their bill                
#         bill += 3;
        
#     print(f"Your final bill is {bill}");        
# else:
#     print("Sorry, you have to frow taller before you can ride.")    

# 논리 연산자
print("Welcom to the rollercoaster!");
height = input("What is your height in cm? ");

bill = 0;

if height >= 120:
    print("You Can ride the rollercoaster!")
    age = int(input("What is your age? "));
    if age < 12:
        bill = 5;
        print("Please pay $5");
    elif age <= 18:    
        bill = 7;
        print("Please pay $7");
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!");
    else:
        bill = 12;
        print("Please pay $12");        
        
    wants_photo = input("Do you want a photo taken? Y or N");
    if wants_photo == "Y":
        #Add $3 to their bill                
        bill += 3;
        
    print(f"Your final bill is {bill}");        
else:
    print("Sorry, you have to frow taller before you can ride.")    
    
# Quiz 사랑 계산기
# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# name1 = name1.lower();
# name2 = name2.lower();

# true_score = 0;
# love_score = 0;
# total_score = 0;

# true_score = name1.count("t");
# true_score += name1.count("r");
# true_score += name1.count("u");
# true_score += name1.count("e");

# true_score += name2.count("t");
# true_score += name2.count("r");
# true_score += name2.count("u");
# true_score += name2.count("e");
    
# love_score = name1.count("l");
# love_score += name1.count("o");
# love_score += name1.count("v");
# love_score += name1.count("e");

# love_score += name2.count("l");
# love_score += name2.count("o");
# love_score += name2.count("v");
# love_score += name2.count("e");
    
# total_score = int(str(true_score) + str(love_score));

# if total_score < 10 or total_score > 90:
#     print(f"Your score is {total_score}, you go together like coke and mentos.");
# elif total_score < 50 and total_score > 40:    
#     print(f"Your score is {total_score}, you are alright together.");
# else:
#     print(f"Your score is {total_score}.");

# Write your code below this line 👇