import pyautogui
import subprocess
import time
import random
import string
import pyperclip


def random_click(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x + random.uniform(-2, 2), y + random.uniform(-2, 2), duration=random.uniform(0.1, 0.4))
    pyautogui.click()


def human_type(text, interval_range=(0.05, 0.15)):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(*interval_range))

def generate_random_two_char_name():
    # You can tweak this logic to use only letters or include digits
    return ''.join(random.choices(string.ascii_lowercase, k=2))

# Step 1: Sleep for 1.5 seconds
time.sleep(1.5)

# Step 2: Run start.py
subprocess.run(["python", "start.py"])
time.sleep(5)
subprocess.run(["python", "signup.py"])
time.sleep(1)
subprocess.run(["python", "signin.py"])
time.sleep(1)
