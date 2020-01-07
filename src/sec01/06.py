
one = 'paraparaparadise'
two = 'paragraph'

def n_gram(n, text):
    text = list(text.replace(' ', ''))
    res = []
    max = len(text)
    cnt = 0
    while max-1 > cnt:
        res.append("".join(text[cnt:cnt+n]))
        cnt += 1

    return res


def require(one, two):
    set_one = set(n_gram(2, one))
    set_two = set(n_gram(2, two))
    union = set_one | set_two
    difference = set_one - set_two
    print("和集合: {}".format(union))
    print("差集合: {}".format(difference))
    print("seを含むか: {}".format("se" in union))


require(one, two)
