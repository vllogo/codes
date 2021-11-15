def find_ternary(num):
    quotient = num / 3
    remainder = num % 3
    if quotient == 0:
        return ""
    else:
        return find_ternary(int(quotient)) + str(int(remainder))


with open("code.txt") as file:
    code = file.read()

new_text = ""
for i in code:
    new_text += chr(ord(i) ^ ord('S'))

text = ""
j = 0
for i in new_text[1:]:
    text += (chr(int(((find_ternary(ord(i) ^ ord(new_text[j])))[::-1]).replace('2', '0'), 2)))
    j += 1

print(text)

with open("text.txt", "w") as file:
    file.write(text)
