# 1.輸入第一個數字  
# !重點:input()：接收輸入回傳字串，int()轉換整數，float()轉換浮點數
num1 = float(input("請輸入第一個數字: "))  

# 2.輸入運算符號
operator = input("請輸入運算符號 (+, -, *, /): ")

# 3.輸入第二個數字
num2 = float(input("請輸入第二個數字: ")) 

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
if result is not None:
  print("計算結果:", result)