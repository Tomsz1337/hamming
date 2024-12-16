from encoder import hamming_encoder
from decoder import hamming_decoder
from bitarray.util import base2ba, ba2base
from bitarray import bitarray

#user_input = bitarray('111100101100', endian='little')
user_input = 'wiadomosc od wyslania'
nchars = len(user_input)

def str2int (user_input):

    x = sum(ord(user_input[byte])<<8*(nchars-byte-1) for byte in range(nchars))
    
    return x

def int2str(x):

    y = ''.join(chr((x>>8*(nchars-byte-1))&0xFF) for byte in range(nchars))

    return y

def hamming_coder(user_input_str):

    user_input_int = str2int(user_input_str)
    tx_data = hamming_encoder(user_input_int)
    rx_data = hamming_decoder(tx_data)
    
    print('message:', int2str(rx_data))
    
#hamming_coder(data_translator(user_input))
#data_translator(user_input)


# int or long to string
#print(''.join(chr((x>>8*(nchars-byte-1))&0xFF) for byte in range(nchars)))
#print(x)
hamming_coder(user_input)
#y = ''.join(chr((x>>8*(nchars-byte-1))&0xFF) for byte in range(nchars))