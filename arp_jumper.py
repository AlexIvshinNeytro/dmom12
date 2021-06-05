#!/usr/bin/env python2
import subprocess
import time
        

def arp_daemon():
    a = subprocess.run('arp -an')
    print(a)
while True:
   time.sleep(5)
   arp_daemon()
def exit():
    exit(0)
       
