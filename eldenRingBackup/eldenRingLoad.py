import os
import shutil
import getpass

username = getpass.getuser()

file_list=os.listdir()
file_list.remove('eldenRingBackup.py')
file_list.remove('eldenRingLoad.py')


print(file_list)
print('로드할 파일 선택하고 엔터 : ',end='')
choi=int(input())
shutil.rmtree(f"C:/Users/{username}/AppData/Roaming/EldenRing")
shutil.copytree(file_list[choi-1],f"C:/Users/{username}/AppData/Roaming/EldenRing")
