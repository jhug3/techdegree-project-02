# Keywords.py file by John Hughes 3/9/18

from ciphers import Cipher
from collections import OrderedDict
import logging

#logging.basicConfig(filename='keyword.log', level = logging.DEBUG)

class Keyword(Cipher):
    ''' Class: Keyword: Child of Cipher
        Uses the Keyword cipher to encrypt or decrypt a message.
        Will ask user for a message and a keyword.
        If a keyword is not given a default one will be used.
        Note: spaces are allowed and will be replaced with #.
    '''
    def __init__(self):
        self.ALPHABET = OrderedDict()
        self.encrypted_alphabet = OrderedDict()
        self.keyword_list = []
        
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
        
    def get_keyword(self):
        # Get the keyword from the user, if empty will use default.
        self.keyword = self.get_user_input("Please enter a keyword, hit enter to use the default keyword.\n>>")
        if self.keyword == '':
            self.keyword = 'KRYPTOFISH'
        # Removes any duplicate letters from the entered keyword
        for letter in self.keyword:
            if letter not in self.keyword_list:
                self.keyword_list.append(letter)
        self.keyword = ''.join(self.keyword_list)
        # Removes any spaces
        self.keyword = ''.join(self.keyword.split(' '))
        self.keyword = self.keyword.upper()
        logging.debug("The return of get_keyword is: {}.".format(self.keyword))
        return self.keyword
        
    def get_message(self):
        # Get the message to encrypt from the user and put it into self.message_list
        self.message = self.get_user_input("Please enter a message to encrypt.\n>>", True)
        self.message = self.message.upper()
        logging.debug("The return of get_message is: {}.".format(self.message))
        return self.message
        
    def get_pad(self, message):
        # Gets the PAD from the user.
        while True:
            pad = self.get_user_input("Please enter a PAD to secure your message.\n"
                        "Note the PAD must be at least as long as your message.\n"
                        "If this is to decypt a message please enter that PAD:\n>>", True)
            if len(pad) >= len(message):
                print("That is a secure PAD!")
                break
            else:
                nothing = input("Please enter a PAD at least as long as the message you are encrypting.\n"
                                "Hit ENTER to continue.")
        pad = pad.upper()
        logging.debug("The return of get_pad is: {}.".format(pad))
        return pad
        
    def get_encrypted_message(self):
        # Get the encrypted message to encrypt, must have already encrypted a message.
        self.encrypted_message = self.get_user_input("Please enter an already encrypted message for decryption.\n>>", True)
        self.encrypted_message = self.encrypted_message.upper()
        logging.debug("The return of get_encrypted_message is: {}.".format(self.get_encrypted_message))
        return self.encrypted_message
        
    def encrypt_message(self, message, keyword):
        # Encrypts the message using the inputed message and keyword.
        encrypted_message = []
        # Create the encrypted alphabet from the keyword:
        index = 0
        for letter in keyword:
            if letter not in self.encrypted_alphabet:
                self.encrypted_alphabet[index] = letter
                index += 1
        for alpha_letter in self.ALPHABET.values():
            if alpha_letter not in self.keyword:
                self.encrypted_alphabet[index] = alpha_letter
                index += 1
        # Print out encrypted alphabet to the debug log:
        logging.debug("The encrypted alphabet is:\n")
        for key, value in self.encrypted_alphabet.items():
            logging.debug("{} : {}".format(key, value))
        # Create the encrypted message:
        for message_letter in message:
            for alpha_key, alpha_letter in self.ALPHABET.items():
                if message_letter == alpha_letter:
                    encrypted_message.append(self.encrypted_alphabet[alpha_key])
        logging.debug("Encrypted message befor subbing spaces: {}.".format(encrypted_message))
        # Subbing # for spaces.
        space_index = 0
        for space_letter in encrypted_message:
            if space_letter == ' ':
                encrypted_message[space_index] = '#'
            space_index += 1 
        logging.debug("The return of encrypt_message (after subbing spaces) is: {}.".format(encrypted_message))
        return ''.join(encrypted_message)
        
    def decrypt_message(self, encrypted_message, keyword):
        # Decrypts the message using the inputed encrypted message and keyword.
        logging.debug("In start of decrypt_message:\nEncrypted_message is:{}\nKeyword is:{}.".format(encrypted_message, keyword))
        decrypted_message = []
        # subs any # back to spaces.
        space_index = 0
        space_message = [letter for letter in encrypted_message]
        for space_letter in space_message:
            if space_letter == '#':
                space_message[space_index] = ' '
            space_index += 1
        encrypted_message = ''.join(space_message)
        logging.debug("Encrypted_message after subbing # back to space is: {}.".format(encrypted_message))
        index = 0
        # Create the encrypted alphabet from the keyword:
        for letter in keyword:
            if letter not in self.encrypted_alphabet:
                self.encrypted_alphabet[index] = letter
                index += 1
        for alpha_letter in self.ALPHABET.values():
            if alpha_letter not in keyword:
                self.encrypted_alphabet[index] = alpha_letter
                index += 1
        # Printing the encrypted alphabet for the debugger:
        logging.debug("The encrypted alphabet in decrypt_message is:\n")
        for key, value in self.encrypted_alphabet.items():
            logging.debug("{} : {}".format(key, value))
        # Decrypt the message
        for letter in encrypted_message:
            for alpha_key, alpha_letter in self.encrypted_alphabet.items():
                if letter == alpha_letter:
                    decrypted_message.append(self.ALPHABET[alpha_key])
        logging.debug("The return of decrypt_message is: {}.".format(decrypted_message))
        return ''.join(decrypted_message)
    
    def encrypt_pad(self, message, pad):
        logging.debug("In incrypt_pad:\nMessage is: {}\nPad is: {}".format(message, pad))
        message_keys = []
        pad_keys = []
        pad_encrypt_keys = []
        pad_encrypted_message = []
        # Gets the number value of the letters in the message.
        # Accounts for any # substituted for spaces.
        for letter in message:
            if letter == '#':
                letter = ' '
            for key, alpha in self.ALPHABET.items():
                if letter == alpha:
                    message_keys.append(key)
                    break
        logging.debug("The number value of the letters in message is: {}.".format(message_keys))
        # Gets the number value of the letters in the PAD.
        for letter in pad:
            for key, alpha in self.ALPHABET.items():
                if letter == alpha:
                    pad_keys.append(key)
        logging.debug("The number value of the letters in the PAD is: {}.".format(pad_keys))
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
        logging.debug("Message with PAD applied before spaces are subbed is: {}.".format(pad_encrypted_message))
         # Subbing # for spaces.
        space_index = 0
        for space_letter in pad_encrypted_message:
            if space_letter == ' ':
                pad_encrypted_message[space_index] = '#'
            space_index += 1
        logging.debug("Message at end of encrypt_pad (after spaces are subbed) is: {}\n".format(pad_encrypted_message))
        return ''.join(pad_encrypted_message)

    def decrypt_pad(self, message, pad):
        logging.debug("In decrypt_pad:\nMessage is:{}\nPad is:{}".format(message, pad))
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
        logging.debug("Message after subbing # back to spaces is: {}.".format(message))
        # Gets the number value of the letters in the message.
        for letter in message:
            for key, alpha in self.ALPHABET.items():
                if letter == alpha:
                    message_keys.append(key)
        logging.debug("The number value of the letters in message is: {}".format(message_keys))
        # Gets the number value of the letters in the PAD.
        for letter in pad:
            for key, alpha in self.ALPHABET.items():
                if letter == alpha:
                    pad_keys.append(key)
        logging.debug("The number values of the letters in PAD is: {}".format(pad_keys))
        message_index = 0
        # Applies the PAD to the message.
        for key in message_keys:
            pad_key = pad_keys[message_index]
            pad_encrypt_keys.append((key - pad_key) % len(self.ALPHABET))
            if pad_encrypt_keys[-1] < 0:
                pad_encrypt_keys += len(self.ALPHABET)
            message_index += 1
        for pad_key in pad_encrypt_keys:
            for key, alpha in self.ALPHABET.items():
                if pad_key == key:
                    pad_encrypted_message.append(self.ALPHABET[key])
        logging.debug("The return of decrypt_pad is: {}.".format(pad_encrypted_message))
        return ''.join(pad_encrypted_message)
