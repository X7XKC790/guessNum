# 猜數字
import random

answerNum = random.randint(1, 100)
for i in range(1, 7):
    guess = input("請在6次內猜出數字：")
    if guess == "" or not guess.isdigit():
        break
    elif int(guess) == answerNum:
        print("恭喜！猜對啦^_^ ")
        quit()
    elif int(guess) > answerNum:
        print("快猜到了~ 猜'低'些試試")
    elif int(guess) < answerNum:
        print("接近答案嘍!! 猜'高'些試試")
print("\n正確答案是：" + str(answerNum))
input()
