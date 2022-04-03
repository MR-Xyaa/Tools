## WARNA ASU #####
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
##################

import random
import sys
import time
import os
def inu_ganteng_banget(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)


user_reply = input("Namamu Bang? \n")
inu_ganteng_banget('\x1b[1;92m[+]===============[ MENU ]===============[+]')
inu_ganteng_banget('\x1b[1;91m[1]____Install Bahan')
inu_ganteng_banget('\x1b[1;93m[2]____Tampilan Termux Oh-My-Zsh')
inu_ganteng_banget('\x1b[1;94m[3]____Matematika')
inu_ganteng_banget('\x1b[1;95m[4]____Dark Multi Brute Force')
inu_ganteng_banget('\x1b[1;96m[5]____KangSpam')
inu_ganteng_banget('\x1b[1;97m[6]____Terkey')
inu_ganteng_banget('\x1b[1;91m[7]____Spamcall')
inu_ganteng_banget('\x1b[1;93m[8]____Spam By Bang Xenzi')
inu_ganteng_banget('\x1b[1;94m[9]____DB-BOM Spam By Bang Xenzi')
inu_ganteng_banget('\x1b[1;94m[10]___Spamer')
inu_ganteng_banget('\x1b[1;95m[00]___EXIT TO MENU')
inu_ganteng_banget('\x1b[1;92m[+]===============[ MENU ]===============[+]')
print("Bang", user_reply)
mengetik('Pilih Menunya Bang')


