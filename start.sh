#!/bin/bash


scripts=(
  "omocaptcha.py"
  "outlook1.py"
  "microsoft.py"
  "outlook2.py"
  "hold.py"
  "outlook3.py"
  "deep1.py"
  "deep2.py"
  "api.py"
  "create-project.py"
)

# Run each script in order
for script in "${scripts[@]}"; do
  echo "Running $script..."
  python3 "$script"
  if [ $? -ne 0 ]; then
    echo "Error: $script failed. Exiting."
    exit 1
  fi
  echo "$script finished successfully."
done

sleep 2.5

bash upload.sh
sleep 2
echo "stop now" > /root/failure.txt
sleep 1
