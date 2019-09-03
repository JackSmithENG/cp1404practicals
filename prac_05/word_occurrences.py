text = input("Text: ")
text_dict = {}
words = text.split()
for word in words:
    if word in text_dict:
        text_dict[word] += 1
    else:
        text_dict[word] = 1

words = list(text_dict.keys())
words.sort()

maximum_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, maximum_length, text_dict[word]))