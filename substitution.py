import argparse
import string
import json

def save_key(key, filename="substitutionkey.json"):
    with open(filename, 'w') as f:
        json.dump({"key": key}, f)

def load_key(filename="substitutionkey.json"):
    try:
        with open(filename, 'r') as f:
            data = f.read().strip()
            if not data:
                return None
            return json.loads(data).get("key")
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def substitution_cipher(text, key, decrypt=False):
    alphabet = string.ascii_lowercase
    key_map = dict(zip(alphabet, key)) if not decrypt else dict(zip(key, alphabet))
    return ''.join(key_map.get(char, char) for char in text.lower())

def process_file(input_file, output_file, key, decrypt=False):
    with open(input_file, 'r') as infile:
        text = infile.read()

    result = substitution_cipher(text, key, decrypt)

    with open(output_file, 'w') as outfile:
        outfile.write(result)

def main():
    parser = argparse.ArgumentParser(description="Substitution")
    parser.add_argument('-e', '--encrypt', action='store_true')
    parser.add_argument('-d', '--decrypt', action='store_true')
    parser.add_argument('-f', '--file')
    parser.add_argument('-o', '--output')
    parser.add_argument('-k', '--key')

    args = parser.parse_args()

    if args.key:
        if len(args.key) != 26 or set(args.key) != set(string.ascii_lowercase):
            print("Invalid substitution key. Use a 26-letter shuffled alphabet.")
            return
        save_key(args.key)
        print("New key set and saved.")
        return

    key = load_key()
    if not key:
        print("No encryption key found. Please set a key using the -k option.")
        return

    if not args.file or not args.output:
        print("Awaiting commands...")
        return

    process_file(args.file, args.output, key, args.decrypt)

if __name__ == "__main__":
    main()
