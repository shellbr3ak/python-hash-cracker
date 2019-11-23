#!/usr/bin/env python3

## NOTE : This script doesn't work with python2, it's gonna throw a syntax error
## because of the formated strings. Happy Cracking :)
import hashlib
import sys
import argparse
import time

BLUE = "\033[34m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"
RESET = "\033[0;0m"
YELLOW = "\033[33m"

print(BLUE + """\n\n
       +------------------------------------------------+
       |                  Coded by : L                  |
       |                                                |
       | https://github.com/shellbr3ak?tab=repositories |
       +------------------------------------------------+
         ____  _          _ _ ____                 _    
        / ___|| |__   ___| | | __ ) _ __ ___  __ _| | __
        \___ \| '_ \ / _ \ | |  _ \| '__/ _ \/ _` | |/ /
         ___) | | | |  __/ | | |_) | | |  __/ (_| |   < 
        |____/|_| |_|\___|_|_|____/|_|  \___|\__,_|_|\_|
                   
                       offensive python
                       ----------------
                  
""" + RESET)


parser = argparse.ArgumentParser(description="Example : python3 hasher.py -m algo -f hashfile -w wordlist")

parser.add_argument("-m", dest="algorithm", help="The Hashing algorithm")
parser.add_argument("-f", dest="hashfile", help="The File Contains the hash")
parser.add_argument("-w", dest="wordlist", help="The dictionary file")

parsed_args = parser.parse_args()

def get_hash(password, algorithm):
    """ Allowed Alogrithms are md5 sha1 sha256 sha512 """
    hash_type = hashlib.new(algorithm)
    hash_type.update(password.encode())
    return hash_type.hexdigest()

try:
    
    algo = parsed_args.algorithm
    hashfile = parsed_args.hashfile
    wordlist = parsed_args.wordlist
    hpass = open(hashfile).read().strip()
    passwords = open(wordlist, encoding="latin1").read().splitlines()
    
    print(f"\nCracking Tha Hash " + YELLOW + f"{hpass}" + RESET)
    time.sleep(2)
    for password in passwords:
        #time.sleep(.2)
        #print(YELLOW + "[+]" + RESET + f" Trying password : {password}")
        if hpass == get_hash(password,algo):
            print(GREEN + f"Hash Cracked : {password}" + RESET)
            break
    else:
        print(RED + "Word Not Found!" + RESET)

except KeyboardInterrupt:
    print(RED + "You Stopped The Script" + RESET)
    pass
except TypeError:
    print(RED + parser.description + RESET)
    pass
