import nmap
import json
import os
import subprocess

output = subprocess.check_output("ip addr", shell=True)

print(output)

#os.system('ipaddr')

#nm = nmap.PortScanner()
#scan = nm.scan(hosts="10.0.0.178",arguments="--script exploit -Pn -p 445")
#scan = nm.scan(hosts="10.66.29.1/24", arguments="--script exploit -Pn -p- ")

#f = open("output_1.json","w+")
#f.write(json.dumps(scan))
#f3.close

#print(scan)