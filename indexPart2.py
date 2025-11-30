dictionary = {
    "привет": "hello",
    "кот": "cat",
    "яблоко": "apple",
    "молоко": "milk"
}


while True:
    word = input("Введите слово на русском (или стоп): ").lower()
    if word == "стоп":
        break

    eng = input("Введите перевод: ").lower()
    dictionary[word] = eng

print(dictionary)

