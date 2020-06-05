"""
Register.py

Created by abelskaya.
Project cryptosystems_hometask
----
Режим регистрации.
Программа генерирует открытый и секретный ключи для шифрования паролей,
открытый ключ подписывается ЭЦП RSA на секретном ключе программы

Режим шифрования.
Программа запрашивает путь к файлу с открытым ключом и просит ввести пароль.
Вывод -- пароль, зашифрованный на открытом ключе криптосистемой Рабина.
"""

import RSA_Keys, Rabin_keys

if __name__ == "__main__":

    print("Please, type your passwd")

    n, p, q = Rabin_keys.generateKeysRabin(256)
    open_key = Rabin_keys.cipherRabinKey(256, n)

    f = open('key.txt', 'w')
    f.write(open_key)
    f,close()

    pswd = sys.argv[1]
    if pswd is None:
        print("Incorrect passwd, please, try again!")
    else:
        ciphered_pswd = pow(pswd, 2, n)
        print(ciphered_pswd)

