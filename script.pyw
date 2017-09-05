import time
from datetime import datetime as dt

'''
create a while infinite loop
check if time is in between specified hours
create a list of required hosts to be blocked
open the file and save the contents in a var
check if the desired hostname exists
if -- delete the existing hosts
else- then append the name at the bottom as 127.0.0.1  hostname

'''

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc"
redirect_url = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","twitter.com","www.twitter.com"]

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,2) < dt.now() <  dt(dt.now().year,dt.now().month,dt.now().day,3):
		with open(hosts_path,'r+') as file:
			contents = file.read()
			for website in website_list:
				if website in contents:
					pass
				else:
					file.write("\n" + redirect_url + "\t" + website + "\n")
	else:
		with open(hosts_path,'r+') as file:
			contents =file.readlines()
			file.seek(0)
			for line in contents:
				if not any(website in line for website in website_list):
					file.write(line)

			file.truncate()






	time.sleep(5)