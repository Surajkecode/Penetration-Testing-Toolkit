import ssl
import socket
from datetime import datetime

def ssl_check(url):
    try:
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=url)
        conn.connect((url, 443))
        cert = conn.getpeercert()
        return cert
    except Exception as e:
        print(f"Error: {e}")
        return None

def parse_cert(cert):
    subject = dict(cert['subject'])
    issuer = dict(cert['issuer'])
    not_after = cert['notAfter']
    return subject, issuer, not_after

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    cert = ssl_check(target_url)

    if cert:
        subject, issuer, not_after = parse_cert(cert)
        print(f"Subject: {subject}")
        print(f"Issuer: {issuer}")
        print(f"Certificate Expiry Date: {not_after}")
    else:
        print("SSL certificate not found.")
