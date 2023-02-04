### DAY 5

## 5.1
# 리스트에서 평균 키 구하기 : for문 사용

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
height_sum = 0
for height in student_heights:
  height_sum += height

num_students = 0
for student in student_heights:
  num_students += 1

height_mean = round(height_sum / num_students, 2)
print(f'평균 : {height_mean}')


## 5.2
# 최대 점수 구하기 : for문 사용

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
maximum = 0
for score in student_scores:
    if maximum < score:
        maximum = score
print(f"최대 점수 : {maximum}")

## 5.3
# 1부터 100까지 짝수 더하기

# Write your code below this row 👇
sum = 0
for i in range(2,101,2):
  sum += i

print(sum)

## 5.4
# FizzBuzz
# 3의 배수 : Fizz, 5의 배수 : Buzz, 15의 배수 : FizzBuzz

# Write your code below this row 👇
for i in range(1,101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

## Final
# 문자, 숫자, 기호 개수에 따라 비밀번호 생성하기
# Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""
while (nr_letters > 0 or nr_symbols > 0 or nr_numbers > 0):
    s = random.choice([letters, numbers, symbols])
    if s == letters and nr_letters > 0:
        nr_letters -= 1
        password += random.choice(s)
    elif s == numbers and nr_numbers > 0:
        nr_numbers -= 1
        password += random.choice(s)
    elif s == symbols and nr_symbols > 0:
        nr_symbols -= 1
        password += random.choice(s)
    else:
        pass
print(password)

