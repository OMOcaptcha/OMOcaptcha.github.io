import socket
import threading
from queue import Queue

START_IP = "192.168.1.1"
END_IP   = "192.168.255.255"
PORT = 445
TIMEOUT = 0.5
THREADS = 3000

queue = Queue()
lock = threading.Lock()

total = 0
done = 0

def ip_to_int(ip):
    a,b,c,d = map(int, ip.split("."))
    return (a<<24) + (b<<16) + (c<<8) + d

def int_to_ip(n):
    return ".".join(str((n >> i) & 255) for i in (24,16,8,0))

def scan():
    global done
    while True:
        try:
            ip = queue.get_nowait()
        except:
            return

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(TIMEOUT)
            if s.connect_ex((ip, PORT)) == 0:
                with lock:
                    print(f"\n[OPEN] {ip}:{PORT}")
                    with open("open_host.txt", "a") as f:
                        f.write(f"{ip}:{PORT}\n")
                    with open("open_host.txt", "a") as f:
                        f.write(f"\\\\{ip}\n")
            s.close()
        except:
            pass

        with lock:
            done += 1
            percent = (done / total) * 100
            print(f"\rProgress: {done}/{total} ({percent:.2f}%)", end="")

        queue.task_done()

# fill queue
start = ip_to_int(START_IP)
end   = ip_to_int(END_IP)

for i in range(start, end + 1):
    queue.put(int_to_ip(i))

total = queue.qsize()
print(f"Total IPs: {total}")

# start threads
for _ in range(THREADS):
    threading.Thread(target=scan, daemon=True).start()

queue.join()
print("\nDone.")
