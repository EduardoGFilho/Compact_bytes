import numpy as np

"""
The functions in the file are meant to facilitate dealing with int datatypes which require less than
1 byte (8 bits) to be represented. compact_bytes "squishes" the data together ignoring the zeros on the most
significant bits, decompact_bytes undoes this process, introducing zeros to such spaces.
"""

#TODO: Since these functions are meant to be use didactically, a couple of "features" could be added:
#Error messages for when inputs are invalid, such as size(a)>=8 or num_bits >=8
#Or warnings which indicate the right number of bits for encoding certain range



def compact_bytes(input_array, num_bits):
    if(num_bits >= 8):
        raise ValueError('This function is meant to work with less than 8 bits!')
        
    input_arr_len = len(input_array) # Lenght of the input
    bit_array = np.array([], dtype=np.uint8) # Inilization of array to hold the unpacked bits
    for i in range(input_arr_len):
        tmp_array = np.unpackbits(np.uint8(input_array[i]), bitorder = "little")[0:num_bits] # unpack byte and discard the most significant bits since they're not necessary
        bit_array = np.concatenate((bit_array, tmp_array), dtype = np.uint8) # "Squish" together all the relevant data into a single array

    output_array = np.packbits(bit_array, bitorder="little") # Turn the "squished" data into a new array and return it

    return output_array

def decompact_bytes(input_array, num_bits):
    if(num_bits >= 8):
        raise ValueError('This function is meant to work with less than 8 bits!')

    output_arr_len = (len(input_array)*8) // num_bits # Figure out how manu numbers were on the original array, which should be the uncompressed output
    bit_array = np.unpackbits(input_array, bitorder = "little") # Unpack "Squished" data
    output_array = np.array([], dtype = np.uint8) # Initialize array to hold the output values
    padding = np.zeros(8 - num_bits, dtype = np.uint8) # Number of zeros present in each value before the compression

    for i in range(output_arr_len):
        tmp_array = bit_array[num_bits*i:num_bits*(i+1)] # Take the data of a single number
        padded_tmp_arr = np.concatenate((tmp_array,padding)) # Pad it so that it has 8 bits
        value = np.packbits(padded_tmp_arr, bitorder = "little") # Pack it back into a byte, little-endianess is an arbitraty choice and the code could be adapted

        output_array = np.concatenate((output_array, value)) # Put the restored data into an array

    return output_array

