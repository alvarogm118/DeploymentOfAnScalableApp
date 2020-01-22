import sys
import os

os.system("sudo lxc-attach --clear-env -n lb -- sudo apt update")
os.system("sudo lxc-attach --clear-env -n lb -- apt -y install haproxy")
os.system("sudo cp haproxy.cfg /var/lib/lxc/lb/rootfs/etc/haproxy")
os.system("sudo lxc-attach --clear-env -n lb -- sudo service haproxy restart")

servers = ["s1", "s2", "s3"]
for item in servers:
	os.system("sudo cp "+ item +"/layout.ejs /var/lib/lxc/"+ item +"/rootfs/root/quiz_2020/views")
