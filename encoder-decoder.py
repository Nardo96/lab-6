#Bernardo Rodriguez
def encode(data):
    #Takes in a string password (int only) and shifts each integer up by 3
    encoded = []
    for char in data:
        encoded.append(str(int(char)+3))
    return ''.join(encoded)
    
def decode(data):
    pass

def show_menu():
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    return input('Please enter your selection: ')

def main():
    while True:
        choice = int(show_menu())
        if choice == 1:
            password = input('Please enter a password to encode: ')
            encoded = encode(password)
            print(f'Your encoded password is: {encoded}')
        elif choice == 2:
            password = input('Please enter a password to decode: ')
            decoded = decode(password)
            print(f'Your decoded password is: {decoded}')
        else:
            return
    

if __name__ == '__main__':
    main()