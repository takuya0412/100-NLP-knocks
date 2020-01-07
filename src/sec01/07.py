import sys
def info(x, y, z):
    return "{}時の{}は{}".format(str(x), str(y), str(z))

if __name__ == "__main__":
    args = sys.argv
    print(info(args[1], args[2], args[3]))
