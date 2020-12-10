import sys
import argparse
import csv
import os
import math

import string


# @Gooey(program_name= "Hex to Binary Conversation",
#      program_description="Hex to Binary Conversation")
def main(argv):
    binary_file = ''
    hex_file = ''
    # parser = GooeyParser(description="Hex to Binary Conversation for .txt for .csv files")
    # parser.add_argument("-h", help="Choose hex file", widget='FileChooser')
    # args = parser.parse_args()
    parser = argparse.ArgumentParser()
    parser.add_argument("--hex", help="Include Hex File Here")
    args = parser.parse_args()

    if args.hex:
        hex_file = args.hex
    else:
        print("Please provide a hex file")
        exit(1)

    if not os.path.exists(hex_file):
        print("Cannot find " + str(hex_file))
        exit(1)
    original_hex_directory = os.path.abspath(hex_file)
    binary_directory = original_hex_directory.replace('.txt', '') + "_bin.txt"

    csv_file = open(binary_directory, 'w', newline='')
    binary_writer = csv.writer(csv_file, delimiter=' ', lineterminator='\n')

    scale = 16

    with open(hex_file, newline='') as csvfile:
        hex_reader = csv.reader(csvfile, delimiter=' ')
        for row in hex_reader:
            binary_string = []
            for col in row:
                if not hex_check(col):
                    print("Not hex value found")
                    continue
                num_of_bits = int(len(col) * math.log2(scale))
                binary_text = bin(int(col, scale))[2:].zfill(num_of_bits)
                binary_string.append(binary_text)
            binary_writer.writerow(binary_string)

    csv_file.close()


def hex_check(value):
    for letter in value:

        # If anything other than hexdigit
        # letter is present, then return
        # False, else return True
        if (letter not in string.hexdigits):
            return False
    return True


if __name__ == '__main__':
    main(sys.argv[1:])
