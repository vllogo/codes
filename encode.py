with open("text.txt") as file:
    text = file.read()

code = "!"
for i in text:
    code += (chr(int(((bin(ord(i))[2:])[::-1]).replace('0', '2'), 3) ^ ord(code[-1])))

new_code = ""
for i in code:
    new_code += (chr(ord(i) ^ ord('S')))

with open("code.txt", "w") as file:
    file.write(new_code)
