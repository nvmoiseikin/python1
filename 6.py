# Уже есть функция title, которая все делает
def my_title(word):
    #print(ord("a"), ord("z"), ord("A") - ord("a"))
    filter_word = "".join(list(filter(lambda x: ord(x) >= ord("a") and ord(x) <= ord("z"), word)))
    # Можно выводить filter_word весто просто ошибки
    if word != filter_word:
        return "<!error!>"
    first_let = ord(filter_word[0])
    first_let += ord("A") - ord("a")
    return chr(first_let) + word[1:]


def my_title_text(text):
    words = text.split(" ")
    return (" ").join(map(my_title, words))


print(my_title("xbcd"))
print(my_title_text("xbcd ajAsdLid sdjh+=dsj !dsldflfv kdfof-- oofdso -----"))
