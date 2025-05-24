import os
import time
import random
import string
import pyperclip

def generate_unique_filename(prefix="deep", extension=".txt"):
    while True:
        rand_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
        filename = f"{prefix}{rand_part}{extension}"
        if not os.path.exists(filename):
            return filename

def find_deep_file():
    for fname in os.listdir():
        if fname.startswith("deep") and fname.endswith(".txt") and os.path.isfile(fname):
            return fname
    return None

time.sleep(1)

clipboard_content = pyperclip.paste()

if not clipboard_content.strip():
    print("Clipboard is empty. Exiting.")
    exit()

target_file = find_deep_file()

if target_file is None:
    target_file = generate_unique_filename()
    print(f"No 'deep*.txt' file found. Creating new file: {target_file}")
else:
    print(f"Found existing file: {target_file}")

with open(target_file, "a", encoding="utf-8") as f:
    f.write(clipboard_content)
    f.write("\n")

print(f"Clipboard content saved to: {target_file}")
