#!/usr/bin/python36
import subprocess
print("content-type: text/html")
print()
print("<h1>Docker Portal</h1>")
x = subprocess.getoutput("sudo docker images")
print("<form action='http://192.168.43.72/cgi-bin/docker.py'>")
print("Enter your docker name : ")
print("<input name='n' />")
print("<br />")
print("Select your image name:")
print("<select name='img'>")
for   i  in  x.split("\n")[1:]:
        j = i.split()
        print("<option>" +  j[0] +  ":"  + j[1] +  "</option>")
print("</select>")
print("<input type='submit' />")
print("</form>")
print('''<iframe hieght=75% width=100% name="dockersiab"></iframe>''')
#print("helo")
output=subprocess.getoutput("sudo docker container ps -a")
#print(output)
container_list = output.split("\n")
#print(container_list)
#print("<iframe width='100%' name='myconsole'></iframe>")

print("""
<table border='5' width='100%'>
<tr>
<th>Container Name</th>
<th>Image Name</th>
<th>Status</th>
<th>Start</th>
<th>Stop</th>
<th>Terminate</th>
<th>Console</th>
</tr>""")

for c in container_list[1:]:
	if "Up" in c:
		cstatus = "running"
	elif  "Exited" in c:
		cstatus = "stopped"
	else:
		status = "unknown status"
	c_details  =  c.split()
	cname =  c_details[-1]
	imagename = c_details[1]

	print('''
	<tr>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td><a href='http://192.168.43.72/cgi-bin/docker_start.py?s={}'>Start</a></td>
	<td><a href='http://192.168.43.72/cgi-bin/docker_stop.py?s={}'>Stop</a></td>
	<td><a href='http://192.168.43.72/cgi-bin/docker_terminate.py?s={}'>Terminate</a></td>
	<td><a target='dockersiab' href='http://192.168.43.72:4202'>Console</a></td>
	</tr>
	'''.format(cname, imagename, cstatus, cname, cname, cname, cname))
print("</table>")




#http://192.168.43.72:4200

