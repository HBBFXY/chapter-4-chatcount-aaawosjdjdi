s = input()
a, b, c, d = 0, 0, 0, 0

for i in s:
    if i.isalpha():
        a += 1
    elif i.isdigit():
        b += 1
    elif i == ' ':
        c += 1
    else:
        d += 1

print("英文字符:", a)
print("数字:", b)
print("空格:", c)
print("其他字符:", d)
