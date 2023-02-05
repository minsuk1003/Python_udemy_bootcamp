### Hangman

# 1. 랜덤으로 단어 생성
# 2. 단어의 알파벳 개수만큼 밑줄 생셩
# 3. 알파벳 중 하나를 입력
# 4-1. 해당 단어에 입력한 알파벳이 존재하면 알파벳 위치 공지
# 4-2. 존재하지 않으면 위치 공지하지 않음
# 5-1. 제한된 횟수 내에 단어의 모든 알파벳을 고르거나, 단어를 맞추면 게임 성공
# 5-2. 제한된 횟수 내에 맞추지 못하면 게임 실패

from hangman_words import word_list
from hangman_art import stages, logo
print(logo)

import random
# 랜덤으로 단어 생성
chosen_word = random.choice(word_list)
print(f"Word : {chosen_word}")

display = []
# 정답 단어의 알파벳 개수만큼 밑줄 생성
for i in range(len(chosen_word)):
    display.append("_")

# 단어 맞추기
# 밑줄이 없을 때까지 맞추기
lives = 6
while True:
    guess = input("Guess a letter : ").lower()
    # 정답 단어와 입력 문자 비교
    checked = False
    for letter in set(chosen_word):
        if letter == guess:
            checked = True
            print("Correct!")
            break

    # 입력 문자가 정답 단어에 포함되면 밑줄에 적용
    if checked == True:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = chosen_word[i]

    # 포함이 안되면 수명 감소 후 다시 입력하라고 출력
    else:
        lives -= 1
        print("no letter..")

    print(f"{' '.join(display)}")

    # 다 맞췄을 경우 게임 종료
    if "_" not in display:
        print("You win!")
        break

    # 수명이 다 했을 경우 게임 종료
    if lives == 0:
        print("You lose")
        break

    # 남은 수명 출력
    for live in range(7):
        if lives == live:
            print(stages[6-live])

    print(f"{lives} turns left.")