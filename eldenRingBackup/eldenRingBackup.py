import os
import shutil
import getpass
from datetime import date

n = 1
username = getpass.getuser()

today = str(date.today())
name = f'{today} ({n})'

if os.path.exists(name):
    while(os.path.exists(name)):
        n += 1
        name = f'{today} ({n})'

        if n>3: #하루 세이브 갯수 제한
            n -= 1
            for i in range(1, n):
                name = f'{today} ({i})'
                shutil.rmtree(name)
                shutil.copytree(f'{today} ({i+1})', name)

            name = f'{today} ({n})'
            shutil.rmtree(name)

shutil.copytree(f"C:/Users/{username}/AppData/Roaming/EldenRing", name)
