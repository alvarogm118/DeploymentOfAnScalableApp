import sys
import os

os.system("sudo lxc-attach --clear-env -n bbdd -- apt update")
os.system("sudo lxc-attach --clear-env -n bbdd -- apt -y install mariadb-server")
os.system("sudo lxc-attach --clear-env -n bbdd -- sed -i -e 's/bind-address.*/bind-address=0.0.0.0/' -e 's/utf8mb4/utf8/' /etc/mysql/mariadb.conf.d/50-server.cnf")
os.system("sudo lxc-attach --clear-env -n bbdd -- systemctl restart mysql")

os.system("sudo lxc-attach --clear-env -n bbdd -- mysqladmin -u root password xxxx")
os.system("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"CREATE USER 'quiz' IDENTIFIED BY 'xxxx';\"")
os.system("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"CREATE DATABASE quiz;\"")
os.system("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'localhost' IDENTIFIED by 'xxxx';\"")
os.system("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'%' IDENTIFIED by 'xxxx';\"")
os.system("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"FLUSH PRIVILEGES;\"")

'''
servers = ["s1", "s2", "s3"]
for item in servers:
	os.system("sudo lxc-attach --clear-env -n "+ item +" -- apt -y install mariadb-client")
	os.system("sudo lxc-attach --clear-env -n "+ item +" -- mysql -h 20.20.4.31 -u quiz --password='xxxx' quiz")
'''