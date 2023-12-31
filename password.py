# program that encodes and decodes passwords
# Hemanshu Boppana

def encode(pwd):
    pwd = list(pwd)
    encoded_pwd_list = []
    for num in pwd:
        # first convert to int to add and the convert to str to append and then join together
        num = int(num)
        num += 3
        num = str(num)
        encoded_pwd_list.append(num)
    
    encoded_pwd = "".join(encoded_pwd_list)

    return encoded_pwd

# tongshan created decode method here
def decode(password):
    password = list(password)
    psw = []
    for i in password:
        i = int(i)
        i = i - 3
        i = str(i)
        psw.append(i)
        decode_psw = "".join(psw)
    return decode_psw



def main():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    repeat = True
    while repeat == True:
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
        elif option == 3:
            repeat = False
            print("Bye Bye!")

if __name__ == "__main__":
    main()
