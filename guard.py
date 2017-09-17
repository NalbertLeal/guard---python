from os import path, listdir, exit
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import re
from exceptions import *

class Guard():
    def __inid__(self, root_path='', key='1010101010101010'):
        self.root_path = root_path
        self.key = self.make_key_16_multiple(key)
        self.aes_obj = AES.new(key, AES.)

        self.all_files_paths = []
        self.queue = []

    def find_contents(self):
        self.queue.append(self.root_path)
        to_continue = True
        while to_continue:
            if len(self.queue) == 0:
                to_continue = False
                continue
            dirparth_name = self.queue.pop(0)
            contents = listdir(p)
            for content in contents:
                if self.is_folder(dirparth_name + '/' +content):
                    self.queue.append(dirparth_name + '/' +content)
                else:
                    self.all_files_paths.append(dirparth_name + '/' +content)

    def is_folder(self, dirname):
        return os.path.isdir(dirname)

    def make_key_16_multiple(self, file_string):
        mod_16 = len(file_string)
        if mod_16 == 16:
            return file_string
        if mod_16 > 16:
            return file_string[0:16]
        else:
            file_mod_16 = file_string
            while mod_16 != 16:
                file_mod_16 += '1'
                mod_16 += 1
            return file_mod_16

    def make_msg_16_multiple(self, file_string):
        mod_16 = len(file_string) % 16
        if mod_16 == 0:
            return file_string
        else:
            file_mod_16 = file_string
            while mod_16 != 16:
                file_mod_16 += '.'
                mod_16 += 1
            return file_mod_16

    def encrypt_all_files(self):
        file_sha_validator = open('sha_validator.dat')
        file_sha_validator_string = file_sha_validator.read()
        for file_path in self.all_files_paths:

            file_to_encrypt = open(file_path)
            file_string = file_to_encrypt.read()

            sha_validator = SHA256.new('abc').hexdigest()
            if len(re.findall(sha_validator, file_sha_validator)) == 1:
                # if is true, the file wasn't modified
                file_to_encrypt.close()
                continue
            else:
                file_string = make_msg_16_multiple(file_string)

                file_to_encrypt.seek(0)
                file_to_encrypt.write( self.aes_obj.encrypt(file_string) ) # put all the content encripted into the file
                file_to_encrypt.truncate()

                # write to sha file validator the new sha
                file_sha_validator.write(' ' + sha_validator + ' ')

                file_to_encrypt.close()
        file_sha_validator.close()

    def decrypt_all_files(self):
        file_sha_validator = open('sha_validator.dat')
        file_sha_validator_string = file_sha_validator.read()
        for file_path in self.all_files_paths:

            file_to_decrypt = open(file_path)
            file_string = file_to_encrypt.read()

            sha_validator = SHA256.new('abc').hexdigest()
            if len(re.findall(sha_validator, file_sha_validator)) == 1:

                file_to_decrypt.seek(0)
                file_to_decrypt.write( self.aes_obj.decrypt(file_string) ) # put all the content encripted into the file
                file_to_decrypt.truncate()

                file_to_decrypt.close()
            else:
                file_to_decrypt.close()
                continue
        file_sha_validator.close()

    def run_encrypt(self):
        if not self.is_folder(self.root_path):
            raise Root_folder_not_directory()
            os.exit(1)

        self.find_contents()
        self.encrypt_all_files()

    def run_decrypt(self):
        if not self.is_folder(self.root_path):
            raise Root_folder_not_directory()
            os.exit(1)

        self.find_contents()
        self.decript_all_files()
