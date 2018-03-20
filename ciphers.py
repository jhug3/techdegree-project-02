import os

class Cipher():
    '''Class Cipher: Parent Class
        Sets up a menu and handels user input and output for included
            Ciphers.
        The menu only gives the user the choices of ciphers, the choice to
            encrypt or decrypt and any other options is handled in each cipher
            class.
    '''
    def __init__(self):
        # Displays the menu
        self.clear_scrn()
        self.main_menu()
        
    def clear_scrn(self):
        # Standard clear screen method/function
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def get_user_input(self, user_message, clear=False):
        # Takes in a message for the user and gets user input and returns what the user inputs.
        if clear == True:
            self.clear_scrn()
            user_input = input(user_message)
            return user_input
        else:
            user_input = input(user_message)
            return user_input
    
    def five_block(self, message):
        # Displays message in a five character block format.
        #  Removes any spaces from message
        message = ''.join(message.split(' '))
        word_list = [letter for letter in message]
        block_list = []
        # If message is longer than 5 letters, splits it into 5 character blocks.
        if len(word_list) > 5:
            index = 0
            for letter in word_list:
                if index == 0:
                    string_word = ''.join(word_list[index:(index+5)])
                    block_list.append(string_word)
                    block_list.append(' ')
                    index += 1
                elif (index % 5) == 0:
                    string_word = ''.join(word_list[index:(index+5)])
                    block_list.append(string_word)
                    block_list.append(' ')
                    index += 1
                index += 1
            joined_string = ''.join(block_list)
            nothing = input("The message in 5 letter block format is: {}."
                            "\nHit Enter to return to the Main Menu.".format(joined_string.rstrip()))
            self.main_menu()
        else:
            nothing = input("The message in 5 letter block format is: {}."
                            "\nHit Enter to return to the Main Menu.".format(message))
            self.main_menu()
            
    def main_menu(self):
        # Method to display the main menu.
        self.clear_scrn()
        print("______Main Menu______\n\n"
                "Please choose a Cipher:\n"
                "1) Keyword\n"
                "2) Affine\n"
                "3) Atbash\n")
        menu_choice = self.get_user_input("Please enter a number 1-3 or a Cipher name:\n>>")
        if menu_choice == '1' or menu_choice.upper() == 'KEYWORD':
            from keywords import Keyword
            keyword = Keyword()
            self.clear_scrn()
            print("___Keyword Menu:___\n"
                    "Please choose an option:\n"
                    "1) ENCRYPT a message\n"
                    "2) ENCRYPT a message using a PAD\n"
                    "3) DECRYPT a message\n"
                    "4) DECRYPT a message using a PAD\n")
            keyword_choice = self.get_user_input("Please enter a number 1-4 or 'Encrypt', 'EncryptPAD', 'Decrypt' or 'DecryptPAD': \n>>")
            if keyword_choice == '1' or keyword_choice.upper() == 'ENCRYPT':
                keyword_messgae = keyword.get_message()
                keyword_keyword = keyword.get_keyword()
                keyword_encrypted_message = keyword.encrypt_message(keyword_messgae, keyword_keyword)
                print("Your encrypted message is:\n{}.\n".format(keyword_encrypted_message))
                keyword_block = input("Do you want to display your message in 5 letter block format? (Y/N)")
                if keyword_block.upper() == 'Y':
                   self.five_block(keyword_encrypted_message)
                nothing = input("\n\nHit enter to return to the Main Menu.")
                self.main_menu()
            elif keyword_choice == '2' or keyword_choice.upper() == 'ENCRYPTPAD':
                keyword_messgae = keyword.get_message()
                keyword_keyword = keyword.get_keyword()
                keyword_encrypted_message = keyword.encrypt_message(keyword_messgae, keyword_keyword)
                keyword_pad = keyword.get_pad(keyword_encrypted_message)
                keyword_pad_message = keyword.encrypt_pad(keyword_encrypted_message, keyword_pad)
                print("Your encrypted message with a PAD is:\n{}".format(keyword_pad_message))
                keyword_block = input("Do you want to display your message in 5 letter block format? (Y/N)")
                if keyword_block.upper() == 'Y':
                   self.five_block(keyword_pad_message)
                nothing = input("\n\nHit enter to return to the Main Menu.")
                self.main_menu()
            elif keyword_choice == '3' or keyword_choice.upper() == 'DECRYPT':
                keyword_encrypted_message = keyword.get_encrypted_message()
                keyword_keyword = keyword.get_keyword()
                keyword_decrypted_message = keyword.decrypt_message(keyword_encrypted_message, keyword_keyword)
                print("Your Decrypted message is:\n{}.\n".format(keyword_decrypted_message))
                nothing = input("\n\nHit enter to return to the Main Menu.")
                self.main_menu()
            elif keyword_choice == '4' or keyword_choice.upper() == 'DECRYPTPAD':
                keyword_encrypted_message_pad = keyword.get_encrypted_message()
                keyword_keyword = keyword.get_keyword()
                keyword_pad = keyword.get_pad(keyword_encrypted_message_pad)
                keyword_encrypted_message = keyword.decrypt_pad(keyword_encrypted_message_pad, keyword_pad)
                keyword_decrypted_message = keyword.decrypt_message(keyword_encrypted_message, keyword_keyword)
                print("Your Decrypted message is:\n{}.\n".format(keyword_decrypted_message))
                nothing = input("\n\nHit enter to return to the Main Menu.")
                self.main_menu()
            else:
                nothing = input("Not a valid entry. Returning to Main Menu. Hit enter to continue.")
                self.main_menu()
        elif menu_choice == '2' or menu_choice.upper() == 'AFFINE':
            from affines import Affine
            affine = Affine()
            self.clear_scrn()
            print("___Affine Menu:___\n"
                    "Please choose an option:\n"
                    "1) ENCRYPT a message\n"
                    "2) ENCRYPT a message using a PAD\n"
                    "3) DECRYPT a message\n"
                    "4) DECRYPT a message using a PAD\n")
            affine_choice = self.get_user_input("Please enter a nubmer 1-4 or 'Encrypt', 'EncryptPAD', 'Decrypt' or 'DecryptPAD': \n>>")
            if affine_choice == '1' or affine_choice.upper() == 'ENCRYPT':
                affine_message = affine.get_message()
                affine_keycode = affine.get_key_code()
                affine_encrypted_message = affine.encrypt_message(affine_message, affine_keycode)
                print("Your encyrpted message is:\n{}".format(affine_encrypted_message))
                keyword_block = input("Do you want to display your message in 5 letter block format? (Y/N)")
                if keyword_block.upper() == 'Y':
                   self.five_block(affine_encrypted_message)
                nothing = input("\n\nHit enter to return to the Main Menu.")
                self.main_menu()
            elif affine_choice == '2' or affine_choice.upper() == 'ENCRYPTPAD':
                affine_message = affine.get_message()
                affine_keycode = affine.get_key_code()
                affine_encrypted_message = affine.encrypt_message(affine_message, affine_keycode)
                affine_pad = affine.get_pad(affine_encrypted_message)
                affine_pad_message = affine.encrypt_pad(affine_encrypted_message, affine_pad)
                print("Your encrypted message with a PAD is:\n{}".format(affine_pad_message))
                keyword_block = input("Do you want to display your message in 5 letter block format? (Y/N)")
                if keyword_block.upper() == 'Y':
                   self.five_block(affine_pad_message)
                nothing = input("\n\nHit enter to return to the Main Menu.")
                self.main_menu()
            elif affine_choice == '3' or affine_choice.upper() == 'DECRYPT':
                affine_encrypted_message = affine.get_encrypted_message()
                affine_keycode = affine.get_key_code()
                affine_decrypted_message = affine.decrypt_message(affine_encrypted_message, affine_keycode)
                print("Your decrypted message is:\n{}.".format(affine_decrypted_message))
                nothing = input("\n\nHit enter to return to the Main Menu.")
                self.main_menu()
            elif affine_choice == '4' or affine_choice.upper() == 'DECRYPTPAD':
                affine_encrypted_message_pad = affine.get_encrypted_message()
                affine_keycode = affine.get_key_code()
                affine_pad = affine.get_pad(affine_encrypted_message_pad)
                affine_encrypted_message = affine.decrypt_pad(affine_encrypted_message_pad, affine_pad)
                affine_decrypted_message = affine.decrypt_message(affine_encrypted_message, affine_keycode)
                print("Your decrypted message is:\n{}.".format(affine_decrypted_message))
                nothing = input("\n\nHit enter to return to the Main Menu.")
                self.main_menu()
            else:
                nothing = input("Not a valid entry. Returning to Main Menu. Hit enter to continue.")
                self.main_menu()
        elif menu_choice == '3' or menu_choice.upper() == 'ATBASH':
            from atbashs import Atbash
            atbash = Atbash()
            self.clear_scrn()
            print("___Atbash Menu:___\n"
                    "Please choose an option:\n"
                    "1) ENCRYPT a message\n"
                    "2) ENCRYPT a message using a PAD\n"
                    "3) DECRYPT a message\n"
                    "4) DECRYPT a message using a PAD\n")
            atbash_choice = self.get_user_input("Please enter a number 1-4 or 'Encrypt', 'EncryptPAD', 'Decrypt' or 'DecryptPAD': \n>>")
            if atbash_choice == '1' or atbash_choice.upper() == 'ENCRYPT':
                atbash_message = atbash.get_message()
                atbash_encrypted_message = atbash.encrypt_message(atbash_message)
                print("Your encrypted message is:\n{}.\n".format(atbash_encrypted_message))
                keyword_block = input("Do you want to display your message in 5 letter block format? (Y/N)")
                if keyword_block.upper() == 'Y':
                   self.five_block(atbash_encrypted_message)
                nothing = input("\n\nHit enter to return to the Main Menu.")
                self.main_menu()
            elif atbash_choice == '2' or atbash_choice.upper() == 'ENCRYPTPAD':
                atbash_message = atbash.get_message()
                atbash_encrypted_message = atbash.encrypt_message(atbash_message)
                atbash_pad = atbash.get_pad(atbash_encrypted_message)
                atbash_pad_message = atbash.encrypt_pad(atbash_encrypted_message, atbash_pad)
                print("Your encrypted message is:\n{}.\n".format(atbash_pad_message))
                keyword_block = input("Do you want to display your message in 5 letter block format? (Y/N)")
                if keyword_block.upper() == 'Y':
                   self.five_block(atbash_pad_message)
                nothing = input("\n\nHit enter to return to the Main Menu.")
                self.main_menu()
            elif atbash_choice == '3' or atbash_choice.upper() == 'DECYPT':
                atbash_encrypted_message = atbash.get_encrypted_message()
                atbash_decrypted_message = atbash.decrypt_message(atbash_encrypted_message)
                print("Your decrypted message is:\n{}.\n".format(atbash_decrypted_message))
                nothing = input("\n\nHit enter to return to the Main Menu.")
                self.main_menu()
            elif atbash_choice == '4' or atbash_choice.upper() == 'DECYPTPAD':
                atbash_encrypted_message_pad = atbash.get_encrypted_message()
                atbash_pad = atbash.get_pad(atbash_encrypted_message_pad)
                atbash_encrypted_message = atbash.decrypt_pad(atbash_encrypted_message_pad, atbash_pad)
                atbash_decrypted_message = atbash.decrypt_message(atbash_encrypted_message)
                print("Your decrypted message is:\n{}.\n".format(atbash_decrypted_message))
                nothing = input("\n\nHit enter to return to the Main Menu.")
                self.main_menu()
            else:
                nothing = input("Not a valid entry. Returning to Main Menu. Hit enter to continue.")
                self.main_menu()
        else:
            nothing = input("Not a valid entry. Returning to Main Menu. Hit enter to continue.")
            self.main_menu()
             
