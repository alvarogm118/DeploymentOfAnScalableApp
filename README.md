# DeploymentOfAnScalableApp
This is the deployment of an scalable application (a Quiz) using Python, VNX and more tools.
There is a picture of the setting attached.

First of all, it is necessary to install the VM (with the VNX installed) on VirtualBox:
https://mega.nz/#!ogFmiQ4L!pSUNKFv1o0fyTQKSw4tEmdIdZwc_hfJFEWJ6LvzGM48

Also, the "VM VistualBox Extension Pack" is needed.

After installing the VM, access to a terminal and download and decompress the setting by typing:
  - wget http://idefix.dit.upm.es/cdps/pc2/pc2.tgz
  - sudo vnx --unpack pc2.tgz
  - cd pc2
  - bin/prepare-pc2-vm

Finally, you download this repository in the folder pc2 inside the VM and run the commands to create and initialitate the setting.

For create and initialiate, run the command: python 1Deploy.py

Then, just wait until everything is ready and the website (Quiz) will be available using the URL: http://20.20.20.2:80

If you want to add a fourth server, just type: python s4.py

If you want to stop and destroy the setting, it is important to do it in this order:
  - If you have added the new server, first: sudo vnx -f s4.mxl --destroy
  - To destroy the rest: sudo vnx -f pc2.xml --destroy
  
This project uses a firewall (that only allows traffic to the balacer, lb), a MariaDB database, glusters (using NAS), Haproxy with Round robin and the Quiz web app.

If you want to learn more about each part, there is a python file for each one and also a document (in spanish) explaining them.
