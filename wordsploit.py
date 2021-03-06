import platform
import sys
import time
import random
import hashlib
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# - Programme par: Keany Vy KHUN
# - Sous Licence : MIT
# - Projet: WordSploit
# - Description: Programme d'attaque par force brute amélioré
# - Status: Non fonctionnel

def selenium():
    global driver
    global chrome_options
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
    driver.set_window_size(1024, 650)
    webdriver.ChromeOptions().add_argument("--disable-popup-blocking")
    webdriver.ChromeOptions().add_argument("--disable-extensions")

print('\033[31m' + '''
 __      __                .____________      .__         .__  __
/  \    /  \___________  __| _/   _____/_____ |  |   ____ |__|/  |_
\   \/\/   /  _ \_  __ \/ __ |\_____  \ ____ \|  |  /  _ \|  \   __\ \
\n \        (  <_> )  | \/ /_/ |/        \  |_> >  |_(  <_> )  ||  |
  \__/\  / \____/|__|  \____ /_______  /   __/|____/\____/|__||__|
       \/                   \/       \/|__|

    --- Développé par Keany Vy KHUN ---
''' + '\033[0m')

def prevent():
    print('\033[33m' + 'Ordinateur:', platform.platform())
    print('Nom:', platform.node())
    print('Processeur:', platform.processor())

def main():
    methode = input('\033[0m'+"""\n
1 - Attaque par force brute
2 - Attaque par dicionnaire
3 - Déchiffrement de Hash
4 - Quitter

Veuillez entrer un nombre : """)

    if methode == "1":
        method_1()
    elif methode == "2":
        method_2()
    elif methode == "3":
        method_3()
    elif methode == "4":
        method_4()
    else:
        erreur()

def method_1():
    selenium()
    global driver
    target = input("\nEntrez l'url du site : ")
    driver.get(target)
    global username
    username = input("\nEntrez le nom d'utilisateur : ")
    brute_force()

def brute_force():
    global driver
    global username
    time.sleep(2)
    driver.find_element_by_xpath('//*[@type="text"]').send_keys(username)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@type="password"]').send_keys("test", Keys.ENTER)
    time.sleep(2)
    close_chrome()

def method_2():
    print('method 2')

def method_3():
    menu_decode()

def menu_decode():
    global encodage
    global name_encodage
    encodage = input("""\n
1 - MD5
2 - SHA1
3 - SHA224
4 - SHA256
5 - SHA384
6 - SHA512

Veuillez choisir un encodage : """)

    if encodage == "1":
        name_encodage = "md5"
        menu_decode_options()
    elif encodage == "2":
        name_encodage = "sha1"
        menu_decode_options()
    elif encodage == "3":
        name_encodage = "sha224"
        menu_decode_options()
    elif encodage == "4":
        name_encodage = "sha256"
        menu_decode_options()
    elif encodage == "5":
        name_encodage = "sha384"
        menu_decode_options()
    elif encodage == "6":
        name_encodage = "sha512"
        menu_decode_options()
    else:
        erreur()

def call_hash_md5():
    global md5_hash
    global options_decode
    md5_hash = input("\nEntrez le hash en "+ name_encodage +" : ")
    dictionnaire()

    if options_decode == "1":
        md5_minuscules('', 1)
    elif options_decode == "2":
        md5_majuscules('', 1)
    elif options_decode == "3":
        md5_chiffres('', 1)
    elif options_decode == "4":
        md5_min_maj('', 1)
    elif options_decode == "5":
        md5_min_chif('', 1)
    elif options_decode == "6":
        md5_all('', 1)
    else:
        erreur()

def menu_decode_options():
    global options_decode
    options_decode = input("""\n
1 - Minuscules (Rapide)
2 - Majuscules (Rapide)
3 - Chiffres (Rapide)
4 - Minuscules + Majuscules (Moyen)
5 - Minuscules + Chiffres (Moyen)
6 - Minuscules + Majuscules + Chiffres (Tout tester)

Veuillez choisir une option à tester : """)
    if options_decode.isdigit():
        length_decode()
        call_hash_md5()
    else:
        erreur()

