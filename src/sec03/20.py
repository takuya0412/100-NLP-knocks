import json

def read_file(title):
    decoder = json.JSONDecoder()
    res = {}
    with open('../resource/jawiki-country.json') as f:
        line = f.readline()
        while line:
            tmp = decoder.raw_decode(line)
            if tmp[0]['title'] == title:
                return tmp[0]['text']
            line = f.readline()
    print(res)





print(read_file('イギリス'))

