#!/usr/bin/python3

import requests
import webbrowser

url=input('ENTER URL OR IP\n>>>')
i=0
d=''
while True:
	try:
		requests.get(url)
		print('досим '+str(i)+': '+url)
	except:
		print("Request didn't connect to server. It means:\n1)server was successfully break")
		print("2) server with sequrity")
		print("do you want to check what mean?[y/n]")
		d=input()
		if(d=='y'):
			webbrowser.open(url)
		else:
			print('good bye...')
		break
	i+=1
