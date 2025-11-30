dictionary = {
    "привет": "hello",
    "кот": "cat",
    "яблоко": "apple",
    "молоко": "milk"
}

word = input("Введите слово на русском: ").lower()


if word in dictionary:
    print("Перевод:", dictionary[word])
else:
    print("Такого слова нет в словаре ")

