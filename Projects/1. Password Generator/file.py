import random

CharList = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd',
    'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
    'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l',
    'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
    'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
    'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
    'Y', 'y', 'Z', 'z', '0', '1', '2',
    '3', '4', '5', '6', '7', '8', '9'
]

PW = ''

Tick = input("De cate caractere vrei sa fie parola? : ")

PW_List = random.choices(CharList, k = int(Tick) - 1)
PW_List.append("@")
random.shuffle(PW_List)

for x in PW_List:
    PW += x

print(PW)