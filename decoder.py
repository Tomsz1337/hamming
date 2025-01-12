from bitarray import bitarray
from bitarray.util import ba2int
from encoder import frame_find_ones, index_xor
import math


rx_data = bitarray('111100101110', endian='little')


def dec_param_calc(received_data):

    data_w = len(received_data)
    check_bits = int(math.log(data_w,2) + 1)
    
    return check_bits


def syndrome_extract (input_frame, check_bits):

    output_list = []
    syndrome_int = 0

    for i in range (check_bits):
        output_list.append(input_frame[2**i - 1])
    #print (output_list)
    for i in range (len(output_list)):
        syndrome_int |= (output_list[i] * 2**i)

    return syndrome_int


def code_bits2fillers (input_frame, check_bits):

    x = bitarray.copy(input_frame)

    for i in range (check_bits):
        x[2**((check_bits -1)-i) - 1] = 0
    return x

def error_calc(frame_removed_code, syndrome_extracted):
    #print(syndrome_extracted)
    index_list = frame_find_ones(frame_removed_code)
    #print(index_list)
    data_xor = int(index_xor(index_list))
    #print(data_xor)
    error_pos = data_xor ^ syndrome_extracted
    #print(error_pos)
    return error_pos

def error_correction(frame, error_pos):
    
    try:
        x = 1 / error_pos
    except:
        print('no error found')
    else:
        if not error_pos == 0:
            frame[error_pos - 1] = not(frame[error_pos - 1])
        print('error detected on position:', error_pos)

    return frame

def msg_translate (frame_corrected, check_bits):

    x = bitarray.copy(frame_corrected)

    for i in range (check_bits):
        bitarray.pop(x, 2**((check_bits -1)-i) - 1)

    return x



def hamming_decoder(received_data):

    check_bits = dec_param_calc(received_data)
    ext_synd = syndrome_extract(received_data, check_bits)
    codeWfillers = code_bits2fillers(received_data, check_bits)
    error_pos = error_calc(codeWfillers, ext_synd)
    corrected_frame = error_correction(codeWfillers, error_pos)
    data = msg_translate(corrected_frame, check_bits)
    print('received frame:',data)
    print('received data int:', ba2int(data))
    return ba2int(data)
    
def syndrome_extract_test():
    syndrome_int = 0
    output_list = [1,1,1,0]
    print(output_list)
    for i in range (len(output_list)):
        syndrome_int |= (output_list[i] * 2**i)
    print(syndrome_int)
    return syndrome_int

#hamming_decoder(rx_data)
