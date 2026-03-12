import os
import sys
import time
import marshal
import zlib
import base64
import threading
import itertools

# কালার কোড
C = "\033[1;36m"
G = "\033[1;32m"
Y = "\033[1;33m"
R = "\033[1;31m"
W = "\033[1;37m"
E = "\033[0m"

is_animating = False

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear_screen()
    print("\033[1;36m" + """
 ▄▄▄▄    █    ██    ▄████▄   ▓█████▄▄▄█████▓ ██▀███  
▓█████▄  ██  ▓██▒  ▒██▀ ▀█   ▓█   ▀▓  ██▒ ▓▒▓██ ▒ ██▒
▒██▒ ▄██▓██  ▒██░  ▒▓█    ▄  ▒███  ▒ ▓██░ ▒░▓██ ░▄█ ▒
▒██░█▀  ▓▓█  ░██░  ▒▓▓▄ ▄██▒ ▒▓█  ▄░ ▓██▓ ░ ▒██▀▀█▄  
░▓█  ▀█▓▒▒█████▓   ▒ ▓███▀ ░ ░▒████▒ ▒██▒ ░ ░██▓ ▒██▒
░▒▓███▀▒░▒▓▒ ▒ ▒   ░ ░▒ ▒  ░ ░░ ▒░ ░ ▒ ░░   ░ ▒▓ ░▒▓░
▒░▒   ░ ░░▒░ ░ ░     ░  ▒     ░ ░  ░   ░      ░▒ ░ ▒░
 ░    ░  ░░░ ░ ░   ░          ░      ░        ░░   ░ 
 ░         ░       ░ ░        ░  ░             ░     
      ░            ░                                 
    """ + "\033[0m")
    print("\033[1;32m" + " "*10 + "DEVELOPER : GREY NETHUNTER </>\n" + "\033[0m")
    print("\033[1;33m" + "-"*55 + "\033[0m\n")

def premium_loading():
    tasks = ["Initializing Core...", "Reading Source...", "Compiling Bytecode...", "Applying Zlib...", "Base85 Encryption...", "Finalizing Stub..."]
    sys.stdout.write("\n")
    for i in range(101):
        time.sleep(0.05)
        bar = '█' * (i // 5)
        spaces = ' ' * (20 - (i // 5))
        
        status = tasks[min(i // 17, 5)]
        
        sys.stdout.write(f"\r{C}[{G}{bar}{spaces}{C}]{E} {W}{i}%{E} - {Y}{status:<20}{E}")
        sys.stdout.flush()
    print("\n")

def animate_spinner(message):
    global is_animating
    spinner = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
    while is_animating:
        sys.stdout.write(f'\r{C}[*]{E} {message} {Y}{next(spinner)}{E}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * (len(message) + 10) + '\r')

def scan_files():
    global is_animating
    is_animating = True
    t = threading.Thread(target=animate_spinner, args=("Scanning phone for .py files...",))
    t.start()
    
    py_files = []
    try:
        for root, dirs, files in os.walk('/sdcard/'):
            if '/.' in root or 'Android/data' in root or 'Android/obb' in root:
                continue
            for file in files:
                if file.endswith('.py'):
                    py_files.append(os.path.join(root, file))
    except Exception:
        pass
        
    is_animating = False
    t.join()
    
    if not py_files:
        print(f"{R}[-] No .py files found in internal storage.{E}")
        return None
        
    print(f"{G}[+] Found {len(py_files)} Python files:{E}\n")
    for i, f in enumerate(py_files):
        file_name = os.path.basename(f)
        print(f"{C}[{i+1}]{E} {file_name}")
        
    choice = input(f"\n{W}[?] Enter the number to encrypt (or press Enter to go back): {E}")
    if choice.isdigit() and 1 <= int(choice) <= len(py_files):
        return py_files[int(choice)-1]
    return None

def encrypt_file(file_path):
    if not os.path.exists(file_path):
        print(f"\n{R}[-] Error: File not found!{E}")
        time.sleep(1)
        return

    out_dir = "/sdcard/grey Nethunter"
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    try:
        premium_loading()

        with open(file_path, 'r') as f:
            source_code = f.read()

        compiled_code = compile(source_code, '<bu_cyber_security>', 'exec')
        marshaled_data = marshal.dumps(compiled_code)
        compressed_data = zlib.compress(marshaled_data)
        encoded_data = base64.b85encode(compressed_data).decode('utf-8')

        stub = f"""# Encrypted by BU CYBER SECURITY (GREY NETHUNTER)
import marshal as m, zlib as z, base64 as b
exec(m.loads(z.decompress(b.b85decode(b'{encoded_data}'))))
"""
        
        file_name = os.path.basename(file_path)
        output_file = os.path.join(out_dir, "enc_" + file_name)

        with open(output_file, 'w') as f:
            f.write(stub)

        print(f"{G}[+] Successfully Obfuscated!{E}")
        print(f"{W}[+] Saved In : {output_file}{E}")
        print(f"{W}[+] File Size: {os.path.getsize(output_file)} bytes{E}\n")
        input(f"{Y}[*] Press Enter to continue...{E}")

    except Exception as e:
        print(f"\n{R}[-] Encryption Failed: {e}{E}")
        time.sleep(2)

def about_tool():
    banner()
    print(f"{C}="*55 + E)
    print(f"{W}                ABOUT THIS TOOL{E}")
    print(f"{C}="*55 + E + "\n")
    print(f"{G}[+] Developer:{E} GREY NETHUNTER")
    print(f"{G}[+] Team:{E} BU CYBER SECURITY\n")
    print(f"{W}Description:{E}")
    print("This is an advanced Python script obfuscator designed")
    print("to protect your source code from reverse engineering.")
    print("It uses a combination of Bytecode Compilation, Marshal")
    print("serialization, Zlib compression, and Base85 encoding.\n")
    print(f"{W}How to Use:{E}")
    print("1. Select 'Scan files' to find all .py files on your phone.")
    print("2. Enter the number of the file you want to encrypt.")
    print("3. Wait for the encryption process to finish.")
    print("4. Your encrypted file will be saved in your internal")
    print("   storage inside the 'grey Nethunter' folder.\n")
    input(f"{Y}[*] Press Enter to go back to Main Menu...{E}")

def main():
    while True:
        banner()
        print(f"{C}[1]{E} Scan phone for .py files")
        print(f"{C}[2]{E} Enter file path manually")
        print(f"{C}[3]{E} About")
        print(f"{C}[4]{E} Exit\n")
        
        choice = input(f"{G}root@bu-cyber:~# {E}").strip()
        
        if choice == '1':
            print()
            target_file = scan_files()
            if target_file:
                encrypt_file(target_file)
        elif choice == '2':
            target_file = input(f"\n{W}[?] Enter full path to .py file: {E}").strip()
            encrypt_file(target_file)
        elif choice == '3':
            about_tool()
        elif choice == '4':
            print(f"\n{R}[*] Exiting...{E}")
            sys.exit()
        else:
            print(f"\n{R}[-] Invalid choice!{E}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[-] Process stopped by user.{E}")
        sys.exit()