def dictionnaire():
    global minuscules
    global majuscules
    global chiffres
    global spcharacters
    minuscules = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    majuscules = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    chiffres = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    spcharacters = ['&', '*', '$']

def length_decode():
    global length_decode
    nombre_max = input("\nIndiquez un nombre de caractères à tester : ")
    if nombre_max.isdigit():
        length_decode = int(nombre_max)
    else:
        erreur()

#loader en attendant la fin du decode
def decode_status():
    loader_length = 40

    sys.stdout.write("\n[%s]" % (" " * loader_length))
    sys.stdout.flush()
    sys.stdout.write("\b" * (loader_length+1))

    for i in range(loader_length):
        time.sleep(1)
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("\n")


#minuscules
def md5_minuscules(word, length):
    start_decode = time.time()
    if length <= length_decode:
        for letter in minuscules:
            dicionnaire = word + letter

            if encodage == "1":
                encodage_type = hashlib.md5()
            elif encodage == "2":
                encodage_type = hashlib.sha1()
            elif encodage == "3":
                encodage_type = hashlib.sha224()
            elif encodage == "4":
                encodage_type = hashlib.sha256()
            elif encodage == "5":
                encodage_type = hashlib.sha384()
            elif encodage == "6":
                encodage_type = hashlib.sha512()

            encodage_type.update(dicionnaire.encode('utf-8'))

            if md5_hash == encodage_type.hexdigest():
                print('\033[35m' + "\nLe hash déchiffré est " + '\033[0m' + '\033[32m' + word + letter)
                print('\033[32m' + md5_hash + '\033[35m' + '\033[0m' +" = " + '\033[32m' + word + letter + "\n" + '\033[0m')
                total_time_decode = time.time() - start_decode
                print("Temps de calcul total : " + str(total_time_decode) + "s\n")
                quit()
            else:
                ##print(word + letter)
                md5_minuscules(word + letter, length + 1)

#majuscules
def md5_majuscules(word, length):
    start_decode = time.time()
    if length <= length_decode:
        for letter in majuscules:
            dicionnaire = word + letter

            if encodage == "1":
                encodage_type = hashlib.md5()
            elif encodage == "2":
                encodage_type = hashlib.sha1()
            elif encodage == "3":
                encodage_type = hashlib.sha224()
            elif encodage == "4":
                encodage_type = hashlib.sha256()
            elif encodage == "5":
                encodage_type = hashlib.sha384()
            elif encodage == "6":
                encodage_type = hashlib.sha512()

            encodage_type.update(dicionnaire.encode('utf-8'))

            if md5_hash == encodage_type.hexdigest():
                print('\033[35m' + "\nLe hash déchiffré est " + '\033[0m' + '\033[32m' + word + letter)
                print('\033[32m' + md5_hash + '\033[35m' + '\033[0m' +" = " + '\033[32m' + word + letter + "\n" + '\033[0m')
                total_time_decode = time.time() - start_decode
                print("Temps de calcul total : " + str(total_time_decode) + "s\n")
                quit()
            else:
                ##print(word + letter)
                md5_majuscules(word + letter, length + 1)

#chiffres
def md5_chiffres(word, length):
    start_decode = time.time()
    if length <= length_decode:
        for letter in chiffres + spcharacters:
            dicionnaire = word + letter

            if encodage == "1":
                encodage_type = hashlib.md5()
            elif encodage == "2":
                encodage_type = hashlib.sha1()
            elif encodage == "3":
                encodage_type = hashlib.sha224()
            elif encodage == "4":
                encodage_type = hashlib.sha256()
            elif encodage == "5":
                encodage_type = hashlib.sha384()
            elif encodage == "6":
                encodage_type = hashlib.sha512()

            encodage_type.update(dicionnaire.encode('utf-8'))
            if md5_hash == encodage_type.hexdigest():
                print('\033[35m' + "\nLe hash déchiffré est " + '\033[0m' + '\033[32m' + word + letter)
                print('\033[32m' + md5_hash + '\033[35m' + '\033[0m' +" = " + '\033[32m' + word + letter + "\n" + '\033[0m')
                total_time_decode = time.time() - start_decode
                print("Temps de calcul total : " + str(total_time_decode) + "s\n")
                quit()
            else:
                ##print(word + letter)
                md5_chiffres(word + letter, length + 1)

