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
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)


user_reply = input("Namamu Bang? \n")
mengetik('\x1b[1;92m[+]===============[ MENU ]===============[+]')
mengetik('\x1b[1;91m[1]___Install Bahan')
mengetik('\x1b[1;93m[2]___Tampilan Termux Oh-My-Zsh')
mengetik('\x1b[1;94m[3]___MTK')
mengetik('\x1b[1;95m[4]___DMBF')
mengetik('\x1b[1;96m[5]___KangSpam')
mengetik('\x1b[1;97m[6]___Terkey')
mengetik('\x1b[1;91m[7]___Spamcall')
mengetik('\x1b[1;93m[8]___Spam By Bang Xenzi')
mengetik('\x1b[1;94m[9]___DB-BOM Spam By Bang Xenzi')
mengetik('\x1b[1;95m[0]___EXIT MENU MR-Xyaa')
mengetik('\x1b[1;92m[+]===============[ MENU ]===============[+]')
print("Bang", user_reply)
mengetik('Silahkan Pilih Menunya')


