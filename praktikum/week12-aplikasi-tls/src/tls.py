import ssl
import socket
from datetime import datetime

hostname = "www.tokopedia.com"
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert = ssock.getpeercert()

print("Issuer:", cert['issuer'])
print("Valid from:", cert['notBefore'])
print("Valid until:", cert['notAfter'])
