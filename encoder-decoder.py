def encode(data):
    #Takes in a string password (int only) and shifts each integer up by 3
    encoded = []
    for char in data:
        encoded.append(str(int(char)+3))
    return ''.join(encoded)

def main():
    pass

if __name__ == '__main__':
    main()