# ----------------------
# expl0r4bimus v1.0
# created by @norcholly
# https://alirfandogan.com/
# https://github.com/norcholly
# ----------------------

import colorama
import nmap
import ping3
import subprocess
import pyfiglet
import requests
import threading
import sys
import time
import os
import readline
from colorama import Fore, Style
from datetime import datetime

# Clear the terminal
subprocess.call(["clear"])

print("\n\n\n")
welcome_message = pyfiglet.figlet_format("expl0r4bimus", font="doom")

# Get the terminal width
terminal_width = os.get_terminal_size().columns

# Print by aligning each line to the center
for line in welcome_message.split("\n"):
    print(Fore.LIGHTGREEN_EX + line.center(terminal_width))
print("\n\n\n")

# Initialize Colorama
colorama.init(autoreset=True)

# Get the current time
current_time = datetime.now().strftime("%H:%M:%S")

# Create the history folder
history_folder = "history"
if not os.path.exists(history_folder):
    os.makedirs(history_folder)

# Set the Tab key as the completion key
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

# Get user input
try:
    target_ip = input(
        Fore.MAGENTA + "[" + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
        Fore.MAGENTA + "[" + Fore.LIGHTCYAN_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
        Fore.LIGHTGREEN_EX + Style.NORMAL + f"Please enter the {Style.BRIGHT}IP address{Style.NORMAL} of the target: " + Fore.LIGHTYELLOW_EX
    )

    wordlist = input(
        Fore.MAGENTA + "[" + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
        Fore.MAGENTA + "[" + Fore.LIGHTCYAN_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
        Fore.LIGHTGREEN_EX + Style.NORMAL + f"Please enter the {Style.BRIGHT}wordlist path{Style.NORMAL}: " + Fore.LIGHTYELLOW_EX
    )

    while True:
        try:
            scan_speed = int(input(
                Fore.MAGENTA + "[" + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
                Fore.MAGENTA + "[" + Fore.LIGHTCYAN_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
                Fore.LIGHTGREEN_EX + Style.NORMAL + f"Please enter the scanning {Style.BRIGHT}speed{Style.NORMAL} "
                                                    f"\n({Fore.LIGHTYELLOW_EX}1 = {Fore.LIGHTGREEN_EX}ports-services-versions-{Style.BRIGHT}slowest, {Style.NORMAL}{Fore.LIGHTYELLOW_EX}2 = {Fore.LIGHTGREEN_EX}ports-services-{Style.BRIGHT}normal, {Style.NORMAL}{Fore.LIGHTYELLOW_EX}3 = {Fore.LIGHTGREEN_EX}ports-{Style.BRIGHT}fastest):{Style.NORMAL} " + Fore.LIGHTYELLOW_EX
            ))
            print("")
            break

        except ValueError:
            print(
                Fore.MAGENTA + "\n[" + Fore.RED + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
                Fore.MAGENTA + "[" + Fore.RED + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
                Fore.RED + Style.NORMAL + f"Please enter a {Style.BRIGHT}number!" + "\r"
            )
except KeyboardInterrupt:
    print(
        Fore.MAGENTA + "\n[" + Fore.RED + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
        Fore.MAGENTA + "[" + Fore.RED + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
        Fore.RED + Style.NORMAL + "Exitting..." + "\r"
    )
    exit()

# Specify the history file
history_file = os.path.join(history_folder, f"{target_ip}.txt")

# Define a variable to store the output
output = ""


# Print and write the output to a file
def print_and_write(output_str):
    global output
    print(output_str)
    output += output_str + "\n"
    with open(history_file, 'a') as f:
        f.write(output_str + "\n")


# Scanning status
scanning = True


# Check the connection with the target machine
def ping_ip(ip):
    while True:
        try:
            response_time = ping3.ping(ip, timeout=2)  # Set a 2-second timeout period
            if response_time is not None and response_time > 0:
                print(
                    Fore.MAGENTA + "\n[" + Fore.LIGHTGREEN_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
                    Fore.MAGENTA + "[" + Fore.LIGHTGREEN_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
                    Fore.LIGHTGREEN_EX + Style.NORMAL + f"The ICMP packets sent to the target were {Style.BRIGHT}successfully {Style.NORMAL}transmitted!" + Fore.LIGHTYELLOW_EX
                )
                time.sleep(2)
                break
            else:
                print(
                    Fore.MAGENTA + "[" + Fore.RED + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
                    Fore.MAGENTA + "[" + Fore.RED + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
                    Fore.RED + Style.NORMAL + f"ICMP packets were {Style.BRIGHT}lost,{Style.NORMAL} retrying every {Style.BRIGHT}5 {Style.NORMAL}seconds..." + "\r"
                )
        except ping3.errors.PingError:
            print(
                Fore.MAGENTA + "[" + Fore.RED + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
                Fore.MAGENTA + "[" + Fore.RED + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
                Fore.RED + Style.NORMAL + f"ICMP packets were {Style.BRIGHT}lost,{Style.NORMAL} retrying every {Style.BRIGHT}5 {Style.NORMAL}seconds..." + "\r"
            )
        time.sleep(5)  # Retry after waiting for 5 seconds


