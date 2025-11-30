from googletrans import Translator

translator = Translator()

text = input("Введите слово или фразу: ")

result = translator.translate(text, src="ru", dest="en")

print("Перевод:", result.text)