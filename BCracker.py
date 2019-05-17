import os
import bitcoin

#This file 'Bits.txt' would contain the addresses you would want to bruteforce

filexy = open('Bits.txt',mode='r')

#Loading all the addresses to memory for fast search
bit_addresses = filexy.read()

filexy.close()

#xchoicesx is structured this way so that lower part of the stack of possible private keys also have a chance to be searched cause if only a simple os.urandom for 2**255 possible private keys, most of the time only really big private keys are generated and tinier private keys don't usually have much chance to be searched!
xchoicesx = [2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]


#This fucntion Generates a private key

def Generate_Private_key_hex():
    while True:
        ln = xchoicesx[os.urandom(1)[0]]
        k = ""
        for i in range(0,ln):
            k += (('{:02x}'.format(os.urandom(1)[0]))+('{:02x}'.format(os.urandom(1)[0])))
        if len(k) <= 64:
            return (((64 - len(k)) * '0')+k)


inmbr = 0
found_nmbr = 0

#The file 'bitsybitsy.txt' would contain all the found bitcoin addresses that have been bruteforced and have been found in the 'Bits.txt' file
filex2 = open('bitsybitsy.txt', 'a')

while True:
    inmbr += 1
    if inmbr % 50000 == 0:
        #Every 50000 iterations that's been done print a notice so we know how far we have come
        print(inmbr)
    private_key_hex = Generate_Private_key_hex()
    if bitcoin.pubkey_to_address(bitcoin.compress(bitcoin.privkey_to_pubkey(private_key_hex))) in bit_addresses:
        #Every bitcoin private key has two types of addresses either a compressed address or an uncompressed one, here we search the compressed version
        found_nmbr += 1
        print(private_key_hex)
        filex2.write(private_key_hex + "\n")
        filex2.flush()
        print("* * * C O M P R E S S E D * * *")
        filex2.write("* * * C O M P R E S S E D * * *" + "\n")
        print("Found " + str(found_nmbr) +" number of address(es) so far. After " + str(inmbr) + " tries.")
        filex2.write("Found " + str(found_nmbr) +" number of address(es) so far. After " + str(inmbr) + " tries." + "\n")
        print("Private key HEX value is: " + private_key_hex)
        filex2.write("Private key HEX value is: " + private_key_hex + "\n")
        print("The bitcoin address found (Compressed): " + bitcoin.pubkey_to_address(bitcoin.compress(bitcoin.privkey_to_pubkey(private_key_hex))))
        filex2.write("The bitcoin address found (Compressed): " + bitcoin.pubkey_to_address(bitcoin.compress(bitcoin.privkey_to_pubkey(private_key_hex))) + "\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        filex2.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n")
        filex2.flush()
    if  bitcoin.pubkey_to_address(bitcoin.privkey_to_pubkey(private_key_hex)) in bit_addresses:
        #Every bitcoin private key has two types of addresses either a compressed address or an uncompressed one, here we search the uncompressed version
        found_nmbr += 1
        print(private_key_hex)
        filex2.write(private_key_hex + "\n")
        filex2.flush()
        print(": : : U N C O M P R E S S E D : : :")
        filex2.write(": : : U N C O M P R E S S E D : : :" + "\n")
        print("Found " + str(found_nmbr) + " number of address(es) so far. After " + str(inmbr) + " tries.")
        filex2.write("Found " + str(found_nmbr) + " number of address(es) so far. After " + str(inmbr) + " tries." + "\n")
        print("Private key HEX value is: " + private_key_hex)
        filex2.write("Private key HEX value is: " + private_key_hex + "\n")
        print("The bitcoin address found (Uncompressed): " + bitcoin.pubkey_to_address(bitcoin.privkey_to_pubkey(private_key_hex)))
        filex2.write("The bitcoin address found (Uncompressed): " + bitcoin.pubkey_to_address(bitcoin.privkey_to_pubkey(private_key_hex)) + "\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        filex2.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n")
        filex2.flush()
