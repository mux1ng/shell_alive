# coding=utf-8

import sqlite3 as db
import requests

def readDB(exectCmd="select * from shell", db_path="data.db"):
	conn = db.connect(db_path)
	cursor = conn.cursor()
	conn.row_factory = db.Row
	cursor.execute(exectCmd)
	rows = cursor.fetchall()
	return rows

def getProxy(proxyType, host, port):
	if proxyType != "NO_PROXY":
		proxyType = proxyType.lower()
		proxyType = "socks5" if proxyType == "socks" else proxyType
		proxies = {
			"http": "{}://{}:{}".format(proxyType, host, port),
			"https": "{}://{}:{}".format(proxyType, host, port)
		}
		return proxies
	else:
		return None

def connectTest(url, proxies=""):
	headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
	try:
		r = requests.get(url, headers=headers, timeout=3, proxies=proxies)
		if r.status_code == 200:
			return True
		else:
			return False
	except:
		return False

def main():
	rows = readDB()
	for row in rows:
		proxies = getProxy(proxyType=row[12], host=row[13], port=row[14])
		if(connectTest(url=row[1], proxies=proxies)):
			print(row[1])

if __name__ == '__main__':
	main()
