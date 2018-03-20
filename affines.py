# Affines.py file by John Hughes 3/10/18

from ciphers import Cipher
from collections import OrderedDict
import logging

#logging.basicConfig(filename='affine.log', level = logging.DEBUG)


class Affine(Cipher):
    ''' Class: Affine: Child of Cipher
        Uses the Affine cipher to encrypt and decrypt a message.
        Will ask the user for a message and a code.
        Note: spaces are allowed and will be replaced with #.
    '''
    def __init__(self):
        
        self.ALPHABET = OrderedDict()
        self.encrypted_alphabet = OrderedDict()
         # Create the ALPHABET OrderedDict:
        self.ALPHABET[0] = 'A'
        self.ALPHABET[1] = 'B'
        self.ALPHABET[2] = 'C'
        self.ALPHABET[3] = 'D'
        self.ALPHABET[4] = 'E'
        self.ALPHABET[5] = 'F'
        self.ALPHABET[6] = 'G'
        self.ALPHABET[7] = 'H'
        self.ALPHABET[8] = 'I'
        self.ALPHABET[9] = 'J'
        self.ALPHABET[10] = 'K'
        self.ALPHABET[11] = 'L'
        self.ALPHABET[12] = 'M'
        self.ALPHABET[13] = 'N'
        self.ALPHABET[14] = 'O'
        self.ALPHABET[15] = 'P'
        self.ALPHABET[16] = 'Q'
        self.ALPHABET[17] = 'R'
        self.ALPHABET[18] = 'S'
        self.ALPHABET[19] = 'T'
        self.ALPHABET[20] = 'U'
        self.ALPHABET[21] = 'V'
        self.ALPHABET[22] = 'W'
        self.ALPHABET[23] = 'X'
        self.ALPHABET[24] = 'Y'
        self.ALPHABET[25] = 'Z'
        self.ALPHABET[26] = ' '

    def get_message(self):
        # Gets a message from the user and returns it.
        self.message = self.get_user_input("Please enter a message to encrypt.\n>>", True)
        logging.debug("The return of get_message is: {}.".format(self.message.upper()))
        return self.message.upper()
        
    def get_pad(self, message):
        # Gets the PAD from the user.
        while True:
            pad = self.get_user_input("Please enter a PAD to secure your message.\n"
                        "Note the PAD must be at least as long as your message.\n"
                        "If this is to decypt a message please enter that PAD:\n>>", True)
            try:
                if len(pad) >= len(message):
                    print("That is a secure PAD!")
                    break
            except InputError:
                print("Please enter a PAD at least as long as the message you are encrypting.")
        pad = pad.upper()
        logging.debug("The return of get_pad is: {}.".format(pad))
        return pad
        
    def get_encrypted_message(self):
        # Gets an encrypted message from the user and returns it.
        self.encrypted_message_str = self.get_user_input("Please enter an already encrypted message for decryption.\n>>", True)
        logging.debug("The return of get_encrypted_message is: {}.".format(self.encrypted_message_str.upper()))
        return self.encrypted_message_str.upper()
        
    def is_coprime(self, number1, number2):
        # Will return true if the two numbers provided are co-prime, otherwise returns false.
        logging.debug("In is_coprime:\nNumber1 is:{}\nNumber2 is: {}".format(number1, number2))
        factors_of_num1 = self.get_factors(number1)
        logging.debug("calling get_factors for num1")
        factors_of_num2 = self.get_factors(number2)
        logging.debug("calling get_factors for num2")
        for num1 in factors_of_num1:
            for num2 in factors_of_num2:
                if num1 and num2 == 1:
                    coprime = True
                elif num1 == num2:
                    coprime = False
        logging.debug("The return of is_coprime is: {}".format(coprime))
        return coprime
                    
    def get_factors(self, number):
        # Returns a list of numbers that are the whole factors of that number.
        factors = [num for num in range(1, number + 1) if not number % num]
        logging.debug("The return of get_factors is: {}".format(factors))
        return factors                    
    
    def get_key_code(self):
        # Walks user through generating a key code.
            # returns two keys as ints.
            # Generate a list of co-prime numbers for the user to choose from.
        alphabet_num = len(self.ALPHABET) + 1
        alpha_coprimes = []
        for num in range(1, alphabet_num):
            if self.is_coprime(num, alphabet_num):
                alpha_coprimes.append(num)
        del(alpha_coprimes[0])
        self.clear_scrn()
        print("Now you need to generate two key numbers to encrypt your message:")
        key1 = input("Please choose one of these numbers:\n {}\n>>".format(alpha_coprimes))
        key2 = input("Please enter a number:\n>>")
        logging.debug("The return of get_key_code is: {}".format(key1, key2))
        return int(key1), int(key2)
        
    def encrypt_alphabet(self, key_code):
        # Generates an encrypted alphabet based on the keycode, creates an OrderedDict
        key1, key2 = key_code
        alpha_len = len(self.ALPHABET)
        for alpha in range(1, alpha_len + 1):
            alpha_loc = ((key1 * alpha + key2) % alpha_len)
            self.encrypted_alphabet[alpha] = self.ALPHABET[alpha_loc]
        # for logging the encrypted alphabet:
        logging.debug("Encrypted Alphabet is:")
        for key, value in self.encrypted_alphabet.items():
            logging.debug("{} : {}".format(key, value))
        
    def encrypt_message(self, message, key_code):
        # Encrypts the message using the provided message and key code, returns a string.
        logging.debug("In encrypt_message:\nMessage is: {}\nKey_code is: {}\nCalling encrypt_alphabet\n".format(message, key_code))
        self.encrypt_alphabet(key_code)
        encrypted_message = []
        for letter in message:
            for key, alpha in self.ALPHABET.items():
                if letter == alpha:
                    encrypted_message.append(self.encrypted_alphabet[key])
        # Subbing # for spaces.
        space_index = 0
        for space_letter in encrypted_message:
            if space_letter == ' ':
                encrypted_message[space_index] = '#'
            space_index += 1
        logging.debug("The return of encrypt_message is: {}.".format(''.join(encrypted_message)))
        return ''.join(encrypted_message)
        
        
        
    def decrypt_message(self, encrypted_message, key_code):
        # Decrypts message using the provided encrypted message and key code.
        logging.debug("In decrypt_message:\nEncrypted_message is: {}\nKey_code is: {}\nCalling encrypt_alphabet".format(encrypted_message, key_code))
        self.encrypt_alphabet(key_code)
        # subs any # back to spaces.
        space_index = 0
        space_message = [letter for letter in encrypted_message]
        for space_letter in space_message:
            if space_letter == '#':
                space_message[space_index] = ' '
            space_index += 1
        encrypted_message = ''.join(space_message)
        decrypted_message = []
        for letter in encrypted_message:
            for key, alpha in self.encrypted_alphabet.items():
                if letter == alpha:
                    decrypted_message.append(self.ALPHABET[key])
        logging.debug("The return of decrypt_message is: {}.".format(''.join(decrypted_message)))
        return ''.join(decrypted_message)
    
    def encrypt_pad(self, message, pad):
        message_keys = []
        pad_keys = []
        pad_encrypt_keys = []
        pad_encrypted_message = []
        # Gets the number value of the letters in the message.
        for letter in message:
            for key, alpha in self.ALPHABET.items():
                if letter == alpha:
                    message_keys.append(key)
        # Gets the number value of the letters in the PAD.
        for letter in pad:
            for key, alpha in self.ALPHABET.items():
                if letter == alpha:
                    pad_keys.append(key)
        message_index = 0
        # Applies the PAD to the message.
        for message_key in message_keys:
            pad_key = pad_keys[message_index]
            pad_encrypt_keys.append((message_key + pad_key) % len(self.ALPHABET))
            message_index += 1
        for pad_encrypt_key in pad_encrypt_keys:
            for key, alpha in self.ALPHABET.items():
                if pad_encrypt_key == key:
                    pad_encrypted_message.append(self.ALPHABET[key])
                    break
        # subbing # for spaces.
        space_index = 0
        for space_letter in pad_encrypted_message:
            if space_letter == ' ':
                pad_encrypted_message[space_index] = '#'
            space_index += 1
        logging.debug("The return of encrypt_pad is: {}".format(pad_encrypted_message))
        return ''.join(pad_encrypted_message)

    def decrypt_pad(self, message, pad):
        message_keys = []
        pad_keys = []
        pad_encrypt_keys = []
        pad_encrypted_message = []
        # subs any # back to spaces.
        space_index = 0
        space_message = [letter for letter in message]
        for space_letter in space_message:
            if space_letter == '#':
                space_message[space_index] = ' '
            space_index += 1
        message = ''.join(space_message)
        # Gets the number value of the letters in the message.
        for letter in message:
            for key, alpha in self.ALPHABET.items():
                if letter == alpha:
                    message_keys.append(key)
        # Gets the number value of the letters in the PAD.
        for letter in pad:
            for key, alpha in self.ALPHABET.items():
                if letter == alpha:
                    pad_keys.append(key)
        message_index = 0
        # Applies the PAD to the message.
        for key in message_keys:
            pad_key = pad_keys[message_index]
            pad_encrypt_keys.append((key - pad_key) % len(self.ALPHABET))
            if pad_encrypt_keys[-1] < 0:
                pad_encrypt_keys += 27
            message_index += 1
        for pad_key in pad_encrypt_keys:
            for key, alpha in self.ALPHABET.items():
                if pad_key == key:
                    pad_encrypted_message.append(self.ALPHABET[key])
        logging.debug("The return of decryp_pad is: {}.".format(pad_encrypted_message))
        return ''.join(pad_encrypted_message)
