# 猜數字
import random

def guess_number_game():
    answer_num = random.randint(1, 100)
    max_attempts = 6

    print("歡迎來到猜數字遊戲！")
    print(f"你有 {max_attempts} 次機會來猜一個 1 到 100 之間的數字。")

    for attempt in range(1, max_attempts + 1):
        guess = input(f"第 {attempt} 次猜測：請輸入你的數字（或按 Enter 退出）：")

        if guess == "":
            print("遊戲結束。")
            break

        if not guess.isdigit():
            print("請輸入一個有效的整數！")
            continue

        guess = int(guess)

        if guess == answer_num:
            print("恭喜！猜對啦^_^ ")
            break
        elif guess > answer_num:
            print("快猜到了~ 猜'低'些試試")
        else:
            print("接近答案嘍!! 猜'高'些試試")

    else:  # 如果沒有提前結束迴圈，則執行這裡的代碼
        print(f"\n正確答案是：{answer_num}")

# 開始遊戲
if __name__ == "__main__":
    guess_number_game()