# Display a blinking message while scanning
def blink_scanning():
    while scanning:
        sys.stdout.write(
            Fore.MAGENTA + "[" + Fore.RED + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
            Fore.MAGENTA + "[" + Fore.RED + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
            Fore.RED + Style.NORMAL + "Scanning... " + "\r"
        )
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(" " * 100 + "\r")  # Clear the previous line
        sys.stdout.flush()
        time.sleep(0.5)


# Scan the target IP address to find open ports
def port_scan(target_ip):
    global scanning
    nm = nmap.PortScanner()

    if scan_speed == 1:
        arguments = '-p 1-65535 -sV'
    elif scan_speed == 2:
        arguments = '-p 1-65535 -sS -sV'
    else:
        arguments = '-F'

    nm.scan(target_ip, arguments=arguments)

    open_ports = []

    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            port_info = nm[host][proto].items()
            for port, info in port_info:
                if info['state'] == 'open':
                    if scan_speed == 1:
                        service = info.get('name', 'unknown')  # Get the service name
                        version = info.get('version', 'unknown')  # Get the service version
                        open_ports.append((port, service, version))
                    elif scan_speed == 2:
                        service = info.get('name', 'unknown')
                        open_ports.append((port, service))
                    else:
                        open_ports.append(port)

    scanning = False
    return open_ports


# Perform directory search on the target URL
def directory_search(target_url, wordlist_path):
    global scanning
    found_directories = []

    # Read the file and create the directory list
    with open(wordlist_path, 'r') as file:
        directories = [line.strip() for line in file]

    for directory in directories:
        directory_url = target_url + directory  # Do not add a slash, it's already in the target_url
        response = requests.get(directory_url)
        if response.status_code == 200 and not directory_url.endswith("/#") and not directory_url.endswith("/"):
            found_directories.append(directory_url)

    scanning = False

    if found_directories:
        print_and_write(
            Fore.MAGENTA + "\n\n[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
            Fore.MAGENTA + "[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
            Fore.LIGHTBLUE_EX + Style.NORMAL + "Directories found: " + Fore.LIGHTYELLOW_EX
        )
        for directory in found_directories:
            if "#" not in directory:
                print_and_write(
                    Fore.MAGENTA + "[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
                    Fore.MAGENTA + "[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
                    Fore.LIGHTGREEN_EX + Style.BRIGHT + directory + Fore.LIGHTYELLOW_EX
                )
    else:
        print_and_write("No directories found...")


