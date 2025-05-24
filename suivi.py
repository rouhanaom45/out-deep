import pyautogui
import time
import os
import subprocess
import random


def random_click_in_area(top_left, bottom_right):
    """Perform a random click within a rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)

# Step 1: Sleep for 3 seconds before starting
time.sleep(1.5)

# Paths to the images of the verification buttons
verif_button_image = 'pass1_button.png'
verif1_button_image = 'deepo_button.png'

# Maximum number of detection attempts
max_attempts = 24

# Check if both image files exist
if not os.path.isfile(verif_button_image):
    print(f"Error: The image file '{verif_button_image}' does not exist.")
if not os.path.isfile(verif1_button_image):
    print(f"Error: The image file '{verif1_button_image}' does not exist.")

# Loop for a maximum number of attempts
for attempt in range(max_attempts):
    print(f"Attempt {attempt + 1} of {max_attempts}: Attempting to detect verification buttons...")

    # Sleep for 4 seconds before each detection attempt
    time.sleep(2)

    # Try to detect the first verification button: verif_button.png
    button_location = None
    try:
        print(f"Trying to detect: {verif_button_image}")
        button_location = pyautogui.locateOnScreen(verif_button_image, confidence=0.8)
    except Exception as e:
        print(f"Error while detecting '{verif_button_image}': {e}")

    # If the first button is detected, click it
    if button_location:
        print(f"'{verif_button_image}' detected at {button_location}, clicking...")
        time.sleep(1)  # Wait before clicking
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)
        pyautogui.write('about:logins')
        time.sleep(0.7)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(656, 504)
        time.sleep(1.4)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.7)
        pyautogui.press('enter')
        time.sleep(1)
        subprocess.run(["python3", "final.py"])
        break  # Exit the loop after clicking the button

    # If the first button is not found, attempt to detect the second button: verif1_button.png
    try:
        print(f"Trying to detect: {verif1_button_image}")
        button_location = pyautogui.locateOnScreen(verif1_button_image, confidence=0.8)
    except Exception as e:
        print(f"Error while detecting '{verif1_button_image}': {e}")

    # If the second button is detected, click it
    if button_location:
        print(f"'{verif1_button_image}' detected at {button_location}, clicking...")
        time.sleep(1)  # Wait before clicking
        for _ in range(random.randint(5, 7)):
            pyautogui.press('down')
            time.sleep(random.uniform(0.5, 0.8))
        time.sleep(1)
        random_click_in_area((761, 501), (840, 515))
        time.sleep(random.uniform(8, 10))
        break  # Exit the loop after clicking the button

    # If neither button is found, press the Down Arrow key and try again
    print(f"Neither '{verif_button_image}' nor '{verif1_button_image}' detected. Pressing Down Arrow key...")
    time.sleep(1)

else:
    print("Maximum detection attempts reached. Exiting...")
    time.sleep(1)
    
