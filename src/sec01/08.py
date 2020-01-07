import sys

def cipher(s):
    res = ""
    for i in s:
        if i.islower() and i.isalpha():
            res += convert(i)
        else:
            res += i
    return res


def convert(x):
    ascii_num = ord(x)
    res = chr(219 - ascii_num)
    return res


if __name__ == "__main__":
    args = sys.argv
    print(cipher(args[1]))
