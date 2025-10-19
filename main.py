# 从键盘输入一行字符
text = input()

# 初始化计数器
letters = 0
digits = 0
spaces = 0
others = 0

# 遍历每个字符并统计
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1

# 输出结果
print("英文字符:", letters)
print("数字:", digits)
print("空格:", spaces)
print("其他字符:", others)
