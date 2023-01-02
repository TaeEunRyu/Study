# 데이터 형식 이해 및 문자열 조작 방법

# Data Type

# String
# print("123" + "456");

# Integer
# print(123 + 345);

# Float
# print(3.141592);

# Bool
# print(True)
# print(False)

# 형식 오류와 형식 확인, 그리고 형 변환
# num_char = len(input("What is your Name?"));
# new_num_char = str(num_char);

# print("Your name has" + num_char + " characters.");
# print(type(num_char));


# Quiz 데이터 형식
# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

# singel_digits = int(two_digit_number[0]);
# two_digits = int(two_digit_number[1]);
# result = singel_digits + two_digits;

# print(str(singel_digits) + " + " + str(two_digits) + " = " + str(result));
# print(result);

# ###################################
# Write your code below this line 👇

# 파이썬의 수학 연산 : 괄호, 곱셈, 나눗셈, 덧셈, 뺄셈 순으로 수식 계산
# print(3 + 5);
# print(3 - 5);
# print(3 * 5);
# print(6 / 3);
# print(2 ** 3);

# Quize BMI 계산기
# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# height = float(height);
# weight = float(weight);

# height = int(height);

# bmi = height / (weight * weight);

# print(str(height) + " % " + "(" + str(weight) + " * " + str(weight) + ")" + " = " + str(bmi));
# print(int(bmi));

# Write your code below this line 👇

# 파이썬의 숫자 처리 및 F-String
# print(round(8 / 3 , 2));

# score = 0;
# score += 1;
# print(score);
# print(f"Your Score is {score}");

# Quiz 삶을 주로 표현 하기
# 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# day = (90 - int(age)) * 365;
# weeks = (90 - int(age)) * 52;
# months = (90 - int(age)) * 12;

# print(f"You have {day} days, {weeks} weeks, and {months} months left.");

# Write your code below this line 👇

# Quiz 팁 계산기
# If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcometo the tip calculator");
bill = input("What was the total bill? $");
tip = input("What percentage tip would you like to give? 10, 12, or 15? ");
personnel = input("How many people to split the bill? ");

bill = float(bill);
tip = float(int(tip) / 100) * bill;
personnel = int(personnel);

totalbill = (bill + tip) / personnel;

print(f"Each person should pay: ${round(totalbill,2)}");