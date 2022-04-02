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
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
user_reply = input("Siapa Namamu? \n")


print("Pengguna:", user_reply)
mengetik('===============[ MENU ]===============[+]')
mengetik('\x1b[1;94m[1]___Install Bahan')
mengetik('\x1b[1;93m[2]___Tampilan Termux Oh-My-Zsh')
mengetik('[3]___MTK')
mengetik('[4]___DMBF')
mengetik('[5]___KangSpam')
mengetik('[6]___Terkey By MR-Xyaa')
mengetik('[7]___Spamcall By MR-Xyaa')
mengetik('[8]___Spam By Bang Xenzi')
mengetik('[0]__EXIT MENU MR-Xyaa')
mengetik('[+]===============[ MENU ]===============[+]')
mengetik('Silahkan Pilih Menunya Bang')


