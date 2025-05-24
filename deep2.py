import pyautogui
import subprocess
import time
import string
import random

def generate_patterned_name(length=6, with_digits=False):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    name = ''
    for _ in range(length // 2):
        name += random.choice(consonants) + random.choice(vowels)
    if len(name) < length:
        name += random.choice(vowels)
    if with_digits:
        name += f"{random.randint(10, 99)}"
    return name[:length] + (name[length:] if with_digits else '')

def random_click(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x + random.uniform(-2, 2), y + random.uniform(-2, 2), duration=random.uniform(0.1, 0.4))
    pyautogui.click()

def human_type(text, interval_range=(0.05, 0.15)):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(*interval_range))

# Loop until welcom.py succeeds
while True:
    time.sleep(1)

    # Run welcom.py and check return code
    result = subprocess.run(["python", "welcom.py"])
    if result.returncode == 0:
        print("welcom.py succeeded. Continuing with remaining steps...")
        break  # Exit loop and continue with remaining steps
    else:
        print("welcom.py failed. Restarting deep2.py...")
        continue  # Restart the loop

# Remaining steps to execute after welcom.py succeeds
time.sleep(1)

for _ in range(random.randint(6, 8)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(random.uniform(1.0, 2.0))

random_click((857, 229), (1039, 434))
time.sleep(random.uniform(1.0, 1.6))

random_click((519, 528), (840, 543))
time.sleep(random.uniform(3.5, 4.6))

random_click((75, 196), (344, 525))
time.sleep(random.uniform(1.0, 1.3))

for _ in range(random.randint(3, 4)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(random.uniform(1.0, 2.0))

random_click((520, 486), (841, 505))
time.sleep(random.uniform(3.5, 4.6))
random_click((75, 196), (344, 525))
time.sleep(random.uniform(1.0, 1.3))
for _ in range(random.randint(3, 4)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(random.uniform(1.0, 2.0))

def action_one():
    random_click((504, 458), (555, 471))
    time.sleep(random.uniform(1.0, 1.3))

def action_two():
    random_click((587, 458), (638, 474))
    time.sleep(random.uniform(1.0, 1.3))

# Randomly choose and execute one action
random.choice([action_one, action_two])()

time.sleep(0.5)

random_click((512, 527), (835, 542))
time.sleep(random.uniform(3.5, 4.6))

name3 = generate_patterned_name(random.randint(6, 8))
human_type(name3)
time.sleep(random.uniform(1.2, 2.3))

random_click((82, 255), (318, 488))
time.sleep(random.uniform(1.0, 1.3))

for _ in range(random.randint(3, 4)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(random.uniform(1.0, 2.0))

actions = [
    lambda: (random_click((517, 417), (620, 428)), time.sleep(random.uniform(1.0, 1.3))),
    lambda: (random_click((654, 415), (750, 428)), time.sleep(random.uniform(1.0, 1.3))),
    lambda: (random_click((515, 459), (596, 472)), time.sleep(random.uniform(1.0, 1.3))),
    lambda: (random_click((632, 457), (728, 472)), time.sleep(random.uniform(1.0, 1.3))),
]

# Randomly execute one of them
random.choice(actions)()

random_click((526, 528), (837, 544))
time.sleep(random.uniform(3.5, 4.6))

random_click((34, 300), (163, 544))
time.sleep(random.uniform(1.0, 1.3))

for _ in range(random.randint(7, 9)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(random.uniform(1.0, 2.0))

random_click((253, 428), (585, 440))
time.sleep(random.uniform(3.5, 4.6))

print("deep2.py finished successfully.")
