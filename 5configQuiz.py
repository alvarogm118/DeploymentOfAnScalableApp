import sys
import os

servers = ["s1", "s2", "s3"]
for item in servers:
	os.system("sudo lxc-attach --clear-env -n "+ item +" -- sudo apt update")
	os.system("sudo lxc-attach --clear-env -n "+ item +" -- sudo apt -y install nodejs")
	os.system("sudo lxc-attach --clear-env -n "+ item +" -- sudo apt -y install npm")
	os.system("sudo lxc-attach --clear-env -n "+ item +" -- git clone https://github.com/CORE-UPM/quiz_2020.git")
	os.system("sudo lxc-attach --clear-env -n "+ item +" -- mv /quiz_2020 root/")
	if item == "s1":
		os.system("sudo lxc-attach --clear-env -n "+ item +" -- bash -c \"cd /root/quiz_2020; mkdir -p public/uploads; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; npm run-script migrate_cdps; npm run-script seed_cdps; ./node_modules/forever/bin/forever start ./bin/www\"")
	else:
		os.system("sudo lxc-attach --clear-env -n "+ item +" -- bash -c \"cd /root/quiz_2020; mkdir -p public/uploads; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www\"")

