#!/usr/bin/env python
from subprocess import *
import time
from scapy.all import *  
import socket
import re


def get_arp_table():
	ret = []
	commandOutput = os.popen('arp -a').read()
	lines = commandOutput.split('\n')
	lines = [e for e in lines if (not 'ress' in e)]
	ACTIVE_IFACE = None
	ID=1
	for line in lines:	
		if line=='':
			continue
		if line[:9]=='Interface':
			ACTIVE_IFACE = line.split(' ')[1]		
		else:
			if ACTIVE_IFACE is None:
				continue	
			line = re.sub(r' +', r' ', line).strip()
			IPV4, PHYSICAL, CACHE_TYPE = line.split(' ')
			CACHE_TYPE = 'dynamic' if CACHE_TYPE[:4]=='dyna' else 'static'		
			ret.append([ID, ACTIVE_IFACE, IPV4, PHYSICAL, CACHE_TYPE])
			ID += 1		
	return ret 
      
def arp_daemon():
   device = socket.if_nameindex()
   device_name = 'wlp1s0'
   p = get_arp_table() #subprocess.run(['arp', '-a']) 
   c =[p]
   if (device[:] == device_name):
        print (['device',device_name,'not found'])
        exit()
   else:
       print(c)
       # with open(r'/opt/mylog', 'a') as log:
        #    log.writelines("%s\n" % line for line in c)
while True:
   time.sleep(3)
   arp_daemon()
       
if __name__ == '__main__':
    arp_daemon()