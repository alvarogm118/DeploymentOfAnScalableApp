import sys
import os
import time

os.system("sudo vnx -f s4.xml --create")
time.sleep(13)

#Glusterfs
os.system("sudo lxc-attach --clear-env -n s4 -- mkdir /mnt/nas")
os.system("sudo lxc-attach --clear-env -n s4 -- mount -t glusterfs 20.20.4.21:/nas /mnt/nas")

#ConfigQuiz
os.system("sudo lxc-attach --clear-env -n s4 -- sudo apt update")
os.system("sudo lxc-attach --clear-env -n s4 -- sudo apt -y install nodejs")
os.system("sudo lxc-attach --clear-env -n s4 -- sudo apt -y install npm")
os.system("sudo lxc-attach --clear-env -n s4 -- git clone https://github.com/CORE-UPM/quiz_2020.git")
os.system("sudo lxc-attach --clear-env -n s4 -- mv /quiz_2020 root/")
os.system("sudo lxc-attach --clear-env -n s4 -- bash -c \"cd /root/quiz_2020; mkdir -p public/uploads; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www\"")

#haproxy
os.system("sudo cp s4/haproxy.cfg /var/lib/lxc/lb/rootfs/etc/haproxy")
os.system("sudo lxc-attach --clear-env -n lb -- sudo service haproxy restart")
os.system("sudo cp s4/layout.ejs /var/lib/lxc/s4/rootfs/root/quiz_2020/views")
