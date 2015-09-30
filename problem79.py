# problem79.py
# Project Euler
# Nicolas Hahn

# list of keys -> passcode string
# at each iteration through list, 
def passcodeDerivation(keys):
    answer = ''
    while len(keys) > 0:
        firsts = []
        rests = []
        for key in keys:
            # split first digits, rest of the key into two lists
            f, r = key[0], key[1:]
            if f not in firsts:
                firsts += f
            rests += r
        for f in firsts:
            # if f has never been seen except as the first digit of a key
            # it must be the next one in the passcode
            if f not in rests:
                newkeys = []
                # take out digit we just found from all keys
                for key in keys:
                    newkeys.append(key.replace(f,''))
                # remove empty keys
                keys = [k for k in newkeys if k != '']
                answer += f
                break
    return answer

# filename -> list of keys
def loadKeys(keyFile):
    keys = []
    with open(keyFile,'r') as f:
        for line in f:
            keys.append(line.replace('\n',''))
    return keys

def main():
    keys = loadKeys('problem79keylog.txt')
    # correct answer = 73162890
    print(passcodeDerivation(keys))

if __name__ == "__main__":
    main()
