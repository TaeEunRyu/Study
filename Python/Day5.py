# 파이썬 반복문

# 파이썬 리스트로 for 반복문 사용
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

# Quiz 평균 높이
# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# total = 0

# for height in student_heights:
#     total += int(height)

# average = total / len(student_heights)
# print(round(average))

# Write your code below this row 👇

# Quiz 높은 점수
# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

# higt_score = 0
# for score in student_scores:
#     if score > higt_score:
#         higt_score = score        

# print(f"The highest score in the class is: {higt_score}")
# Write your code below this row 👇

# for 반복문과 range() 함수
# for Loop with Range
# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number

# print(total)    

# Quiz 짝수 더하기
# Write your code below this row 👇
# total = 0;

# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number

# print(total)        

# Quiz FizzBuzz
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)        

# Quiz 비밀번호 생성기
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# empty = None

# for x in range(nr_letters + 1):
#     random_index = random.randint(0, len(letters))
#     empty = letters[random_index]
#     password += empty

# for y in range(nr_symbols + 1):
#     random_index = random.randint(0, len(numbers))
#     empty = numbers[random_index]
#     password += empty
    
# for z in range(nr_numbers + 1):
#     random_index = random.randint(0, len(symbols))
#     empty = symbols[random_index]
#     password += empty   
    
# print(f"Here is your password : {password}")    

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password2 = ""
empty2 = None

password_count = nr_letters + nr_symbols + nr_numbers
while len(password2) < password_count:
    random_index = random.randint(0, 2)
    if random_index == 0:
        if nr_letters != 0:
           random_index = random.randint(0, len(letters) - 1)
           empty2 = letters[random_index]
           password2 += empty2
           nr_letters -= 1
        else:           
            continue
    elif random_index == 1:     
        if nr_symbols != 0:
            random_index = random.randint(0, len(numbers) - 1)
            empty2 = numbers[random_index]
            password2 += empty2
            nr_symbols -= 1
        else:           
            continue
    elif random_index == 2:
        if nr_numbers != 0:
            random_index = random.randint(0, len(symbols) - 1)
            empty2 = symbols[random_index]
            password2 += empty2
            nr_numbers -= 1
        else:           
            continue
        
print(f"Here is your password : {password2}")