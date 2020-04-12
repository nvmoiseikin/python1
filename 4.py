import re
eng_rus = {"one": "один", "two": "два", "three": "три", "four": "четыре"}


def trans(word):
    real_word = str(word[0]).lower()
    trans_word = eng_rus.get(real_word)
    if trans_word is not None:
        return eng_rus.get(real_word).title()
    return real_word


with open("4.in.txt", encoding="utf-8") as file_in:
    text = file_in.read()
    with open("4.out.txt", mode="wt", encoding="utf-8") as file_out:
        file_out.write(re.sub(r"\b\w*", trans, text))
