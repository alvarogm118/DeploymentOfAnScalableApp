import sys
import os


os.system("sudo vnx -f pc2.xml --create")
os.system("python3 2fw.py")
os.system("python3 3mariaBBDD.py")
os.system("python3 4glusterfs.py")
os.system("python3 5configQuiz.py")
os.system("python3 6haproxy.py")


