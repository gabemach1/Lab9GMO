'''

This is Gabriel Machado's main.py file

'''



def encode(x):

    x = list(x)
    i = 0
    l = len(x)
    while i < len(x):
        if int(x[i]) < 7:
            x[i] = int(x[i]) + 3
            i += 1
        else:
            x[i] = int(x[i]) - 7
            i += 1
    y = ''
    i = 0
    while i < l:
        y += str(x[i])
        i += 1

    return y

def decode(x):
    x = str(x)
    y = ""
    for num in x:
        y += (str((int(num)-3+10) % 10))
    return y

def main():

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = input("Please enter an option: ")

        if option == "1":
            original = str(input("Please enter your password to encode: "))
            passwordEnc = encode(original)
            print("Your password has been encoded and stored!\n")
        if option == "2":
            passwordDec = decode(passwordEnc)
            print("The encoded password is", passwordEnc, "and the original password is", passwordDec, "\n")
        if option == "3":
            break




if __name__ == "__main__":
    main()


