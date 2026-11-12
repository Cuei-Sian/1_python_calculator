# 簡易計算機程式

# 加入while迴圈，讓使用者可以重複使用計算機，直到輸入n結束程式。
while True:
    # 加入try-except來處理輸入錯誤或錯誤，else區塊來處理運算，避免程式中斷。
    try:
      # 1.輸入第一個數字  
      # !重點:input()：接收輸入回傳字串，int()轉換整數，float()轉換浮點數
        num1 = float(input("請輸入第一個數字: "))  

        # 2.輸入運算符號
        operator = input("請輸入運算符號 (+, -, *, /): ")

        # 3.輸入第二個數字
        num2 = float(input("請輸入第二個數字: ")) 

    except ValueError:
        print("輸入錯誤: 請輸入有效的數字!")
        continue  # 如果輸入錯誤，跳過本次迴圈，重新開始。
        # print("輸入錯誤: 計算機結束!")
        # break  # 如果輸入錯誤，結束程式。

    else:
      # 4.根據運算符號進行計算  
      # !重點:= 是把資料放進變數， == 是判斷是否相等，if、elif、else 後面要加冒號 :，條件成立後的程式碼要縮排，通常是4個空格。
        if operator == "+":
          result = num1 + num2

        elif operator == "-":
          result = num1 - num2

        elif operator == "*":
          result = num1 * num2

        elif operator == "/": # !重點: 避免除以零的錯誤，先判斷除數是否為零
          if num2 == 0: 
            result = None
            print("錯誤: 除數不能為零")
          else:
            result = num1 / num2

        else:
          result = None
          print("輸入錯誤: 無效的運算符號")

        # 5.輸出結果
        if result is not None: # 只有當 result 不是 None 時，才顯示計算結果。
          print("計算結果:", result)

    # 加入巢狀while迴圈，讓使用者可以重複使用計算機，直到輸入n結束程式。
    while True:  
        # 0.詢問使用者是否要繼續使用計算機
        answer = input("是否要繼續使用計算機? (y/n): ")
        if answer == "n":
          break  #記得加上break，否則會無限迴圈下去。(內層while迴圈結束)
        elif answer == "y":
          break  # 如果使用者輸入y，繼續下一次迴圈。(內層while迴圈結束)
        else:
          print("輸入錯誤，請輸入 y 或 n！")
          continue  # 如果使用者輸入其他字元，結束程式。

    if answer == "n":
        break  # 如果使用者輸入n，結束程式。(外層while迴圈結束)

print("計算機結束，謝謝使用!")