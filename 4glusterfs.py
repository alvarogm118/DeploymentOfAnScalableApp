import sys
import os

os.system("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 20.20.4.22")
os.system("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 20.20.4.23")
os.system("sudo lxc-attach --clear-env -n nas1 -- gluster peer status")
os.system("sudo lxc-attach --clear-env -n nas1 -- gluster volume create nas replica 3 20.20.4.21:/nas 20.20.4.22:/nas 20.20.4.23:/nas force")
os.system("sudo lxc-attach --clear-env -n nas1 -- gluster volume start nas")
os.system("sudo lxc-attach --clear-env -n nas1 -- gluster volume info")
#Se ha replicado nas1 en nas2 y nas3 y todo lo que se modifique en este aparece en los otros 2.

nases = ["nas1", "nas2", "nas3"]
for item in nases:
	os.system("sudo lxc-attach --clear-env -n "+ item +" -- gluster volume set nas network.ping-timeout 5")

servers = ["s1", "s2", "s3"]
for item in servers:
	os.system("sudo lxc-attach --clear-env -n "+ item +" -- mkdir /mnt/nas")
	os.system("sudo lxc-attach --clear-env -n "+ item +" -- mount -t glusterfs 20.20.4.21:/nas /mnt/nas")
