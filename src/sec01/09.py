import sys
from random import randint
from math import floor


def typoglycemia(s):
    s = s.split(' ')
    changer = {}
    st_charge = ""
    ind = 0
    for i in s:
        if len(i)>4:
            # print(">4: {}".format(i))
            changer[i[0]+"{}"+i[-1]] = {'index': ind, 'num': len(i) - 2}
            st_charge +=i[1:-1]
        ind += 1
        st_charge_list = list(st_charge)
        # print(changer)
    for k, v in changer.items():
        gen_str, st_charge_list = get_random_string(v['num'], st_charge_list)
        new_key = k.format(gen_str)
        s[v['index']] = new_key

    return s


def get_random_string(n, li):
    res = ""
    for _ in range(n):
        max = len(li)-1
        res += li.pop(floor(randint(0, max)))
    return res, li


if __name__ == "__main__":
    args = sys.argv
    print(args[1])
    print(" ".join(typoglycemia(args[1])))
