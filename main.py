import gc
import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(5)
while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        client_s, client_addr = s.accept()
        s.settimeout(3.0)
        req = client_s.recv(4096)
        s.settimeout(None)
        client_s.send(req)
        client_s.close()
    except OSError as e:
        client_s.close()

