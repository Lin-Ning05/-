n = int(input())
words = ["money", "cash", "urgent", "account", "transfer", "heritage", "prize"]
answer = []

for _ in range(n):
    s = input().lower() #轉小寫用來比較
    count = 0

    for word in words:
        start = 0
        while True:
            temp = s.find(word, start) #從第start開始找在第幾個
            if temp == -1: #沒找到
                break

            left_ok = (temp == 0) or (not s[temp - 1].isalpha()) #看前一個是不是英文字
            right = temp + len(word)
            right_ok = (right == len(s)) or (not s[right].isalpha()) #後一個

            if left_ok and right_ok:
                count += 1

            start = temp + 1

    answer.append(str(count))

print(",".join(answer))