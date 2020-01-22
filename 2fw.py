import sys
import os

os.system("sudo cp fw.fw /var/lib/lxc/fw/rootfs/root")
os.system("nmap -F 20.20.2.2")
os.system("sudo lxc-attach --clear-env -n fw -- chmod 777 /root/fw.fw")
os.system("sudo lxc-attach --clear-env -n fw -- sudo /root/fw.fw")
os.system("nmap -F 20.20.2.2")

