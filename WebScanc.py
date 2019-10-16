#!/usr/bin/python
import requests
import time
import os
import re
import sys

def Title():
	print('''



 /$$$$$$$$                      /$$$$$$
| $$_____/                     /$$$_  $$
| $$        /$$$$$$   /$$$$$$ | $$$$\ $$  /$$$$$$
| $$$$$    /$$__  $$ /$$__  $$| $$ $$ $$ /$$__  $$
| $$__/   | $$  \__/| $$  \__/| $$\ $$$$| $$  \__/
| $$      | $$      | $$      | $$ \ $$$| $$
| $$$$$$$$| $$      | $$      |  $$$$$$/| $$
|________/|__/      |__/       \______/ |__/




		''')

def Web_Scan_Data(ip):
	url = 'http://api.webscan.cc/?action=query&ip=%s' % ip
	Data = requests.get(url)
	Clear_Data = Data.text.encode('utf-8')
	Clear_Data = Clear_Data.replace('[','')
	Clear_Data = Clear_Data.replace(']','')
	Clear_Data = Clear_Data.replace('{','')
	Clear_Data = Clear_Data.replace('}','')
	Clear_Data = Clear_Data.replace('"domain":"','')
	Clear_Data = Clear_Data.replace('"','')
	Clear_Data = Clear_Data.replace(',title:,','\n')
	Clear_Data = Clear_Data.replace(',title:','')
	Clear_Data = Clear_Data.replace('\\','')
	return Clear_Data

def Web_Scan_Cduan(ip):
	ip = ip.split('.')
	A = ip[0]
	B = ip[1]
	C = ip[2]
	Cduan = A + '.' + B + '.' + C + '.'
	Dir = os.getcwd()
	FileDir = 'ok/' + Cduan + '1' + '.txt'
	if os.path.exists('ok') == True:
		pass
	else:
		os.mkdir('ok')
	if os.path.exists(FileDir) == True:
		pass
	else:
		fp = open(FileDir,'w')
	for i in range(255):
		fp = open(FileDir,'a')
		Cduan_Scan = Cduan + str(i)
		Url_Data = Web_Scan_Data(Cduan_Scan)
		print("Scan Now:" + Cduan_Scan)
		time.sleep(0.5)
		print(Url_Data)
		print("----------------------------------------------------------------")
		if 'null' in Url_Data:
			pass
		else:
			fp.write(Url_Data)
			fp.write('\n')
			fp.close()
def main():
	ip = sys.argv[1]
	Title()
	time.sleep(2)
	Web_Scan_Cduan(ip)
if __name__ == '__main__':
	main()%
