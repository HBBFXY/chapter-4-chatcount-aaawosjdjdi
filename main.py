# Input a line of characters from keyboard
text = input()

# Initialize counters
letters = 0
digits = 0
spaces = 0
others = 0

# Count each character
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1

# Output results
print("英文字符:", letters)
print("数字:", digits)
print("空格:", spaces)
print("其他字符:", others)
