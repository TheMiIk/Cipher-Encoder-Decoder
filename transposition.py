import argparse
import json
import math

class transposition_cipher:
    def __init__(self, key_file="transpositionkey.json"):
        self.key_file = key_file
        self.key = self.load_key()

    def save_key(self, key):
        with open(self.key_file, 'w') as f:
            json.dump({"key": key}, f)
        self.key = key

    def load_key(self):
        try:
            with open(self.key_file, 'r') as f:
                data = f.read().strip()
                if not data:
                    return None
                key_data = json.loads(data)
                return key_data.get("key")
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def get_sequence(self):
        return sorted(range(len(self.key)), key=lambda x: self.key[x])

    def encrypt(self, text):
        if not self.key:
            raise ValueError("No key for encryption.")
        key_sequence = self.get_sequence()
        num_columns = len(self.key)
        num_rows = math.ceil(len(text) / num_columns)
        padding = ' ' * ((num_columns * num_rows) - len(text))
        text += padding
        grid = [list(text[i:i + num_columns]) for i in range(0, len(text), num_columns)]
        sorted_grid = [''.join(row[i] for row in grid) for i in key_sequence]
        return ''.join(sorted_grid)

    def decrypt(self, text):
        if not self.key:
            raise ValueError("No key for decryption.")
        key_sequence = self.get_sequence()
        num_columns = len(self.key)
        num_rows = math.ceil(len(text) / num_columns)
        col_lengths = [num_rows] * num_columns
        sorted_keys = sorted(enumerate(key_sequence), key=lambda x: x[1])
        grid = [''] * num_columns
        index = 0
        for i, _ in sorted_keys:
            grid[i] = text[index:index + col_lengths[i]]
            index += col_lengths[i]
        plaintext = ''.join(''.join(grid[col][row] for col in range(num_columns)) for row in range(num_rows))
        return plaintext.rstrip()

def main():
    parser = argparse.ArgumentParser(description="Transposition")
    parser.add_argument('-e', '--encrypt', action='store_true')
    parser.add_argument('-d', '--decrypt', action='store_true')
    parser.add_argument('-f', '--file')
    parser.add_argument('-o', '--output')
    parser.add_argument('-k', '--key')

    args = parser.parse_args()

    cipher = transposition_cipher()

    if args.key:
        cipher.save_key(args.key)
        print("New key set and saved.")
        return

    if not cipher.key:
        print("No encryption key found. Please set a key using the -k option.")
        return

    if not args.file or not args.output:
        print("Awaiting commands...")
        return

    with open(args.file, 'r') as infile:
        text = infile.read()

    result = cipher.decrypt(text) if args.decrypt else cipher.encrypt(text)

    with open(args.output, 'w') as outfile:
        outfile.write(result)

if __name__ == "__main__":
    main()
