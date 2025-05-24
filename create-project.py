import time
import subprocess

for _ in range(5):
    subprocess.run(["python3", "project.py"])
    time.sleep(3)

time.sleep(1.5)
