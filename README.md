# SerialGen
An automation script for ysoserial payload generation.

- Intro
  - As BurpSuite's Deserialization Scanner almost never works... I built SerialGen to automate the generation of payloads using ysoserial.
  
- How it works
  - Basically, the script generates DNS lookup payloads for all gadgets supported by ysoserial, and outputs everything to a burp_payloads.txt file, so you can load it in Intruder afterwards.
  - Each payload will attempt to make a DNS resolution to {gadgetName}.{domain}, so you can identify the ones that worked when they arrive in collaborator

# Usage

```
python3 serialgen.py <domain>
```
