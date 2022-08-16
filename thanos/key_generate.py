""" Built-in module """
import os
import re
import sys
# External modules #
from argon2 import PasswordHasher
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.aead import AESCCM


def print_err(msg: str) -> print:
    """
    Displays error message via stderr.

    :param msg:  The error message to be displayed.
    :return:  Displays formatted error message.
    """
    return print(f'\n* [ERROR] {msg} *\n', file=sys.stderr)


def get_secret() -> str:
    """
    Prompts user for password input to implement cryptographic scheme.

    :return:  Validated user input.
    """
    # Loop until proper input is provided #
    while True:
        # Prompt user for password to implement cryptographic keys #
        secret = input('Enter password for encryption scheme: ')
        # If password syntax validation fails #
        if not re.search(r'^[a-zA-Z\d_!+$@&(]{6,30}', secret):
            print_err('Improper input detected, try again with minimum of 6 letters, numbers,'
                      ' and _!+$@&(special characters)')
            continue

        return secret


def main():
    """
    Prompts for password to create cryptographic key set saved to file.

    :return:  Nothing
    """
    # Prompt user for password to implement key scheme #
    password = get_secret()

    # Initialize argon5 hashing algo #
    hash_algo = PasswordHasher()
    # Hash input password #
    hash_pass = hash_algo.hash(password)

    # Generate Fernet key #
    fern_key = Fernet.generate_key()
    # Encrypt input password with Fernet key #
    crypt_pass = Fernet(fern_key).encrypt(password.encode())

    # Generate AESCCM key/nonce #
    aesccm_key = AESCCM.generate_key(bit_length=256)
    nonce = os.urandom(13)

    try:
        # Open key file in append bytes mode #
        with open('thanos_keys.key', 'ab') as key_file:
            # Write results in random order to obfuscate #
            key_file.write(crypt_pass + b'\n')
            key_file.write(hash_pass.encode() + b'\n')
            key_file.write(nonce + b'\n')
            key_file.write(fern_key + b'\n')
            key_file.write(aesccm_key + b'\n')

    # If error occurs during file operation #
    except (IOError, OSError, UnicodeError) as file_err:
        print_err(f'Error occurred writing keys to key file: {file_err}')
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main()
