import os
import sys

def process_file(filename):

    with open(filename, 'rb') as f:
        data = f.read()
   
    # destination data
    new_data = bytearray()
   
    # 256 bytes of header, 256 bytes of trackinfo
    i = 256 + 256
    while i < len(data):
        # Add 4 KB of data
        new_data.extend(data[i:i+4096])
        # Move index
        i += 4096
        # Skip 256 bytes of trackinfo
        i += 256
   
    # Save destination data
    new_filename = filename + ".strip"
    with open(new_filename, 'wb') as f:
        f.write(new_data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python skip_trackdata.py <filename>")
    else:
        process_file(sys.argv[1])