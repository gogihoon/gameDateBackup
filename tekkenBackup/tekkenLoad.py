import os
import shutil
import getpass

username = getpass.getuser()

file_list=os.listdir()
file_list.remove('tekkenBackup.py')
file_list.remove('tekkenLoad.py')


print(file_list)
print('로드할 파일 선택하고 엔터 : ',end='')
choi=int(input())
shutil.rmtree(r"C:\Users\zzzrl\AppData\Local\TekkenGame\Saved\SaveGames\TEKKEN7")
shutil.copytree(file_list[choi-1],r"C:\Users\zzzrl\AppData\Local\TekkenGame\Saved\SaveGames\TEKKEN7")
