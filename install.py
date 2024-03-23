import os

with open("packages.x86_64") as f:
    lines = f.readlines()
    for line in lines:
        os.system("pacman -S " + line + " --noconfirm")
