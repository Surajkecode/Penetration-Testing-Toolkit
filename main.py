import sys
import os
from port_scanner import port_scan
from brute_forcer import brute_force_login
from http_header_analyzer import analyze_http_headers
from dir_buster import brute_force_directories
from network_sniffer import sniff_packets
from ssl_scanner import ssl_check
from vulnerability_scanner import run_vulnerability_scans
from report_generator import generate_report

# Function to show the menu and handle user input
def show_menu():
    print("\nPenetration Testing Toolkit - Main Menu")
    print("1. Port Scanner")
    print("2. Brute Force Login")
    print("3. HTTP Header Analyzer")
    print("4. Directory Buster")
    print("5. Network Sniffer")
    print("6. SSL/TLS Certificate Scanner")
    print("7. Vulnerability Scanner")
    print("8. Generate Report")
    print("9. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == '1':
            target = input("Enter the target IP: ")
            port_range = list(range(1, 1024))  # Default port range
            open_ports = port_scan(target, port_range)
            if open_ports:
                print(f"Open ports: {open_ports}")
                generate_report("Port Scan", target, f"Open ports: {open_ports}")
            else:
                print("No open ports found.")

        elif choice == '2':
            target = input("Enter the target URL: ")
            username = input("Enter the username: ")
            wordlist_file = input("Enter the path to the wordlist: ")
            brute_force_login(target, username, wordlist_file)

        elif choice == '3':
            target_url = input("Enter the target URL: ")
            headers = analyze_http_headers(target_url)
            if headers:
                for header, value in headers.items():
                    print(f"{header}: {value}")
                generate_report("HTTP Header Analysis", target_url, str(headers))
            else:
                print("Failed to retrieve headers.")

        elif choice == '4':
            url = input("Enter the target URL: ")
            wordlist_file = input("Enter the path to the wordlist: ")
            brute_force_directories(url, wordlist_file)

        elif choice == '5':
            interface = input("Enter the network interface (e.g., eth0, wlan0): ")
            print("Starting packet sniffing...")
            sniff_packets(interface)

        elif choice == '6':
            target_url = input("Enter the target URL: ")
            cert = ssl_check(target_url)
            if cert:
                subject, issuer, not_after = parse_cert(cert)
                print(f"Subject: {subject}")
                print(f"Issuer: {issuer}")
                print(f"Certificate Expiry Date: {not_after}")
                generate_report("SSL Certificate Check", target_url, str(cert))
            else:
                print("SSL certificate not found.")

        elif choice == '7':
            url = input("Enter the target URL: ")
            vulnerabilities = run_vulnerability_scans(url)
            if vulnerabilities:
                print(f"Vulnerabilities found: {', '.join(vulnerabilities)}")
                generate_report("Vulnerability Scan", url, f"Vulnerabilities: {', '.join(vulnerabilities)}")
            else:
                print("No vulnerabilities found.")

        elif choice == '8':
            print("Generating a custom report...")
            test_type = input("Enter test type (e.g., Port Scan, Vulnerability Scan): ")
            target = input("Enter target: ")
            result = input("Enter result: ")
            generate_report(test_type, target, result)

        elif choice == '9':
            print("Exiting the toolkit.")
            sys.exit()

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