#minuscules + majuscules
def md5_min_maj(word, length):
    start_decode = time.time()
    if length <= length_decode:
        for letter in minuscule + majuscules:
            dicionnaire = word + letter

            if encodage == "1":
                encodage_type = hashlib.md5()
            elif encodage == "2":
                encodage_type = hashlib.sha1()
            elif encodage == "3":
                encodage_type = hashlib.sha224()
            elif encodage == "4":
                encodage_type = hashlib.sha256()
            elif encodage == "5":
                encodage_type = hashlib.sha384()
            elif encodage == "6":
                encodage_type = hashlib.sha512()

            encodage_type.update(dicionnaire.encode('utf-8'))

            if md5_hash == encodage_type.hexdigest():
                print('\033[35m' + "\nLe hash déchiffré est " + '\033[0m' + '\033[32m' + word + letter)
                print('\033[32m' + md5_hash + '\033[35m' + '\033[0m' +" = " + '\033[32m' + word + letter + "\n" + '\033[0m')
                total_time_decode = time.time() - start_decode
                print("Temps de calcul total : " + str(total_time_decode) + "s\n")
                quit()
            else:
                ##print(word + letter)
                md5_min_maj(word + letter, length + 1)

#minuscules + chiffres
def md5_min_chif(word, length):
    start_decode = time.time()
    if length <= length_decode:
        for letter in minuscule + chiffres:
            dicionnaire = word + letter

            if encodage == "1":
                encodage_type = hashlib.md5()
            elif encodage == "2":
                encodage_type = hashlib.sha1()
            elif encodage == "3":
                encodage_type = hashlib.sha224()
            elif encodage == "4":
                encodage_type = hashlib.sha256()
            elif encodage == "5":
                encodage_type = hashlib.sha384()
            elif encodage == "6":
                encodage_type = hashlib.sha512()

            encodage_type.update(dicionnaire.encode('utf-8'))

            if md5_hash == encodage_type.hexdigest():
                print('\033[35m' + "\nLe hash déchiffré est " + '\033[0m' + '\033[32m' + word + letter)
                print('\033[32m' + md5_hash + '\033[35m' + '\033[0m' +" = " + '\033[32m' + word + letter + "\n" + '\033[0m')
                total_time_decode = time.time() - start_decode
                print("Temps de calcul total : " + str(total_time_decode) + "s\n")
                quit()
            else:
                ##print(word + letter)
                md5_min_chif(word + letter, length + 1)

#minuscules + chiffres + majuscules + spcharacters
def md5_all(word, length):
    start_decode = time.time()
    if length <= length_decode:
        for letter in minuscules + majuscules + chiffres + spcharacters:
            dicionnaire = word + letter

            if encodage == "1":
                encodage_type = hashlib.md5()
            elif encodage == "2":
                encodage_type = hashlib.sha1()
            elif encodage == "3":
                encodage_type = hashlib.sha224()
            elif encodage == "4":
                encodage_type = hashlib.sha256()
            elif encodage == "5":
                encodage_type = hashlib.sha384()
            elif encodage == "6":
                encodage_type = hashlib.sha512()

            encodage_type.update(dicionnaire.encode('utf-8'))

            if md5_hash == encodage_type.hexdigest():
                print('\033[35m' + "\nLe hash déchiffré est " + '\033[0m' + '\033[32m' + word + letter)
                print('\033[32m' + md5_hash + '\033[35m' + '\033[0m' +" = " + '\033[32m' + word + letter + '\033[0m')
                total_time_decode = time.time() - start_decode
                print("Temps de calcul total : " + str(total_time_decode) + "s\n")
                quit()
            else:
                ##print(word + letter)
                md5_all(word + letter, length + 1)

def method_4():
    quit()

def erreur():
    print('Entrez un nombre valide.')
    quit()

def close_chrome():
    global driver
    driver.delete_all_cookies()
    driver.close()

if __name__ == "__main__":
    prevent()
    main()
