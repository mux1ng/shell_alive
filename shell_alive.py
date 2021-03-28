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

def connectTest(url):
	headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
	try:
		r = requests.get(url, headers=headers, timeout=3)
		if r.status_code == 200:
			return True
		else:
			return False
	except:
		return False

def main():
	rows = readDB()
	for row in rows:
		if(connectTest(url=row[1])):
			print(row[1])

if __name__ == '__main__':
	main()