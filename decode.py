def find_ternary(num):
    quotient = num / 3
    remainder = num % 3
    if quotient == 0:
        return ""
    else:
        return find_ternary(int(quotient)) + str(int(remainder))


with open("code.txt") as file:
    code = file.read()

text = ""
for i in code:
    text += (chr(int(((find_ternary(ord(i)))[::-1]).replace('2', '0'), 2)))

print(text)

with open("text.txt", "w") as file:
    file.write(text)
