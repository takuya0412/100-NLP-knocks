import re


def extract_category_line(path):
    with open(path, 'r') as f:
        text = f.readline()
        all_text = ""
        while text:
            all_text += text
            text = f.readline()

    ptn_a = re.compile(r"Category")




