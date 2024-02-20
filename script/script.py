import time
import os
from os import system
import platform

def clear():
  system = platform.system().lower()

  if system == 'windows':
      _ = os.system('cls')
  elif system == 'linux' or system == 'darwin':
      _ = os.system('clear')
  elif system == 'android':
      _ = subprocess.run(['termux-exec', 'sh', '-c', 'clear'], check=False)
  else:
      print(f"Unsupported platform '{system}'")

# Call the clear function
print("Checking if Platform is Supported!") # Warning
time.sleep(0.5)
print(f"You are using '{system}'") # OS Alert
time.sleep(1)
print("Running test!") # testing if previouse script works
print("1")
clear()

print("done")
clear()
