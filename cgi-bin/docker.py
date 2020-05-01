#!/usr/bin/python36


import subprocess
import cgi

print("content-type: text/html")
print("location: http://192.168.43.72/cgi-bin/run.py")
print()


form = cgi.FieldStorage()

docker_name = form.getvalue("n")
docker_image = form.getvalue("img")

docker_run = "sudo docker run -d -i -t -p 4202:4200 -p 1234:80 -v mystorage:/dir --name  {}  {}".format(docker_name ,  docker_image)


x = subprocess.getoutput(docker_run)

print("location: http://192.168.43.72/cgi-bin/run.py")
print()


