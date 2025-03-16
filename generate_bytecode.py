#!/usr/bin/env python3
import os
import argparse

# EVM opcodes (in hex)
OP_JUMPDEST = 0x5b
OP_PUSH1 = 0x60

def generate_jumpdest_bytecode(size):
    """Generate bytecode filled with JUMPDEST opcodes"""
    return bytes([OP_JUMPDEST] * size)

def generate_push_jumpdest_bytecode(size):
    """Generate bytecode filled with PUSH1 0x5b sequences"""
    # Each sequence is 2 bytes: PUSH1 (0x60) followed by JUMPDEST value (0x5b)
    sequences_count = size // 2
    remainder = size % 2
    
    bytecode = bytes([OP_PUSH1, OP_PUSH1] * sequences_count)
    
    # Add one more byte if size is odd
    if remainder:
        bytecode += bytes([OP_PUSH1])
        
    return bytecode

def bytes_to_hex(bytecode):
    """Convert bytes to hex string with 0x prefix"""
    return "0x" + bytecode.hex()

def write_bytecode_to_file(bytecode, filename):
    """Write bytecode to a file as hex string"""
    hex_string = bytes_to_hex(bytecode)
    
    with open(filename, 'w') as f:
        f.write(hex_string)
    
    print(f"Generated {filename} ({len(bytecode)} bytes)")

def main():
    parser = argparse.ArgumentParser(description='Generate EVM bytecode for jumpdest analysis testing')
    parser.add_argument('--output-dir', default='bytecode_samples', help='Directory to output bytecode files')
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Define sizes to generate (in bytes)
    sizes = [
        128,                # 128 bytes
        1024,               # 1 KB
        48 * 1024,          # 48 KB (EIP-3860 limit)
        64 * 1024,          # 64 KB 
        128 * 1024,         # 128 KB
        256 * 1024,         # 256 KB
        512 * 1024,         # 512 KB
        1024 * 1024,        # 1 MB
        2 * 1024 * 1024,    # 2 MB
        5 * 1024 * 1024,    # 5 MB
        10 * 1024 * 1024,   # 10 MB
        15 * 1024 * 1024,   # 15 MB
    ]
    
    # Generate bytecode files
    for size in sizes:
        # Generate JUMPDEST-filled bytecode
        jumpdest_bytecode = generate_jumpdest_bytecode(size)
        jumpdest_filename = os.path.join(args.output_dir, f"jumpdest_monster_{size}b.hex")
        write_bytecode_to_file(jumpdest_bytecode, jumpdest_filename)
        
        # Generate PUSH1 JUMPDEST sequence bytecode
        push_jumpdest_bytecode = generate_push_jumpdest_bytecode(size)
        push_filename = os.path.join(args.output_dir, f"push1_monster_{size}b.hex")
        write_bytecode_to_file(push_jumpdest_bytecode, push_filename)

if __name__ == "__main__":
    main()
