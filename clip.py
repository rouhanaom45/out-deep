import time
import subprocess
import pyperclip

# Step 1: Sleep for 1 second
time.sleep(1)

# Step 2: Run generator.py
subprocess.run(["python3", "generator.py"])

# Step 3: Sleep for 1.5 seconds
time.sleep(1.5)

# Step 4: Copy contents of book.py to clipboard
with open("book.py", "r") as file:
    content = file.read()
pyperclip.copy(content)

# Step 5: Sleep for 1 second
time.sleep(1)
