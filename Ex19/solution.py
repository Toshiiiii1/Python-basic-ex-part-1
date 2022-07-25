def checkIs(strr):
    if (strr.startswith("Is")):
        return strr
    else:
        return "Is"+strr

if __name__ == "__main__":
    strr = input()
    print(checkIs(strr))