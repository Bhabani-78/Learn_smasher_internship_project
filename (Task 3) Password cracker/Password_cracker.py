from urllib.request import hashlib
import colorama
from colorama import Fore,Style

colorama.init()
print(Fore.GREEN + Style.BRIGHT)
print()
print(r".______      ___           _______.     _______.____    __    ____  ______   .______       _______  ")
print (r"|   _  \    /   \         /       |    /       |\   \  /  \  /   / /  __  \  |   _  \     |       \ ")
print (r"|  |_)  |  /  ^  \       |   (----`   |   (----` \   \/    \/   / |  |  |  | |  |_)  |    |  .--.  |")
print(r"|   ___/  /  /_\  \       \   \        \   \      \            /  |  |  |  | |      /     |  |  |  |")
print(r"|  |     /  _____  \  .----)   |   .----)   |      \    /\    /   |  `--'  | |  |\  \----.|  '--'  |")
print(r"| _|    /__/     \__\ |_______/    |_______/        \__/  \__/     \______/  | _| `._____||_______/ ")
print(r"                                                                                                    ")
print(r"              ______ .______          ___       ______  __  ___  _______ .______                    ")
print(r"             /      ||   _  \        /   \     /      ||  |/  / |   ____||   _  \                   ")
print(r"            |  ,----'|  |_)  |      /  ^  \   |  ,----'|  '  /  |  |__   |  |_)  |                  ")
print(r"            |  |     |      /      /  /_\  \  |  |     |    <   |   __|  |      /                   ")
print(r"            |  `----.|  |\  \----./  _____  \ |  `----.|  .  \  |  |____ |  |\  \----.              ")
print(r"             \______|| _| `._____/__/     \__\ \______||__|\__\ |_______|| _| `._____|              ")
print()


while True:
    print()
    print ("Enter Type of Hash to be cracked (Select 3 to quit the script)!\n 1. SHA1 Hash \n 2. MD5 Hash \n 3. Quit Script")
    print() 
    k = input(">")

    if (k=="1"):
        passFound = False


        sha1hash = input("Please input the SH1 hash to crack.\n>")


        with open ("file.txt","r") as file:

            for guess in file:

                hashedGuess = hashlib.sha1(bytes(guess.strip(), 'utf-8')).hexdigest()


                if hashedGuess.upper() == sha1hash.upper():

                    print("The password is ", str(guess))
                    passFound=True
                    break
                elif hashedGuess != sha1hash:
                    print("Password guess ",str(guess)," does not match, trying next...")

        if (passFound==False):
            print("Password not in database, we'll get them next time.")

    elif (k=="2"):
        passFound = False
        md5hash = input("Please input the MD5 hash to crack.\n>")

        with open ("file.txt","r") as file:

            for guess in file:

                hashedGuess = hashlib.md5(bytes(guess.strip(), 'utf-8')).hexdigest()

                if hashedGuess.upper() == md5hash.upper():

                    print("The password is ", str(guess))
                    passFound=True
                    break
                elif hashedGuess != md5hash:
                    print("Password guess ",str(guess)," does not match, trying next...")

        if (passFound==False):
            print("Password not in database, we'll get them next time.")

    elif (k=="3"):
        quit()