from version import Version
from requests import get
from color import color

from time import sleep
from re import findall
from inputimeout import TimeoutOccurred, inputimeout
import json

class data:
	def __init__(self):
		
		self.wbm = [13,18]
		self.AniGameId = '571027211407196161'
		
		with open('settings.json', "r") as file:
			data = json.load(file)
			self.token = data["token"]
			
	def check(self):
		version = self.Version()
		if self.token and self.channel == 'nothing':
			print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
			sleep(2)
			
		else:
			response = get('https://discord.com/api/v9/users/@me',headers={"Authorization": self.token})
			if not response.ok:
				print(f"{color.fail} !!! [ERROR] !!! {color.reset} Invalid Token")
				sleep(2)


	
a = data()
a.check()
