text = input()

letters = 0
digits = 0
spaces = 0
others = 0

for i in text:
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
        letters += 1
    elif '0' <= i <= '9':
        digits += 1
    elif i == ' ':
        spaces += 1
    else:
        others += 1

print("英文字符:", letters)
print("数字:", digits)
print("空格:", spaces)
print("其他字符:", others)
