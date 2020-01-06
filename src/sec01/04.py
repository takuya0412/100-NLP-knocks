text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

first = [1, 5, 6, 7, 8, 9, 15, 16, 19]

def create_list(text):
    text = text.replace(',', '').replace('.', '').split(' ')
    res = {}
    for i in range(len(text)):
        if i+1 in first:
            key = text[i][0]
        else:
            key = text[i][:2]
        res[key] = i+1

    return res

print(create_list(text))
