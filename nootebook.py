import pyautogui
import time
import os

time.sleep(1.5)

button_images = [
    'nootebook_button.png'
]

max_attempts = 100000

for image in button_images:
    if not os.path.isfile(image):
        print(f"Error: The image file '{image}' does not exist.")

for attempt in range(max_attempts):
    print(f"Attempt {attempt + 1} of {max_attempts}: Attempting to detect verification buttons...")
    time.sleep(2)

    for image in button_images:
        try:
            print(f"Trying to detect: {image}")
            location = pyautogui.locateOnScreen(image, confidence=0.8)
        except Exception as e:
            print(f"Error while detecting '{image}': {e}")
            location = None

        if location:
            print(f"'{image}' detected at {location}, clicking...")
            time.sleep(1)
            pyautogui.click(location)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            print(f"'{image}' clicked")
            exit()

    print("No buttons detected in this attempt. Pressing Down Arrow key to continue...")
    time.sleep(1)

print("Maximum detection attempts reached. Exiting...")
