import pyautogui
import time
import random
import string
import subprocess

time.sleep(2)

def human_typing(text):
    """Simulate human-like typing."""
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.15))

def random_click_in_area(top_left, bottom_right):
    """Perform a random click within a rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)

def generate_random_name(length=6):
    """Generate a random name with alternating consonant and vowel."""
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    name = ""
    for _ in range(length):
        name += random.choice(consonants) + random.choice(vowels)
    return name[:length]


subprocess.run(["python3", "ready.py"])
time.sleep(3.5)
subprocess.run(["python3", "stop.py"])
time.sleep(2)
subprocess.run(["python3", "down.py"])
time.sleep(2)

random_click_in_area((1334, 169), (1349, 183))
time.sleep(random.uniform(1, 1.5))

random_click_in_area((1129, 245), (1316, 254))
time.sleep(random.uniform(4, 5.5))

random_click_in_area((22, 280), (230, 294))
time.sleep(random.uniform(4, 5.5))

random_click_in_area((460, 311), (547, 319))
time.sleep(random.uniform(3, 3.8))

random_click_in_area((264, 332), (292, 499))
time.sleep(random.uniform(1, 1.5))

for _ in range(random.randint(8, 10)):
    pyautogui.press('down')
    time.sleep(random.uniform(0.5, 0.8))

time.sleep(1)

random_click_in_area((1222, 402), (1297, 414))
time.sleep(random.uniform(2, 2.5))

random_name = generate_random_name(random.randint(6, 8))
human_typing(random_name)
time.sleep(random.uniform(0.5, 1))

random_click_in_area((813, 457), (870, 471))
time.sleep(random.uniform(2, 2.5))

random_click_in_area((863, 419), (871, 426))
time.sleep(random.uniform(1, 1.5))

random_click_in_area((832, 495), (872, 509))
time.sleep(random.uniform(2, 2.5))

subprocess.run(["python3", "save.py"])
