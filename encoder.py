from bitarray.util import int2ba
from bitarray.util import ba2int
from bitarray import bitarray
import math

def create_frame (data, msg_width, check_bits, bits_added):

    frame = int2ba(data, endian='little')
    print('raw_frame', frame)
    for i in range (bits_added):
        bitarray.insert(frame, msg_width + i, 0)
    print('frame_added_bits',frame)
    for i in range (check_bits):
        bitarray.insert(frame, 2**i - 1, 0)
    print('frame_w_fillers',frame)
    return frame 

def frame_find_ones (data_frame):

    index_list = []

    for i in range(len(data_frame)):
        if(data_frame[i] == 1):
            index_list.append(i + 1)
    print('index list', index_list)
    return index_list

def index_xor (index_list):
    
    syndrome = index_list[0]

    for i in range (1,len(index_list)):
        syndrome = syndrome ^ index_list[i]
    print('syndrome', syndrome)
    return syndrome

def msg_encode (uncoded_msg, syndrome, check_bits):

    coded_msg = bitarray.copy(uncoded_msg)

    for i in range (check_bits):
        bitarray.pop(coded_msg, 2**((check_bits -1)-i) - 1)
    print(coded_msg)
    synd_list = int2ba(syndrome, endian='little')
    while len(synd_list) < 8:
        synd_list.append(0)
    print('synd_list', synd_list)
    for i in range (check_bits):
        bitarray.insert(coded_msg, 2**i -1, synd_list[i])

    return coded_msg


def hamming_encoder (msg_data):

    print('input_data:', msg_data)
    frame_param = enc_parameter_calc(msg_data)
    frame = create_frame(msg_data, frame_param[0], frame_param[1], frame_param[2])
    index_list = frame_find_ones(frame)
    syndrome = index_xor(index_list)
    encoded_frame = msg_encode(frame, syndrome, frame_param[1])
    print('transmitted data:' ,encoded_frame)
    return encoded_frame

def checksum(encoded_frame):

    check = ba2int(encoded_frame)
    print('checksum:',check)
    return check

def enc_parameter_calc(msg_data):

    msg = int2ba(msg_data, endian='little')
    bits_added = bit_adder(msg)
    #print('bits added' ,bits_added)
    data_w = len(msg)
    #print('data_width',data_w)
    check_bits = int(math.log(data_w,2) + 1)
    #print('check_bits' ,check_bits)
    msg_w = check_bits + data_w
    #print('msg_width',msg_w)
    return msg_w, check_bits, bits_added

def bit_adder(msg):
    l1 = len(msg)
    if len(msg) < 8:
        while len(msg) < 8:
            bitarray.append(msg,0)
    elif len(msg) < 16 :
        while len(msg) < 16:
            bitarray.append(msg,0)
    elif len(msg) < 32 :
        while len(msg) < 32:
            bitarray.append(msg,0)
    elif len(msg) < 64 :
        while len(msg) < 64:
            bitarray.append(msg,0)
    l2 = len(msg)
    return l2 - l1

def encoder_test(i):
    try:
        hamming_encoder(i)
    except:
        
        print('error',i)

#bit_adder(int2ba(1952805748, endian='little'))
#for i in range (255):
#    encoder_test(i)
#hamming_encoder(57)

