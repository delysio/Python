#!/usr/bin/env python3
import sys
import os
import argparse

def show_help():
    """Display help information for the program."""
    help_text = """
Inverts bytes in a file from a specified offset

Usage:
  python byte_inverter.py input_file [--output OUTPUT_FILE] [--offset OFFSET_HEX] [--help]

Arguments:
  input_file             Path to the input file to process

Options:
  --output, -o           Specify custom output filename (default: input_file.inv)
  --offset, -f           Specify offset in hexadecimal (default: 0x1200)
  --help, -h             Display this help message and exit

Example:
  python byte_inverter.py data.bin -o modified.bin -f 0x2000

Description:
  This program reads an input file, copies bytes before the specified offset unchanged,
  and performs an XOR operation with 0xFF on all bytes after the offset.
  The result is saved to the output file.
"""
    print(help_text)

def invert_bytes(input_file, output_file=None, offset=0x1200):
    try:
        # Check if file exists
        if not os.path.exists(input_file):
            print(f"Error: File {input_file} does not exist.")
            return False
            
        # Create output filename if not provided
        if output_file is None:
            output_file = f"{input_file}.inv"
        
        with open(input_file, 'rb') as in_file, open(output_file, 'wb') as out_file:
            # Copy bytes before the offset without changes
            data_before = in_file.read(offset)
            out_file.write(data_before)
            
            # Read the rest of the file and invert bytes
            data_after = in_file.read()
            inverted_data = bytes([byte ^ 0xFF for byte in data_after])
            out_file.write(inverted_data)
            
        print(f"File processed successfully. Result saved to: {output_file}")
        return True
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def parse_arguments():
    parser = argparse.ArgumentParser(add_help=False, description="Byte Inverter - Inverts bytes in a file from a specified offset")
    parser.add_argument("input_file", nargs="?", help="Path to the input file to process")
    parser.add_argument("--output", "-o", help="Specify custom output filename")
    parser.add_argument("--offset", "-f", help="Specify offset in hexadecimal (default: 0x1200)")
    parser.add_argument("--help", "-h", action="store_true", help="Display help message and exit")
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    
    # Show help if requested or if no input file provided
    if args.help or args.input_file is None:
        show_help()
        sys.exit(0)
        
    # Parse offset if provided
    offset = 0x1200  # Default offset
    if args.offset:
        try:
            offset = int(args.offset, 16)
        except ValueError:
            print(f"Error: Invalid offset format. Please use hexadecimal format (e.g., 0x1200)")
            sys.exit(1)
    
    # Process the file
    success = invert_bytes(args.input_file, args.output, offset)
    sys.exit(0 if success else 1)