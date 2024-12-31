import socket
import threading
import logging
from queue import Queue

# Set up logging
logging.basicConfig(filename='penetration_testing.log', level=logging.INFO)

def scan_port(target, port, q):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        q.put(port)
    sock.close()

def port_scan(target, port_range):
    open_ports = []
    q = Queue()

    threads = []
    for port in port_range:
        thread = threading.Thread(target=scan_port, args=(target, port, q))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    while not q.empty():
        open_ports.append(q.get())

    return open_ports

if __name__ == "__main__":
    target = input("Enter the target IP: ")
    port_range = list(range(1, 1024))  # Default port range
    open_ports = port_scan(target, port_range)
    
    if open_ports:
        logging.info(f"Open ports on {target}: {open_ports}")
        print(f"Open ports on {target}: {open_ports}")
    else:
        logging.info(f"No open ports found on {target}")
        print(f"No open ports found.")
