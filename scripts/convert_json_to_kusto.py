#!/usr/bin/env python3
import sys
import json
import pyperclip
import os

def main():
    if len(sys.argv) != 3:
        print("Usage: convert_json_to_kusto.py <directory> <base_filename>")
        sys.exit(1)

    directory = sys.argv[1]
    base_filename = sys.argv[2]
    try:
        json_string = pyperclip.paste()
        kusto_query = json.loads(json_string)
        output_file_path = os.path.join(directory, f"{base_filename}")
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(kusto_query)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
