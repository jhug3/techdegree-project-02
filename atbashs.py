# Atbashes.py file by John Hughes 3/13/18

from ciphers import Cipher
from collections import OrderedDict
import logging

#logging.basicConfig(filename='atbash.log', level = logging.DEBUG)



class Atbash(Cipher):
    ''' Class: Atbash: Child of Cipher
        Uses the Atbash cipher to encrypt and decrypt a message.
        Will ask the user for a message to encrypt or decrypt.
        Note: spaces are allowed and will be replaced with #.
    '''
    def __init__(self):
        
        self.ALPHABET = OrderedDict()
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
        
        # Generates the encrypted alphabet, the reverse of ALPHABET
        #self.encrypted_alphabet = OrderedDict(reversed(list(self.ALPHABET.items())))
        self.encrypted_alphabet = OrderedDict()
        alpha_index = 0
        for item in reversed(self.ALPHABET.values()):
            logging.debug("Item is: {}".format(item))
            self.encrypted_alphabet[alpha_index] = item
            alpha_index +=1
        # Logging encrypted_alphabet
        logging.debug("Encrypted alphabet is:")
        for key, value in self.encrypted_alphabet.items():
            logging.debug("{} : {}".format(key, value))
        

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
        
    def encrypt_message(self, message):
        # Returns the message, encrypted with spaces replaced with #
        encrypted_message = []
        for letter in message:
            logging.debug("Letter in message is: {}".format(letter))
            for key, alpha in self.ALPHABET.items():
                logging.debug("key: {} alpha: {}".format(key, alpha))
                if letter == alpha:
                    encrypted_message.append(self.encrypted_alphabet[key])
                    break
            logging.debug("Encrypted message before space replace is: {}.".format(encrypted_message))
        # Subbing # for spaces.
        space_index = 0
        for space_letter in encrypted_message:
            if space_letter == ' ':
                encrypted_message[space_index] = '#'
            space_index += 1
        logging.debug("The return of encrypt_message is: {}.".format(encrypted_message))
        return ''.join(encrypted_message)
        
    def decrypt_message(self, message):
        # subs any # back to spaces.
        space_index = 0
        space_message = [letter for letter in message]
        for space_letter in space_message:
            if space_letter == '#':
                space_message[space_index] = ' '
            space_index += 1
        message = ''.join(space_message)
        decrypted_message = []
        for letter in message:
            for key, alpha in self.encrypted_alphabet.items():
                if letter == alpha:
                    decrypted_message.append(self.ALPHABET[key])
        logging.debug("The return of decrypted_message is: {}.".format(decrypted_message))
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
        logging.debug("The return of decrypt_pad is: {}".format(pad_encrypted_message))
        return ''.join(pad_encrypted_message)
