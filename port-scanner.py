import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import init as colorama_init, Fore, Style

colorama_init()

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((ip, port))
        print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} Port {port} is open.")
    except Exception:
        pass
    finally:
        sock.close()

def main():
    ip = input("\nEnter the IP you want to scan: ")

    port_range = input("Specify the range of ports (x-y): ")
    start_port, end_port = map(int, port_range.split("-"))

    max_threads = input("Enter the number of threads (50 by default): ")
    
    if max_threads == '':
        max_threads = 50
    else:
        try:
            max_threads = int(max_threads)
        except ValueError as e:
            print(e)

    with ThreadPoolExecutor(max_threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)

if __name__ == "__main__":
    main()
