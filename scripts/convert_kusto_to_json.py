#!/usr/bin/env python3
import sys
import json
import pyperclip

def main():
    if len(sys.argv) != 2:
        print("Usage: convert_kusto_to_json.py <kusto_file_path>")
        sys.exit(1)
    kusto_file_path = sys.argv[1]
    try:
        with open(kusto_file_path, 'r', encoding='utf-8') as f:
            kusto_query = f.read()
        json_string = json.dumps(kusto_query)
        pyperclip.copy(json_string)
        print("JSON string copied to clipboard.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()
