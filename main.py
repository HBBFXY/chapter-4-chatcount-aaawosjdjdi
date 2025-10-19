s = input()
a = 0
b = 0
c = 0
d = 0

for char in s:
    if char.isalpha():
        a += 1
    elif char.isdigit():
        b += 1
    elif char.isspace():
        c += 1
    else:
        d += 1

print("英文字符:", a)
print("数字:", b)
print("空格:", c)
print("其他字符:", d)
