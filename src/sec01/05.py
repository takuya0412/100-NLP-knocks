
def n_gram(n, text):
    text = list(text.replace(' ', ''))
    res = []
    max = len(text)
    cnt = 0
    while max-1 > cnt:
        res.append("".join(text[cnt:cnt+n]))
        cnt += 1

    return res

text = "I am an NLPer"
print(n_gram(2, text))
