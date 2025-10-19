s = input()
a = 0
b = 0
c = 0
d = 0

for i in s:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        a = a + 1
    elif i >= '0' and i <= '9':
        b = b + 1
    elif i == ' ':
        c = c + 1
    else:
        d = d + 1

print("英文字符:", a)
print("数字:", b)
print("空格:", c)
print("其他字符:", d)
