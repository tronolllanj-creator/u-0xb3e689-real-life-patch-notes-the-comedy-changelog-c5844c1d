#!/usr/bin/env python3
import os  # stdlib only: no network, no randomness
import sys

ENTRY_LINE = 'v1.0.4: Fixed a bug where blinking caused a temporary loss of consciousness and visual feed.'

def validate():
    if not (1 <= len(ENTRY_LINE) <= 160):
        raise ValueError("ENTRY_LINE length must be between 1 and 160 characters")

def entry_path():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, 'entry.txt')

def main():
    validate()
    
    file_path = entry_path()
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(ENTRY_LINE + '\n')
        
    print(f"{ENTRY_LINE}")
    print(f"Character count: {len(ENTRY_LINE)}")
    
    sys.exit(0)

if __name__ == '__main__':
    main()
