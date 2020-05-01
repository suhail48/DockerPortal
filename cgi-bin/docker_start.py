#!/usr/bin/python36

import subprocess
import cgi

print("content-type: text/html")


form = cgi.FieldStorage()

cname = form.getvalue("s")

cmd = "sudo docker start {}".format(cname)

x = subprocess.getoutput(cmd)
cmd = "sudo docker exec {} /usr/sbin/shellinaboxd -u shellinabox --cert=/var/lib/shellinabox --port=4200 -t --disable-ssl-menu".format(cname)

x = subprocess.getoutput(cmd)

print("location: http:192.168.43.72/cgi-bin/run.py")
print()




