#Bernardo Rodriguez
def encode(data):
    #Takes in a string password (int only) and shifts each integer up by 3
    encoded = []
    for char in data:
        encoded.append(str(int(char)+3))
    return ''.join(encoded)
    
def decode(data):

    decoded_password = ""
    for digit in data:
        # Cast digit to an int and subtract 3. % 10 to get the first digit
        digit = (int(digit) - 3) % 10
        # Add each digit to a new string
        decoded_password += str(digit)
    return decoded_password

def show_menu():
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    return input('Please enter your selection: ')

def main():

    choice = 0
    while choice != 3:      # the loop has to end as soon as the user inputs 3
        choice = int(show_menu())       # we don't need the int as we already defined choice as an integer = '0'
        if choice == 1:
            password = input('Please enter a password to encode: ')
            encoded = encode(password)
            print(f'Your encoded password is: {encoded}')       # i don't we have to show the encoded password
        elif choice == 2:
            password = input('Please enter a password to decode: ')
            decoded = decode(password)
            print(f'Your decoded password is: {decoded}')
        else:
            return
    

if __name__ == '__main__':
    main()