# Start scanning and process the results
try:
    ping_ip(target_ip)

    print_and_write(
        Fore.MAGENTA + "\n\n[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
        Fore.MAGENTA + "[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
        Fore.LIGHTWHITE_EX + Style.BRIGHT + "------------------------------------------------------------\n" + Fore.LIGHTYELLOW_EX
    )

    blinking_thread = threading.Thread(target=blink_scanning)
    blinking_thread.start()

    open_ports = port_scan(target_ip)
    blinking_thread.join()

    # Print open ports and services
    print_and_write(
        Fore.MAGENTA + "\n[" + Fore.LIGHTGREEN_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
        Fore.MAGENTA + "[" + Fore.LIGHTGREEN_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
        Fore.LIGHTGREEN_EX + Style.NORMAL + "Open ports and services:" + Fore.LIGHTYELLOW_EX
    )
    if scan_speed == 1:
        for port, service, version in open_ports:
            print_and_write(
                Fore.MAGENTA + "[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
                Fore.MAGENTA + "[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
                Fore.LIGHTBLUE_EX + Style.NORMAL + f"Open port:{Fore.LIGHTGREEN_EX} {Style.BRIGHT} {port},{Fore.LIGHTBLUE_EX} {Style.NORMAL} Service:{Fore.LIGHTGREEN_EX} {Style.BRIGHT} {service.upper()},{Style.NORMAL} {Fore.LIGHTBLUE_EX} Version:{Fore.LIGHTGREEN_EX} {Style.BRIGHT} {version}" + Fore.LIGHTYELLOW_EX
            )
    elif scan_speed == 2:
        for port, service in open_ports:
            print_and_write(
                Fore.MAGENTA + "[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
                Fore.MAGENTA + "[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
                Fore.LIGHTBLUE_EX + Style.NORMAL + f"Open port:{Fore.LIGHTGREEN_EX} {Style.BRIGHT} {port},{Fore.LIGHTBLUE_EX} {Style.NORMAL} Service:{Fore.LIGHTGREEN_EX} {Style.BRIGHT} {service.upper()}" + Fore.LIGHTYELLOW_EX
            )
    else:
        for port in open_ports:
            print_and_write(
                Fore.MAGENTA + "[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
                Fore.MAGENTA + "[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
                Fore.LIGHTBLUE_EX + Style.NORMAL + f"Open port:{Fore.LIGHTGREEN_EX} {Style.BRIGHT} {port}" + Fore.LIGHTYELLOW_EX
            )

    print_and_write(
        Fore.MAGENTA + "\n\n[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
        Fore.MAGENTA + "[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
        Fore.LIGHTWHITE_EX + Style.BRIGHT + "------------------------------------------------------------\n" + Fore.LIGHTYELLOW_EX
    )

    # If ports 80 or 8080 are open, perform a directory scan
    if any(port == 80 or port == 8080 for port in (p[0] if isinstance(p, tuple) else p for p in open_ports)):
        if any(port == 80 for port in (p[0] if isinstance(p, tuple) else p for p in open_ports)):
            print_and_write(
                Fore.MAGENTA + "\n[" + Fore.LIGHTGREEN_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
                Fore.MAGENTA + "[" + Fore.LIGHTGREEN_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
                Fore.LIGHTGREEN_EX + Style.NORMAL + f"Port {Style.BRIGHT}80 {Style.NORMAL}is open, indicating a potential web server. Let's perform a {Style.BRIGHT}directory scan..." + Fore.LIGHTYELLOW_EX
            )
        elif any(port == 8080 for port in (p[0] if isinstance(p, tuple) else p for p in open_ports)):
            print_and_write(
                Fore.MAGENTA + "\n[" + Fore.LIGHTGREEN_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
                Fore.MAGENTA + "[" + Fore.LIGHTGREEN_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
                Fore.LIGHTGREEN_EX + Style.NORMAL + f"Port {Style.BRIGHT}8080 {Style.NORMAL}is open, indicating a potential web server. Let's perform a {Style.BRIGHT}directory scan..." + Fore.LIGHTYELLOW_EX
            )
        target_url = f"http://{target_ip}/"
        wordlist_path = wordlist
        scanning = True
        blinking_thread = threading.Thread(target=blink_scanning)
        blinking_thread.start()
        directory_search(target_url, wordlist_path)
        blinking_thread.join()
    else:
        print_and_write(
            Fore.MAGENTA + "[" + Fore.LIGHTGREEN_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
            Fore.MAGENTA + "[" + Fore.LIGHTGREEN_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
            Fore.LIGHTGREEN_EX + Style.NORMAL + f"Neither port {Style.BRIGHT}80 {Style.NORMAL}or {Style.BRIGHT}8080 {Style.NORMAL}is open, skipping directory search..." + Fore.LIGHTYELLOW_EX
        )

    print_and_write(
        Fore.MAGENTA + "\n\n[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
        Fore.MAGENTA + "[" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
        Fore.LIGHTWHITE_EX + Style.BRIGHT + "------------------------------------------------------------\n" + Fore.LIGHTYELLOW_EX
    )

    print_and_write(
        Fore.MAGENTA + "\n[" + Fore.LIGHTWHITE_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
        Fore.MAGENTA + "[" + Fore.LIGHTWHITE_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
        Fore.LIGHTWHITE_EX + Style.NORMAL + f"All processes have been completed. \nThe processes have been saved in the 'history' directory. {Style.BRIGHT}{Fore.LIGHTRED_EX}@norcholly {Style.NORMAL}{Fore.LIGHTWHITE_EX}wishes you good attack..." + Fore.LIGHTYELLOW_EX
    )

    print_and_write(
        Fore.MAGENTA + "[" + Fore.LIGHTWHITE_EX + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
        Fore.MAGENTA + "[" + Fore.LIGHTWHITE_EX + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
        Fore.LIGHTWHITE_EX + Style.NORMAL + f"{Style.BRIGHT}{Fore.LIGHTRED_EX}expl0r4bimus v1.0" + Fore.LIGHTYELLOW_EX
    )
except KeyboardInterrupt:
    print(
        Fore.MAGENTA + "\n[" + Fore.RED + Style.BRIGHT + "Explorabimus" + Fore.MAGENTA + "] " +
        Fore.MAGENTA + "[" + Fore.RED + Style.BRIGHT + current_time + Fore.MAGENTA + "] " +
        Fore.RED + Style.NORMAL + "Exitting..." + "\r"
    )
    exit()
