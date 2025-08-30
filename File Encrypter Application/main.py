from cryptography.fernet import Fernet
import os

# Define the main menu for user choices
def main_menu():
    print("1 - Encrypt File")
    print("2 - Decrypt File")
    print("3 - Generate New Key")

# Define a function to display an error message with optional text
def error_message(text="space"):
    print(f"Do Not Enter {text} ...")

# Define a function to encrypt a file using a given key
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Define a function to decrypt a file using a given key
def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

# Main loop to repeatedly show the menu and handle user choices
while True:
    main_menu()

    # Loop to handle user input and validation of the choice
    while True:
        user_choice = input("Enter Your Choice: ")

        if not user_choice:
            error_message()
            continue
        elif not user_choice.isdigit():
            error_message(user_choice)
            continue
        else:
            user_choice = int(user_choice)

        if user_choice > 3:
            error_message(user_choice)
            continue
        else:
            break

    # Option 1: Encrypt a file
    if user_choice == 1:
        while True:
            key = input("Enter Your Key: ")

            if not key:
                error_message()
                continue
            try:
                Fernet(key)
            except:
                print("Key Is Invalid")
                continue
            else:
                break

        while True:
            file_path = input("Enter File Path: ")

            if not file_path:
                error_message()
                continue
            elif os.path.isfile(file_path) and os.path.dirname(file_path) == "":
                break
            else:
                print("The file is not in the directory.")
                continue

        encrypt_file(file_path, key)
        print("File Has Been Encrypted.")

    # Option 2: Decrypt a file
    elif user_choice == 2:
        while True:
            file_path = input("Enter File Path: ")

            if not file_path:
                error_message()
                continue
            elif os.path.isfile(file_path) and os.path.dirname(file_path) == "":
                break
            else:
                print("The file is not in the directory.")
                continue

        while True:
            key = input("Enter Your Key: ")

            if not key:
                error_message()
                continue
            try:
                fernet = Fernet(key)
                with open(file_path, "rb") as file:
                    fernet.decrypt(file.read())
            except:
                print("Key Is Invalid")
                continue
            else:
                break

        decrypt_file(file_path, key)
        print("File Has Been Decrypted.")

    # Option 3: Generate a new key
    elif user_choice == 3:
        key = Fernet.generate_key()
        print("Key is Generated.")

        user_input = input("Save Key in .txt File [y/s]: ")

        save_text = ["Y", "y", "YES", "yes", "Yes"]

        if user_input in save_text:
            with open("key.txt", "w") as file:
                file.write(key.decode("utf-8"))
            print("Key.txt File Saved.")
        else:
            continue
