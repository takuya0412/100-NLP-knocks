from collections import Counter

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."


def tokenize(text):
    text = text.replace(',', '').replace('.', '').split(' ')
    print(text)
    counter = Counter(text)
    print(counter)
    return list(counter)

print(tokenize(sentence))
