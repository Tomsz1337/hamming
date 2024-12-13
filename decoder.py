from bitarray import bitarray
from encoder import frame_find_ones, index_xor
import math
from functools import reduce

rx_data = bitarray('111100101100', endian='little')


def dec_param_calc(received_data):

    data_w = len(received_data)
    check_bits = int(math.log(data_w,2) + 1)
    
    return check_bits


def syndrome_extract (input_frame, check_bits):

    output_list = []

    for i in range (check_bits):
        output_list.append(input_frame[2**(3-i) -1])

    syndrome_int = int(reduce(lambda x, y: x * 10 + y, output_list))
    #print(syndrome_int)
    return syndrome_int


def code_bits2fillers (input_frame, check_bits):

    x = bitarray.copy(input_frame)

    for i in range (check_bits):
        x[2**((check_bits -1)-i) - 1] = 0
    return x

def error_calc(frame_removed_code, syndrome_extracted):
    print(syndrome_extracted)
    index_list = frame_find_ones(frame_removed_code)
    print(index_list)
    data_xor = int(index_xor(index_list))
    print(data_xor)
    error_pos = data_xor ^ syndrome_extracted
    print(error_pos)
    return error_pos

def error_correction(frame, error_pos):
    
    if not error_pos == 0:
        frame[error_pos - 1] = not(frame[error_pos - 1])
    
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
    #corrected_frame = error_correction(codeWfillers, error_pos)
    #data = msg_translate(corrected_frame, check_bits)
    #print(error_pos)
    


hamming_decoder(rx_data)
