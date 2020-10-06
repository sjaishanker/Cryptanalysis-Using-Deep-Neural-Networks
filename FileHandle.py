from Des import DES_encrypt
import os

def textToBits(text, encoding='utf-8', errors='surrogatepass'):
    '''takes text as input and returns bits'''
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def textFromBits(bits, encoding='utf-8', errors='surrogatepass'):
    '''takes bits as input and returns text'''
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def writeToFile(filename, message):
    '''write message to given file location'''
    if os.path.exists(filename):
        append_write = 'a'
    else:
        append_write = 'w'
    f = open(filename, append_write)
    f.write(message)
    f.close()


def readFromFile(file_location):
    ''' Takes in file location as input and returns list of 8 character slices'''
    batches = []
    with open(file_location, "r") as f:
        counter = 1
        batch = ""
        while True:
            byte = f.read(1)
            if not byte:
                if counter == 8 or counter == 0:
                    break
                else:
                    for x in range(7 - counter):
                        batch += " "
                    break
            else:
                if counter == 8:
                    batch += byte
                    counter = 1
                    batches.append(batch)
                    batch = ""
                else:
                    batch += byte
                    counter += 1
    return batches



def decToBin(x):
    """Converts Decimal to Binary"""
    return int(bin(x)[2:])


def fileLength(fname):
    """Returns Length of file"""
    i = -1
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def makeDataset(key, input_file):
    '''makes dataset from given files and key'''
    batches = readFromFile(input_file)
    plain_text = []
    cipher_text = []
    for x in range(len(batches)):
        bits = textToBits(batches[x])
        temp = [ord(c) for c in batches[x]]
        plain_text.append(temp)
        encrypted = DES_encrypt(bits,key)
        temp = []
        for y in range(len(encrypted)):
            if encrypted[y] == '0':
                temp.append(0)
            else:
                temp.append(1)
        cipher_text.append(temp)
    return plain_text, cipher_text
